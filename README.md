# Isogeny Graphs of Elliptic Curves in Characteristic Zero

Computational resources accompanying the paper

> Alexander J. Barrios, Enrique González-Jiménez, and Ivan Novak,  
> *Isogeny Graphs of Elliptic Curves in Characteristic Zero*,  
> arXiv:2608.02494 (2026).

- **Paper:** <https://arxiv.org/abs/2608.02494>
- **Repository:** <https://github.com/enrique-gonzalez-jimenez/isogeny-graphs>

## Overview

Let $E$ be an elliptic curve over a field $K$ of characteristic zero. Its
isogeny graph $\mathcal{G}(E/K)$ is the undirected edge-weighted graph whose
vertices are the $K$-isomorphism classes of elliptic curves $K$-isogenous to
$E$. Two vertices are joined by an edge of weight $p$ whenever representatives
of the corresponding classes are connected by a $K$-rational isogeny of prime
degree $p$.

The paper classifies the isogeny graphs that can arise when $\mathrm{End}_K(E)\cong\mathbb{Z}.$

The classification is described in terms of the $p$-adic and adelic Galois
representations attached to $E$, together with the modular curves associated
with certain subgroups of $\mathrm{GL}_2(\widehat{\mathbb{Z}}).$

This repository contains SageMath and Magma code used to perform, reproduce,
and verify computations appearing in:

- Section 8: determining the isogeny graph from the adelic Galois
  representation;
- Section 9: modular curves associated with isogeny graphs;
- Section 10: explicit classification of genus-zero isogeny graphs;
- Appendix A: an LMFDB zoo of isogeny graphs; and
- Appendix B: tables for the explicit classification of genus-zero isogeny
  graphs.

## Repository structure

```text
isogeny-graphs/
├── README.md
├── LICENSE
├── CITATION.cff
├── .gitignore
│
├── section-8/
│   ├── README.md
│   ├── image_to_graph_algorithm.sage
│
├── section-9/
│   ├── README.md
│   ├── model_XH.m
│
├── section-10/
│   ├── README.md
│   ├── genus_zero_classification.sage
│
├── appendix-a/
    ├── README.md
    ├── ecnf_cmtype_not1_graph_types_clean.sage
    ├── data/
    ├── figures/
    └── output/

```

## Computational components

### Section 8: Determining the isogeny graph from the adelic Galois representation

**Directory:** `section-8/`  
**Main file:** `section-8/image_to_graph_algorithm.sage`

This SageMath code implements the algorithm in Theorem 8.1.


### Section 9: Modular curves associated with isogeny graphs

**Directory:** `section-9/`  
**Main file:** `section-9/model_XH.m`

This Magma code implements the computations carried out in Section 9.

The classification in the paper associates open subgroups $H\leq\mathrm{GL}_2(\widehat{\mathbb{Z}})$

with possible isogeny graphs. The corresponding modular curve is denoted by $X_H$.

The code supports the calculations used in:

- Lemma 9.10;
- the classification of the genus-zero modular curves associated with isogeny graphs;
- the classification of the genus-one modular curves associated with isogeny graphs; and
- the computation of the models recorded in Table 5.

The genus-zero modular curves associated with isogeny graphs consist of the
classical modular curves $X_0(n)$ together with the four nonclassical cases
associated with $H_9^1, H_{16}^2, H_2^0\times H_9^1,$ and $H_{25}^1.$

See `section-9/README.md` for detailed execution instructions and a
description of the expected output.

### Section 10: Explicit classification of genus-zero isogeny graphs

**Directory:** `section-10/`  
**Main file:** `section-10/genus_zero_classification.sage`

The SageMath code in this directory supports the computations in Section 10 and Appendix B.

Section 10 completes the explicit classification of the isogeny graphs
associated with genus-zero modular curves. The classical cases arising from
$X_0(n)$ are complemented by the four cases associated with $H_9^1,H_{16}^2,H_2^0\times H_9^1,$ and $H_{25}^1.$

The corresponding values of $n$ are $n\in\{9,16,18,25\}.$

For these values, the code constructs and verifies the extended parametrized
families $\mathcal{C}_{n,m}^{1}(t,d)$ appearing in Theorem 10.3 and Appendix B.

See `section-10/README.md` for the correspondence between the scripts and the
individual results and tables in the paper.

### Appendix A: An LMFDB zoo of isogeny graphs

**Directory:** `appendix-a/`  
**Main file:** `appendix-a/ecnf_cmtype_not1_graph_types_clean.sage`

This SageMath code produces the data, figures, and report associated with
Appendix A, entitled *An LMFDB Zoo of Isogeny Graphs*.

The computation accesses the LMFDB database of elliptic curves over number
fields and examines the records in the `ec_nfcurves` collection.

## Correspondence between the paper and the code

The principal correspondence is as follows.

### Section 8

`section-8/image_to_graph_algorithm.sage`

implements the algorithm in Theorem 8.1 and determines the pointed isogeny
graph from the image of the adelic Galois representation.

### Section 9

`section-9/model_XH.m`

performs the modular-curve computations used in Lemma 9.10 and computes the
models recorded in Table 5.

### Section 10 and Appendix B

The files in `section-10/`

construct and verify the explicit parametrized families associated with the
genus-zero modular curves considered in Theorem 10.3 and Appendix B.

### Appendix A

`appendix-a/ecnf_cmtype_not1_graph_types_clean.sage`

queries the LMFDB, reconstructs the labeled isogeny graphs from the stored
isogeny matrices, classifies the graph types, selects examples, and produces
the figures and report appearing in the LMFDB zoo.

The numbering above refers to version 1 of the paper on arXiv. If the
numbering changes in a later version of the manuscript, the documentation in
this repository should be updated accordingly.

## Software requirements

### SageMath

The computations in Sections 8 and 10 and Appendix A require SageMath:

<https://www.sagemath.org/>

The exact version used for the final computations should be recorded here:

```text
SageMath version: [TO BE ADDED]
```

### Magma

The computations in Section 9 require Magma:

<https://magma.maths.usyd.edu.au/>

The exact version used for the final computations should be recorded here:

```text
Magma version: [TO BE ADDED]
```

The Section 9 computations also require a local copy of David Zywina's
`Modular` package.

```text
davidzywina/Modular commit: [TO BE ADDED]
```

### LMFDB access

The initial Appendix A database query requires:

- a SageMath environment compatible with the LMFDB codebase;
- access to a local or authorized LMFDB database installation;
- the LMFDB Python and SageMath modules; and
- permission to query the relevant database collections.

The exact import and database connection instructions depend on the local
LMFDB setup and are documented in `appendix-a/README.md`.

The saved offline classification in `appendix-a/data/` can be used to
regenerate the summaries, graph images, and PDF report without performing the
database query again.

## Installation

Clone this repository:

```bash
git clone https://github.com/enrique-gonzalez-jimenez/isogeny-graphs.git
cd isogeny-graphs
```

The SageMath computations in Sections 8 and 10 do not require a separate
installation step beyond a working SageMath installation.

For the Section 9 computations, clone the external `Modular` package:

```bash
git clone https://github.com/davidzywina/Modular.git
```

The path to `Modular.spec` must then be supplied in the relevant Magma script
or local configuration file.

The Appendix A database-query stage must be executed inside an environment
with access to the LMFDB codebase and database.

## Quick start

### Section 8

Move to the corresponding directory:

```bash
cd section-8
```

Run the SageMath program:

```bash
sage image_to_graph_algorithm.sage
```

Examples of admissible input and the corresponding expected graphs should be
provided in:

```text
section-8/examples/
```

### Section 9

Move to the corresponding directory:

```bash
cd section-9
```

After specifying the path to `Modular.spec`, run:

```bash
magma model_XH.m
```

The group data used by the program should be stored in:

```text
section-9/input/
```

The models and other machine-readable output should be stored in:

```text
section-9/output/
```

### Section 10

Move to the corresponding directory:

```bash
cd section-10
```

Run the main SageMath program:

```bash
sage genus_zero_classification.sage
```

If the verification is divided into several programs, the individual
verification scripts can be stored and executed from:

```text
section-10/verification/
```

### Appendix A

From a SageMath environment with access to the LMFDB database, move to the
Appendix A directory:

```bash
cd appendix-a
```

Run:

```bash
sage ecnf_cmtype_not1_graph_types_clean.sage
```

If the program provides separate online and offline modes, the exact commands
are documented in `appendix-a/README.md`.

## Input and output conventions

Each computational README describes the exact data formats used by the
corresponding programs.

In particular, the documentation records:

- how matrix groups and their generators are represented;
- how graph vertices are numbered or labeled;
- how the distinguished vertex is represented;
- how edge labels are obtained from isogeny matrices;
- how LMFDB curve and number-field labels are stored;
- which database filters are applied;
- which files are generated;
- which output corresponds to each theorem, table, or appendix; and
- whether a computation requires database access.

An edge labeled by a prime $p$ represents a $K$-rational isogeny of degree
$p$.

## Data directories

### Section-specific data

Inputs and outputs specific to a computation are stored inside the
corresponding section or appendix.

For example:

```text
section-9/input/
section-9/output/
section-10/output/
appendix-a/data/
appendix-a/figures/
appendix-a/output/
```

### Shared data

The top-level `data/` directory is reserved for data shared by more than one
part of the repository.

In particular:

```text
data/genus_zero_models/
```

may contain machine-readable versions of the models and parametrizations
associated with the genus-zero modular curves and the families appearing in
Appendix B.

Every data file should be accompanied by documentation recording:

- the script that generated it;
- the command used;
- the software version;
- the meaning of each field;
- the corresponding result in the paper;
- whether it is input or generated output; and
- whether external database access was required.

## Appendix A data provenance

The data in `appendix-a/` are derived from LMFDB records for elliptic curves
over number fields.

The reproducibility metadata should record:

```text
Query date: [TO BE ADDED]
SageMath version: [TO BE ADDED]
LMFDB commit: [TO BE ADDED]
Database collection: ec_nfcurves
Filters: number = 1, cm_type != 1
Number of selected isogeny classes: [TO BE ADDED]
Number of graph types: [TO BE ADDED]
```

Since the LMFDB is updated over time, the result of a new query may differ
from the saved classification. The data included with a repository release
should therefore be regarded as a snapshot of the derived classification at
the recorded query date.

The repository should contain only the derived data needed to reproduce the
classification, figures, and report. It should not contain a complete copy of
the LMFDB database.

When possible, the offline classification should be stored in both:

- a SageMath-native format, such as `.sobj`; and
- a human-readable and software-independent format, such as JSON.

For example:

```text
appendix-a/data/graph_types.sobj
appendix-a/data/graph_types.json
```

## Reproducibility

For every main computation, the README in the corresponding directory
records:

1. the result of the paper being verified or illustrated;
2. the mathematical or database input;
3. the machine-readable input format;
4. the command used to run the computation;
5. the expected output;
6. the version of SageMath or Magma used;
7. the external dependencies;
8. the expected running time, when relevant;
9. whether database access is required;
10. the date of the database query, when relevant; and
11. any manual post-processing required to obtain a displayed model, graph,
    or figure.

Outputs that form part of the paper are stored either in the corresponding
`output/` directory or under `data/`.

Temporary files, caches, compiled SageMath files, and local installation
paths are not included in the repository.

## Mathematical conventions

Throughout the code and documentation:

- $K$ denotes a field of characteristic zero;
- $\overline{K}$ denotes an algebraic closure of $K$;
- $G_K=\mathrm{Gal}(\overline{K}/K)$ denotes the absolute Galois group of
  $K$;
- $E/K$ denotes an elliptic curve;
- $\mathcal{G}(E/K)$ denotes its isogeny graph;
- $\mathcal{G}_p(E/K)$ denotes its $p$-primary isogeny graph;
- $\rho_{E,n}$ denotes the mod-$n$ Galois representation;
- $\rho_{E,p^\infty}$ denotes the $p$-adic Galois representation;
- $\rho_E$ denotes the adelic Galois representation; and
- $X_H$ denotes the modular curve associated with a subgroup
  $H\leq\mathrm{GL}_2(\widehat{\mathbb{Z}})$.

The notation $\mathbb{Z}$, $\mathbb{Q}$, $\mathbb{Z}_p$, and
$\widehat{\mathbb{Z}}$ is used throughout the Markdown documentation.

Names of groups and algebraic objects are written using `\mathrm`, for
example:

```text
\mathrm{End}
\mathrm{GL}
\mathrm{Gal}
```

Further information about notation can be placed in `docs/notation.md`.

## Versioning

The repository is intended to provide a reproducible computational companion
to the paper.

Each release should state the version of the paper to which it corresponds.
For example:

```text
Repository release v1.0.0 corresponds to arXiv:2608.02494v1.
```

The documentation should be updated whenever:

- the numbering of the results in the paper changes;
- the input or output format of a program changes;
- a new database query is performed;
- the saved LMFDB classification is regenerated; or
- the external `Modular` dependency is updated.

For long-term preservation, stable releases may be archived in Zenodo. If a
Zenodo archive is created, its DOI should be added here and to
`CITATION.cff`.

```text
Software DOI: [TO BE ADDED]
```

## Citation

If you use this code or the accompanying data in your research, please cite
the paper:

```bibtex
@article{BarriosGonzalezJimenezNovak2026,
  author        = {Barrios, Alexander J. and
                   González-Jiménez, Enrique and
                   Novak, Ivan},
  title         = {Isogeny Graphs of Elliptic Curves in Characteristic Zero},
  year          = {2026},
  eprint        = {2608.02494},
  archivePrefix = {arXiv},
  primaryClass  = {math.NT}
}
```

If a stable version of this repository is archived, please also cite the
corresponding software release:

```bibtex
@software{IsogenyGraphsCode2026,
  author  = {Barrios, Alexander J. and
             González-Jiménez, Enrique and
             Novak, Ivan},
  title   = {Computational Resources for Isogeny Graphs of Elliptic Curves
             in Characteristic Zero},
  year    = {2026},
  version = {1.0.0},
  doi     = {[TO BE ADDED]},
  url     = {https://github.com/enrique-gonzalez-jimenez/isogeny-graphs}
}
```

GitHub citation metadata are provided in `CITATION.cff`.

## External software, databases, and acknowledgements

The computations in Section 9 make use of:

> David Zywina, `Modular`: Magma code for computing modular forms and models
> of modular curves.  
> <https://github.com/davidzywina/Modular>

The `Modular` package is based on the methods and computations described in
reference [95] of the paper.

The computations in Appendix A use data from the LMFDB and its SageMath-based
database infrastructure.

The explicit computations in the paper were carried out using SageMath and
Magma.

External packages and databases are not part of the present repository and
remain subject to their own licenses, terms of use, and citation
requirements.

## License

The original code in this repository is distributed under the terms of the
`LICENSE` file.

```text
License: [TO BE ADDED]
```

The accompanying paper, external software, LMFDB data, and third-party
components may be subject to separate licensing terms.

In particular:

- David Zywina's `Modular` package is governed by the license included in its
  own repository; and
- LMFDB data and software are governed by the licensing and citation
  conditions of the LMFDB project.

## Authors

- **Alexander J. Barrios**
- **Enrique González-Jiménez**
- **Ivan Novak**

For questions about the code or to report a computational issue, please use
the GitHub issue tracker:

<https://github.com/enrique-gonzalez-jimenez/isogeny-graphs/issues>
