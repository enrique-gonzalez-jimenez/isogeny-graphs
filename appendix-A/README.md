# Appendix A: An LMFDB Zoo of Isogeny Graphs

This directory contains the SageMath code and derived data used to produce Appendix A of the paper

> Alexander J. Barrios, Enrique Gonzalez-Jimenez, and Ivan Novak,  
> *Isogeny graphs of elliptic curves in characteristic zero*,  
> arXiv:2608.02494 (2026).

- **Paper:** https://arxiv.org/abs/2608.02494
- **Repository:** https://github.com/enrique-gonzalez-jimenez/isogeny-graphs
- **LMFDB:** <https://www.lmfdb.org/>
  
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
## Main file

```text
lmfdb_isogeny_lmfdb_zoo.sage
```

The program is written for SageMath and uses the LMFDB database
infrastructure.

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

## Table 9: A small zoo of isogeny configurations

The following table reproduces Table 9 of the paper. It gives one elliptic
curve for every isogeny graph type appearing in the LMFDB.

The columns have the following meanings:

- **Isogeny label:** label of the edge-weighted isogeny graph;
- **Size:** number of vertices in the graph, equivalently the number of $K$-isomorphism classes in the isogeny class;
- **Degree:** isogeny class degree;
- **LMFDB label:** an example elliptic curve realizing the graph. It is a direct link to the corresponding elliptic curve.


| isogeny label | size | degree | LMFDB label |
|---|---:|---:|---:|
| `1.0` | 1 | 1 | [`37.a`](https://www.lmfdb.org/EllipticCurve/Q/37/a/) |
| `2.0` | 2 | 2 | [`46.a`](https://www.lmfdb.org/EllipticCurve/Q/46/a/) |
| `3.0` | 2 | 3 | [`44.a`](https://www.lmfdb.org/EllipticCurve/Q/44/a/) |
| `5.0` | 2 | 5 | [`38.b`](https://www.lmfdb.org/EllipticCurve/Q/38/b/) |
| `7.0` | 2 | 7 | [`26.b`](https://www.lmfdb.org/EllipticCurve/Q/26/b/) |
| `11.0` | 2 | 11 | [`121.a`](https://www.lmfdb.org/EllipticCurve/Q/121/a/) |
| `13.0` | 2 | 13 | [`147.b`](https://www.lmfdb.org/EllipticCurve/Q/147/b/) |
| `17.0` | 2 | 17 | [`14450.b`](https://www.lmfdb.org/EllipticCurve/Q/14450/b/) |
| `19.0` | 2 | 19 | [`361.a`](https://www.lmfdb.org/EllipticCurve/Q/361/a/) |
| `23.0` | 2 | 23 | [`2.2.265.1-9.2-a`](https://www.lmfdb.org/EllipticCurve/2.2.265.1/9.2/a/) |
| `29.0` | 2 | 29 | [`2.0.631.1-32.2-b`](https://www.lmfdb.org/EllipticCurve/2.0.631.1/32.2/b/) |
| `31.0` | 2 | 31 | [`2.0.447.1-32.2-b`](https://www.lmfdb.org/EllipticCurve/2.0.447.1/32.2/b/) |
| `37.0` | 2 | 37 | [`1225.b`](https://www.lmfdb.org/EllipticCurve/Q/1225/b/) |
| `41.0` | 2 | 41 | [`2.0.359.1-32.2-a`](https://www.lmfdb.org/EllipticCurve/2.0.359.1/32.2/a/) |
| `43.0` | 2 | 43 | [`1849.b`](https://www.lmfdb.org/EllipticCurve/Q/1849/b/) |
| `67.0` | 2 | 67 | [`4489.b`](https://www.lmfdb.org/EllipticCurve/Q/4489/b/) |
| `73.0` | 2 | 73 | [`2.0.31.1-2450.16-g`](https://www.lmfdb.org/EllipticCurve/2.0.31.1/2450.16/g/) |
| `163.0` | 2 | 163 | [`26569.a`](https://www.lmfdb.org/EllipticCurve/Q/26569/a/) |
| `9.0` | 3 | 9 | [`19.a`](https://www.lmfdb.org/EllipticCurve/Q/19/a/) |
| `25.0` | 3 | 25 | [`11.a`](https://www.lmfdb.org/EllipticCurve/Q/11/a/) |
| `49.0` | 3 | 49 | [`2.0.11.1-9153.2-a`](https://www.lmfdb.org/EllipticCurve/2.0.11.1/9153.2/a/) |
| `4.1` | 4 | 4 | [`17.a`](https://www.lmfdb.org/EllipticCurve/Q/17/a/) |
| `2.0-3.0` | 4 | 6 | [`20.a`](https://www.lmfdb.org/EllipticCurve/Q/20/a/) |
| `2.0-5.0` | 4 | 10 | [`66.c`](https://www.lmfdb.org/EllipticCurve/Q/66/c/) |
| `2.0-7.0` | 4 | 14 | [`49.a`](https://www.lmfdb.org/EllipticCurve/Q/49/a/) |
| `3.0-5.0` | 4 | 15 | [`50.a`](https://www.lmfdb.org/EllipticCurve/Q/50/a/) |
| `3.0-7.0` | 4 | 21 | [`162.b`](https://www.lmfdb.org/EllipticCurve/Q/162/b/) |
| `2.0-11.0` | 4 | 22 | [`2.0.47.1-6.1-a`](https://www.lmfdb.org/EllipticCurve/2.0.47.1/6.1/a/) |
| `2.0-13.0` | 4 | 26 | [`2.0.191.1-32.2-a`](https://www.lmfdb.org/EllipticCurve/2.0.191.1/32.2/a/) |
| `27.0` | 4 | 27 | [`27.a`](https://www.lmfdb.org/EllipticCurve/Q/27/a/) |
| `3.0-11.0` | 4 | 33 | [`2.2.265.1-4.1-a`](https://www.lmfdb.org/EllipticCurve/2.2.265.1/4.1/a/) |
| `2.0-17.0` | 4 | 34 | [`2.0.15.1-800.2-a`](https://www.lmfdb.org/EllipticCurve/2.0.15.1/800.2/a/) |
| `5.0-7.0` | 4 | 35 | [`2.2.5.1-2401.1-b`](https://www.lmfdb.org/EllipticCurve/2.2.5.1/2401.1/b/) |
| `3.0-13.0` | 4 | 39 | [`2.0.7.1-15876.2-e`](https://www.lmfdb.org/EllipticCurve/2.0.7.1/15876.2/e/) |
| `3.0-17.0` | 4 | 51 | [`2.2.17.1-81.1-b`](https://www.lmfdb.org/EllipticCurve/2.2.17.1/81.1/b/) |
| `3.0-19.0` | 4 | 57 | [`2.0.23.1-162.1-a`](https://www.lmfdb.org/EllipticCurve/2.0.23.1/162.1/a/) |
| `3.0-41.0` | 4 | 123 | [`2.2.41.1-81.1-c`](https://www.lmfdb.org/EllipticCurve/2.2.41.1/81.1/c/) |
| `3.0-89.0` | 4 | 267 | [`2.2.89.1-81.1-a`](https://www.lmfdb.org/EllipticCurve/2.2.89.1/81.1/a/) |
| `9.1` | 5 | 9 | [`2.0.3.1-324.1-a`](https://www.lmfdb.org/EllipticCurve/2.0.3.1/324.1/a/) |
| `8.1` | 6 | 8 | [`21.a`](https://www.lmfdb.org/EllipticCurve/Q/21/a/) |
| `2.0-9.0` | 6 | 18 | [`14.a`](https://www.lmfdb.org/EllipticCurve/Q/14/a/) |
| `5.0-9.0` | 6 | 45 | [`2.0.39.1-4.2-a`](https://www.lmfdb.org/EllipticCurve/2.0.39.1/4.2/a/) |
| `2.0-25.0` | 6 | 50 | [`2.0.7.1-5632.18-a`](https://www.lmfdb.org/EllipticCurve/2.0.7.1/5632.18/a/) |
| `3.0-25.0` | 6 | 75 | [`2.2.5.1-2025.1-c`](https://www.lmfdb.org/EllipticCurve/2.2.5.1/2025.1/c/) |
| `9.0-11.0` | 6 | 99 | [`2.2.33.1-1.1-a`](https://www.lmfdb.org/EllipticCurve/2.2.33.1/1.1/a/) |
| `3.0-49.0` | 6 | 147 | [`2.2.21.1-49.1-a`](https://www.lmfdb.org/EllipticCurve/2.2.21.1/49.1/a/) |
| `4.1-3.0` | 8 | 12 | [`30.a`](https://www.lmfdb.org/EllipticCurve/Q/30/a/) |
| `16.1` | 8 | 16 | [`15.a`](https://www.lmfdb.org/EllipticCurve/Q/15/a/) |
| `4.1-5.0` | 8 | 20 | [`2.2.89.1-4.1-b`](https://www.lmfdb.org/EllipticCurve/2.2.89.1/4.1/b/) |
| `4.1-7.0` | 8 | 28 | [`2.2.28.1-1.1-a`](https://www.lmfdb.org/EllipticCurve/2.2.28.1/1.1/a/) |
| `2.0-3.0-5.0` | 8 | 30 | [`2.2.5.1-81.1-a`](https://www.lmfdb.org/EllipticCurve/2.2.5.1/81.1/a/) |
| `2.0-3.0-7.0` | 8 | 42 | [`4.4.1600.1-1.1-a`](https://www.lmfdb.org/EllipticCurve/4.4.1600.1/1.1/a/) |
| `2.0-3.0-11.0` | 8 | 66 | [`4.4.17424.1-1.1-a`](https://www.lmfdb.org/EllipticCurve/4.4.17424.1/1.1/a/) |
| `16.2` | 10 | 16 | [`2.0.4.1-200.2-a`](https://www.lmfdb.org/EllipticCurve/2.0.4.1/200.2/a/) |
| `2.0-9.1` | 10 | 18 | [`2.0.3.1-196.2-a`](https://www.lmfdb.org/EllipticCurve/2.0.3.1/196.2/a/) |
| `32.0` | 10 | 32 | [`2.0.15.1-15.1-a`](https://www.lmfdb.org/EllipticCurve/2.0.15.1/15.1/a/) |
| `8.1-3.0` | 12 | 24 | [`2.2.17.1-4.1-a`](https://www.lmfdb.org/EllipticCurve/2.2.17.1/4.1/a/) |
| `4.1-9.0` | 12 | 36 | [`2.2.33.1-12.1-a`](https://www.lmfdb.org/EllipticCurve/2.2.33.1/12.1/a/) |
| `8.1-5.0` | 12 | 40 | [`4.4.2048.1-1.1-a`](https://www.lmfdb.org/EllipticCurve/4.4.2048.1/1.1/a/) |
| `64.1` | 12 | 64 | [`4.4.3600.1-225.1-c`](https://www.lmfdb.org/EllipticCurve/4.4.3600.1/225.1/c/) |
| `2.0-9.0-5.0` | 12 | 90 | [`4.4.3600.1-1.1-b`](https://www.lmfdb.org/EllipticCurve/4.4.3600.1/1.1/b/) |
| `9.0-5.0-7.0` | 12 | 315 | [`4.4.11025.1-1.1-a`](https://www.lmfdb.org/EllipticCurve/4.4.11025.1/1.1/a/) |
| `16.1-3.0` | 16 | 48 | [`4.4.9248.1-4.2-a`](https://www.lmfdb.org/EllipticCurve/4.4.9248.1/4.2/a/) |
| `4.1-3.0-5.0` | 16 | 60 | [`4.4.3600.1-1.1-a`](https://www.lmfdb.org/EllipticCurve/4.4.3600.1/1.1/a/) |
| `16.1-7.0` | 16 | 112 | [`4.4.12544.1-1.1-a1`](https://www.lmfdb.org/EllipticCurve/4.4.12544.1/1.1/a/) |
| `8.1-9.0` | 18 | 72 | [`4.4.2304.1-1.1-a1`](https://www.lmfdb.org/EllipticCurve/4.4.2304.1/1.1/a/) |
