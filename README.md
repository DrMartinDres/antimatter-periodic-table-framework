# Toward an Antimatter Periodic Table

Local review candidate: `v1.0.0-rc2`  
DOI: to be reserved before final Zenodo publication  
License: Creative Commons Attribution 4.0 International (CC BY 4.0)

## Authors

- Dr. Martin Dres
- Emanuel Dres
- Jonathan Dres

## Overview

This repository develops a scientific framework for an antimatter periodic table.
It does not propose a new chemical periodic law. Instead, it treats the
antimatter periodic table as a CPT-isomorphic evidence-status framework over the
classical periodic table.

The framework separates four domains:

- experimentally confirmed systems, anchored by antihydrogen production,
  trapping, spectroscopy, and gravitational tests;
- theoretically expected structures, based on CPT symmetry and established
  atomic physics;
- open or experimentally unverified systems, including neutral anti-atoms beyond
  antihydrogen, anti-ions, anti-molecules, and antimatter chemistry;
- speculative domains, such as large astrophysical antimatter structures or
  hypothetical deviations from matter-antimatter symmetry.

## Core Claim

The central claim is deliberately conservative:

> The antimatter periodic table is a CPT-isomorphic preparedness framework, not
> a new periodic law.

In the manuscript, the formal contribution is described more narrowly as a
CPT-isomorphic evidence-status framework. Preparedness is the broader motivation
for future anti-atom, anti-ion, anti-molecule, and astrophysical searches.

Under CPT symmetry, isolated anti-atoms are expected to share the internal
spectral and orbital structure of their matter counterparts. The open problem is
not a replacement for chemical periodicity, but the experimental realization,
storage, characterization, and chemical study of antimatter systems beyond
antihydrogen.

## Main Representation

The release candidate uses a split-cell table as the main representation. Each
cell separates:

- the classical orbital/block structure indexed by positive atomic number `Z`;
- the evidence status of the corresponding antimatter system;
- residual or deviation information only when a named observable has data.

The `confidence` column in `data/element_status_table.csv` is a visualization
and triage heuristic only. It is not the manuscript's formal evidence vector.

Mirror or dual layouts are didactic views of charge conjugation only. They must
not be read as negative atomic numbers or as a second periodic law.

## Repository Structure

- `paper/` - English LaTeX manuscript and compiled review PDF
- `figures/` - generated PDF figures used for review
- `data/` - element status table
- `models/` - conceptual model notes
- `scripts/` - reproducible figure build helper
- `docs/de/` - German working drafts, not part of the English release candidate

## Citation

For review purposes, cite:

Dres, M., Dres, E., & Dres, J. (2026). *Toward an Antimatter Periodic Table: A
Preparedness Framework.* Local review candidate `v1.0.0-rc2`. DOI: to be
reserved before final Zenodo publication.

The final public citation should be updated after the Zenodo DOI has been
reserved and inserted into the manuscript and metadata.

## Release Status

This repository state is intended for local pre-Zenodo review only.

Deferred actions:

- DOI reservation
- Zenodo upload
- Zenodo publication
- GitHub release tagging for the final public record

Before any public release, run the release checks described in `AGENTS.md` and
confirm that no release-relevant files contain German text, DOI placeholders, or
claims implying a new chemical periodic law.

## License

Creative Commons Attribution 4.0 International (CC BY 4.0).
