# Toward an Antimatter Periodic Table

Version: `v1.0.0`
DOI: none assigned
License: CC BY 4.0

## Authors

- Dr. Martin Dres (Independent Researcher)

## Overview

This repository develops a scientific framework for an antimatter periodic table.
It does not propose a new chemical periodic law. Instead, it treats the
antimatter periodic table as a CPT-isomorphic evidence-status and preparedness
framework over the classical periodic table.

This repository release does not claim that antimatter has a distinct chemical
periodic law. The table is an evidence-status representation. Neutral
antihelium atoms and heavier neutral anti-atoms are not claimed as
experimentally realized.

The framework separates four domains:

- experimentally confirmed systems, anchored by antihydrogen production,
  trapping, spectroscopy, and gravitational tests;
- theoretically expected structures, based on CPT symmetry and established
  atomic physics;
- open or experimentally unverified systems, including neutral anti-atoms beyond
  antihydrogen, anti-ions, anti-molecules, and prospective antimatter-chemistry
  questions;
- speculative domains, such as large astrophysical antimatter structures or
  hypothetical deviations from matter-antimatter symmetry.

## Core Claim

The central claim is deliberately conservative:

> The antimatter periodic table is a CPT-isomorphic evidence-status and
> preparedness framework, not a new periodic law.

In the manuscript, evidence status is the formal representation layer.
Preparedness is the broader motivation for future anti-atom, anti-ion,
anti-molecule, and astrophysical searches.

Under CPT symmetry, isolated anti-atoms are expected to share the internal
spectral and orbital structure of their matter counterparts. The open problem is
not a replacement for chemical periodicity, but the experimental realization,
storage, characterization, and eventual chemical study of antimatter systems
beyond antihydrogen.

## Main Representation

Version `v1.0.0` uses a split-cell table as the main representation. Each
cell separates:

- the classical orbital/block structure indexed by positive atomic number `Z`;
- the evidence status of the corresponding antimatter system;
- residual or deviation information only when a named observable has data.

The `confidence` column in `data/element_status_table.csv` is a visualization
and triage heuristic only. It is not the manuscript's formal evidence vector.

Mirror or dual layouts are didactic views of charge conjugation only. They must
not be read as negative atomic numbers or as a second periodic law.

Full-size exports of the main split-cell figure are available as:

- `figures/split_cell_table_v1.0.0.svg`
- `figures/split_cell_table_v1.0.0.png`

The release manuscript PDF is available as
`paper/Antimatter_Periodic_Table_Framework_v1.0.0.pdf`.

## Repository Structure

- `paper/` - English LaTeX manuscript and compiled PDF
- `figures/` - generated SVG/PNG exports of the main split-cell table
- `data/` - element status table
- `scripts/` - reproducible figure build helper

## Citation

Dres, M. (2026). *Toward an Antimatter Periodic Table: A Preparedness
Framework.* Version `v1.0.0`.

## Release Status

This repository release is version `v1.0.0` and is released without a DOI. A
DOI-bearing archival release may be prepared separately in the future.

## License

Creative Commons Attribution 4.0 International (CC BY 4.0).
