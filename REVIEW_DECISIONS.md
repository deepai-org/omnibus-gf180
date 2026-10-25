# Instrumentation review decisions

2026-10-25. Incorporated into DESIGN_PLAN.md; no circuit performance or area is yet measured. The supplied review labels twelve proposals A1–A12 despite its heading saying ten.

| Proposal | Decision |
|---|---|
| A1 simultaneous capture | Adopt 192-channel target/96 fallback with common strobe and two existing outputs. Budget differential hold capacitors, buffers, droop, skew, acquisition and kickback. Does not eliminate uncertainty or capture an entire waveform. |
| A2 clamps and cut | Adopt 32 clampable nodes, four eight-node sets and a declared 96/96 cut. Start exhaustive state acquisition at four nodes; distinguish state-table coverage from full IIT computation and one cut from a minimum partition. |
| A3 passive pickups | Adopt a small coupon/readout allocation with shielded and conducted controls. Reject universal orientation-sign discrimination and zero-cost active readout assumptions. Baseline is coupling measurement, not CEMI compliance. |
| A4 efference copy | Adopt 16 reserved existing edges with independent lesions and action/world counterfactual tests. A copied command predicts consequences; it is not evidence they occurred. |
| A5 same-die controls | Adopt five registered conditions and readback CRC plus host SHA-256 manifest. No extra hash pin. Exact acyclic matching requires graph feasibility; report silence and motor disconnection are different conditions. |
| A6 heterogeneity | Adopt three-bit gain trim and predeclared calibration/heterogeneity conditions. Does not establish a CLT requirement or compensate every mismatch. |
| A7 capacity sweep | Adopt inhibitory-bias sweep; characterize occupancy 0–4 for the existing four candidate assemblies, not a promised 1–6 range. |
| A8 bounded reports | Adopt telemetry with an independently validated behavioral meaning. Predicting a hardwired code from its source state is tautological; compare against controlled actual attention and future consequences instead. |
| A9 internal stimulus | Optional seeded sequencer/LFSR and coarse DAC fixture within the budget. Distinguish clocked internal environment from clock-stopped external-stimulus testing; PRNG is not entropy. |
| A10 adaptation | Adopt disableable adaptation on 40 selected nodes, with target time-scale ratio >=10 and explicit auxiliary-state accounting. No claim that adaptation alone guarantees ignition or criticality. |
| A11 overrun order | Protect capture/clamps and provenance; remove expansion, try lower weight resolution, then 96 captures and simplified optional service before reducing task scope. No unconditional promise that all coupons survive a hard physical limit. |
| A12 paradigms | Adopt masking, sustained conflict and report-silent controls with explicit timing and validation requirements. Biological comparisons remain qualitative unless independently justified. |

Storage is screened at 45% effective utilization, with a 35–60% sensitivity range, not assumed proven at either endpoint. Binary-weighted DACs are candidates: 1+2+4+8 still uses 15 unit widths. Capacitor arithmetic is 192 × 2 pF = 384 pF = 0.000384 µF; kT/C alone is not total circuit noise.

The exact CLT source, mathematical estimator and valence postulate remain unresolved. Neither the supplied review nor this revision establishes satisfaction of CLT, whole-chip IIT or CEMI. Bounded resource regulation is deliberately not a test of genuine existential precarity.
