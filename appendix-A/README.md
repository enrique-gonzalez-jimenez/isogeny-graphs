# Appendix A: An LMFDB Zoo of Isogeny Graphs

This repository contains the computations for **Appendix A: An LMFDB Zoo of Isogeny Graphs** in:

> Alexander J. Barrios, Enrique Gonzalez-Jimenez, and Ivan Novak,  
> *Isogeny Graphs of Elliptic Curves in Characteristic Zero*,  
> arXiv:2608.02494 (2026).

- **Paper:** https://arxiv.org/abs/2608.02494
- **Repository:** https://github.com/enrique-gonzalez-jimenez/isogeny-graphs

## Description

The SageMath script queries the LMFDB database for isogeny classes of elliptic curves defined over `Q` and over number fields, subject to the condition

```text
cm_type != 1
```

For every pair

```text
(isogeny class size, isogeny class degree)
```

the script selects one representative isogeny class according to the following ordered criteria:

1. Prefer a class defined over `Q`, whenever one exists.
2. Among classes over `Q`, minimize the conductor.
3. Otherwise, minimize the degree of the number field of definition.
4. Minimize the absolute value of the field discriminant.
5. Minimize the norm of the conductor of the isogeny class.
6. Use the LMFDB label as a deterministic final tie-breaker.

The results are ordered first by isogeny class size and then by isogeny class degree. Each row has the form

```text
size, degree, LMFDB_label
```

## Requirements

The computation is intended to run in a SageMath environment with the LMFDB database interface installed and configured. The following command must work in SageMath:

```python
from lmfdb import db
```

## Usage

Start SageMath in the appropriate Conda environment and run:

```bash
sage lmfdb_isogeny_pairs.sage
```
