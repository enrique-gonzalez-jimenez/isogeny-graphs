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

- Section 9: modular curves associated with isogeny graphs;
- Section 10: explicit classification of genus-zero isogeny graphs;
- Appendix A: an LMFDB zoo of isogeny graphs; and
- Appendix B: tables for the explicit classification of genus-zero isogeny
  graphs.


## Correspondence between the paper and the code

The principal correspondence is as follows.

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
