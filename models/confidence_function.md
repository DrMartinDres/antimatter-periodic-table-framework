# Confidence Function

The CSV `confidence` field is a visualization and triage heuristic, not the
formal evidence vector used in the manuscript and not a claim that CPT symmetry
itself is doubtful.

## Working Heuristic

For the CSV dataset this is encoded as a compact practical scale:

- `1.00`: neutral anti-atom produced, trapped, and precisely characterized.
- `0.65`: antinucleus observed, but neutral anti-atom not established.
- `0.35`: light anti-atom structure is CPT-expected, but not realized.
- `0.20`: higher anti-atoms remain a preparedness domain.

## Current Assignments

- `Z = 1`: `1.00`, because antihydrogen is the experimental anchor.
- `Z = 2`: `0.65`, because the evidence is for antihelium nuclei, not
  neutral antihelium atoms.
- `3 <= Z <= 10`: `0.35`, because the structure is theoretically expected but
  the neutral anti-atoms are not realized.
- `Z > 10`: `0.20`, because experimental accessibility and complexity become
  increasingly limiting.

These values are visualization and triage parameters only. They should not be
collapsed into the manuscript's formal evidence vector and should be
recalibrated when new anti-atom, anti-ion, anti-molecule, spectroscopy, or
astrophysical data are added.
