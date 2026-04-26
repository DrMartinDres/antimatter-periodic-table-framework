# Deviation Framework

The deviation framework is reserved for genuine matter-antimatter residuals.
Missing evidence is not treated as a physical deviation.

## Residual Definition

For an observable `O`, the dimensionless residual is:

```text
rho_O(overline(E_Z)) =
  (O_antimatter(Z) - O_matter(Z)) / sigma_O(Z)
```

- `sigma_O`: combined experimental and reference uncertainty for the comparison.
- `rho_O` compatible with zero: compatible with CPT expectations within
  finite uncertainty, not an exact zero residual.
- `rho_O < 0`: significant negative residual.
- `rho_O > 0`: significant positive residual.
- `?`: unmeasured, not a deviation.
- `N`: antinucleus-only evidence, neutral anti-atom not established.

## Deviation Classes

- `none`: measured compatibility within uncertainty.
- `status`: evidence level differs from the matter reference.
- `unknown`: neutral anti-atom or observable is not measured.
- `residual`: a quantified nonzero residual exists for a named observable.

## Notation

```text
overline(E_Z)[O:rho_O]
```

Example:

```text
overline(H)[1S-2S:rho_1S-2S]
```

In the current table, antihydrogen spectroscopy should be described in words as
compatible with zero within current uncertainty. The `overline(He)` entry, where
only antihelium-nucleus evidence exists, remains `N`, not a residual.
