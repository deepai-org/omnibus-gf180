# First transistor-level agent primitive

`leaky_state.spice` implements a continuous-time, capacitor-backed tracking
state with a six-transistor current-mirror OTA in unity negative feedback.
It uses GF180 `nfet_03v3`/`pfet_03v3` models, not behavioral gain sources.
The testbench supplies ideal power, input voltage and reference current. The
storage capacitor now instantiates the GF180 2 fF/µm² M4–M5 MIM model at
31.6×31.6 µm (about 2.02 pF including modeled fringe). Geometry is specified
electrically, not laid out or DRC-qualified.

This targets an actual model operation such as attention predicted telemetry:
`d(predicted_feedback)/dt = (estimate - predicted_feedback)/0.5`.
The OTA supplies a nonlinear function of input minus stored voltage; near zero
error, `tau ≈ C/gm`. It is **not** yet an implementation of the entire attention
block, of an arbitrary weighted sum, or of the complete agent.

Candidate encoding for this experiment is `V = 1.63 + 0.04*x` volts, x in [0,1].
The physical-to-normalized time scale must be chosen from measured dynamics;
the simulator does not establish exact first-order equivalence. The cell has no
clock and does not time-share its state. Bias generation, reset, readout/loading,
and interconnect are separate obligations.

## Reproduce

```sh
python3 circuits/screen_leaky_state.py --pdk /path/to/gf180/ngspice
python3 circuits/screen_leaky_state.py --pdk /path/to/gf180/ngspice --output evidence/leaky-state-mim --sweep
```

The directory must contain `design.ngspice`, `sm141064.ngspice` and their
referenced `sm141064.spice`/`sm141064_mim.spice` model files. The local
run used `/home/ubuntu/svalbard/scratch/transceiver-pad-pdk/ngspice` read-only.
No PDK files are copied into this repository. Requires ngspice and NumPy.
Generated decks, traces, logs and source/PDK hashes are in
the selected output directory; rerunning replaces that experiment's generated
files. `evidence/leaky-state` retains the original ideal-capacitor experiment
and its hashes are historical. `evidence/leaky-state-mim` is the current sweep.

## Historical ideal-capacitor result, 27°C, 3.3 V, unloaded output

| Reference current | 63% rise delay | Step gain | Worst endpoint offset | Mean rail power |
|---|---:|---:|---:|---:|
| 1 nA | 137.0 µs | 0.99724 | 2.815 mV | 6.73 nW |
| 3 nA | 47.0 µs | 0.99731 | 2.658 mV | 20.10 nW |
| 10 nA | 15.7 µs | 0.99729 | 2.575 mV | 66.76 nW |

Input rises from 1.63 to 1.67 V in 1 µs, then returns. Rise delay is the first
sample crossing 63% of the measured endpoint difference, relative to the end
of the input ramp; it is not a fitted pole or an AC bandwidth measurement.
The 2 µs requested transient step limits precision, especially in the fastest
case. Power includes both OTA and the reference branch's rail current but not
the circuitry that would generate that current or drive the input.

The approximately 7% normalized offset is a **substitution blocker**, not
removed by interpreting the measured final value as the ideal target. It needs
explicit treatment and mismatch qualification before this can replace the
software integrator. A successful nominal trace does not prove the design fits.

## Current PDK-MIM and loading screen

The three nominal bias cases plus 17 additional cases cover MOS typical/SS/FF,
−40/27/125°C, and 0/1 pF additional output capacitance at 3 nA reference current.
All 20 simulations produce finite traces and return to their original endpoint.
MIM process variation is held typical; this is not a full process/supply/
temperature or statistical sign-off.

At 3 nA across the swept cases, measured step gain is 0.99712–0.99744,
endpoint offset is 2.069–3.550 mV, and 63% rise delay is 36.7–93.1 µs.
At typical/27°C, adding 1 pF changes the delay from 47.0 to 71.0 µs without
removing the DC offset. At 1 nA nominal, replacing ideal storage with the MIM
model changes delay from 137 to 139 µs. No trace processing subtracts offset.

The worst observed offset is nearly 9% of the 40 mV signal span. This remains
the main demonstrated substitution problem. Differential encoding or another
offset treatment must be designed and verified, including mismatch; nominal
cancellation alone would not settle it. Ideal added capacitance is only a load
screen, not actual downstream-transistor or extracted interconnect loading.

## Still required

- Operating range/common-mode, supply, mixed MOS corners and MIM-corner sweeps.
- Actual downstream gate loading, finite-bandwidth response and noise/mismatch.
- Offset mitigation or a justified calibrated encoding, propagated into the
  agent rather than silently subtracting error in the measurement script.
- Storage-capacitor layout, bias/reference and reset implementation.
- Layout, DRC/LVS, extracted response and area; no physical fit claim yet.
- Substitution of measured/nonideal dynamics into the same agent tasks.
