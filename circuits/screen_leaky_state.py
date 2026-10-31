"""GF180 transistor-level leaky-state screen; not layout/sign-off evidence."""
import argparse
import hashlib
import json
from pathlib import Path
import subprocess
import numpy as np


def screen(pdk, output, sweep=False):
    pdk, output = pdk.resolve(), output.resolve()
    output.mkdir(parents=True, exist_ok=True)
    cell = Path(__file__).with_name('leaky_state.spice').resolve()
    rows = []
    cases = [(i, 'typical', 27, 0) for i in (1e-9, 3e-9, 10e-9)]
    if sweep:
        cases += [(3e-9, corner, temp, load) for corner in ('typical', 'ss', 'ff')
                  for temp in (-40, 27, 125) for load in (0, 1e-12)
                  if (corner, temp, load) != ('typical', 27, 0)]
    for current, corner, temp, load in cases:
        work = output / f'{current*1e9:g}nA-{corner}-{temp}C-{load*1e12:g}pF'
        work.mkdir(exist_ok=True)
        deck = f'''GF180 leaky state transistor test
.include {pdk}/design.ngspice
.lib {pdk}/sm141064.ngspice {corner}
.lib {pdk}/sm141064.ngspice mimcap_typical
.include {cell}
.temp {temp}
.options reltol=1e-5 abstol=1e-15 vntol=1e-8
VDD VDD 0 3.3
IREF VDD BIAS {current}
VIN IN 0 PWL(0 1.63 1m 1.63 1.001m 1.67 3m 1.67 3.001m 1.63 5m 1.63)
XSTATE IN OUT VDD 0 BIAS leaky_state
{f'CLOAD OUT 0 {load}' if load else '* No extra output capacitance'}
.control
set wr_singlescale
set wr_vecnames
tran 2u 5m
wrdata trace.txt v(IN) v(OUT) i(VDD)
quit
.endc
.end
'''
        (work / 'test.spice').write_text(deck)
        proc = subprocess.run(['ngspice', '-b', 'test.spice'], cwd=work,
                              text=True, capture_output=True, timeout=60)
        (work / 'ngspice.log').write_text(proc.stdout + proc.stderr)
        if proc.returncode:
            raise RuntimeError(f'ngspice failed; inspect {work}/ngspice.log')
        trace = np.loadtxt(work / 'trace.txt', skiprows=1)
        t, vin, vout, supply = trace.T
        before = float(np.interp(.00099, t, vout))
        after = float(np.interp(.00299, t, vout))
        target = before + (after-before)*(1-np.exp(-1))
        segment = (t >= .001001) & (t < .003)
        times, values = t[segment], vout[segment]
        crossings = np.flatnonzero(values >= target)
        tau = None if not len(crossings) else float(times[crossings[0]] - .001001)
        rows.append(dict(reference_current_a=current, corner=corner, temperature_c=temp,
                         additional_load_f=load, before_v=before, after_v=after,
                         endpoint_error_v=max(abs(before-1.63), abs(after-1.67)),
                         step_gain=(after-before)/.04, rise_63_time_s=tau,
                         final_return_v=float(vout[-1]),
                         mean_supply_power_w=float(-3.3*np.mean(supply)),
                         finite=bool(np.all(np.isfinite(trace)))))
    report = dict(status='MIM_transistor_screen_not_qualified_block', results=rows,
                  simulator=subprocess.check_output(['ngspice','--version'],text=True),
                  source_sha256={str(p): hashlib.sha256(p.read_bytes()).hexdigest()
                                 for p in (cell,Path(__file__).resolve(),pdk/'design.ngspice',pdk/'sm141064.ngspice',pdk/'sm141064.spice',pdk/'sm141064_mim.spice')},
                  limitations=['PDK MIM model, ideal external current reference and capacitive load.',
                               'MIM typical only; no mismatch, supply sweep or actual fanout network.',
                               'No layout, extracted parasitics, reset or full-agent substitution.'])
    (output/'summary.json').write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps(rows,indent=2))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--pdk',type=Path,required=True)
    parser.add_argument('--output',type=Path,default=Path('evidence/leaky-state'))
    parser.add_argument('--sweep',action='store_true')
    args = parser.parse_args()
    screen(args.pdk,args.output,args.sweep)
