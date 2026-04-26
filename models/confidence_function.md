# Confidence Function

The current framework uses confidence as an evidence-readiness score, not as a
claim that CPT symmetry itself is doubtful.

## Working Heuristic

```text
C(Z) = evidence_weight * realization_status * characterization_status
```

For the CSV dataset this is encoded as a compact practical scale:

- `1.00`: neutral anti-atom produced, trapped, and precisely characterized.
- `0.65`: antinucleus observed, but neutral anti-atom not established.
- `0.35`: light anti-atom structure is CPT-expected, but not realized.
- `0.20`: higher anti-atoms remain a preparedness domain.

## Current Assignments

- `Z = 1`: `1.00`, because antihydrogen is the experimental anchor.
- `Z = 2`: `0.65`, because antihelium has antinucleus status only.
- `3 <= Z <= 10`: `0.35`, because the structure is theoretically expected but
  the neutral anti-atoms are not realized.
- `Z > 10`: `0.20`, because experimental accessibility and complexity become
  increasingly limiting.

These values are visualization and triage parameters; they should be recalibrated
when new anti-atom, anti-ion, anti-molecule, spectroscopy, or astrophysical data
are added.
