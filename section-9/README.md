# Section 9: Models of the modular curves $X_0^r(p^k)$

This directory contains the Magma computations used in Section 9 of:

> Alexander J. Barrios, Enrique González-Jiménez, and Ivan Novak,  
> *Isogeny graphs of elliptic curves in characteristic zero*,  
> [arXiv:2608.02494](https://arxiv.org/abs/2608.02494) (2026).

The script constructs the congruence subgroups associated with the isogeny graphs considered in Section 9 and computes models of the corresponding modular curves.

## Files

- [`model_XH.m`](model_XH.m): Magma script that constructs the relevant subgroups of $\mathrm{GL}_2(\mathbb Z/N\mathbb Z)$, creates the associated modular-curve records, and computes models using David Zywina's `Modular` package.
- [`model_XH_output.txt`](model_XH_output.txt): output obtained by running `model_XH.m` with Magma V2.29-1.

## Requirements

The computations were performed with:

- **Magma V2.29-1**;
- David Zywina's [`Modular`](https://github.com/davidzywina/Modular) repository.

Download or clone the `Modular` repository and place the directory `Modular-main` in this folder, so that the following command in `model_XH.m` points to the specification file:

```magma
AttachSpec("Modular-main/Modular.spec");
```

The expected directory structure is therefore:

```text
section-9/
├── Modular-main/
│   ├── Modular.spec
│   └── ...
├── model_XH.m
├── model_XH_output.txt
└── README.md
```

## Running the computation

From within the `section-9` directory, run:

```bash
magma model_XH.m
```

To save the output to a file, run:

```bash
magma model_XH.m > model_XH_output.txt
```

## Description of the code

### `IsogGraphSubgroup(p,k,r)`

For a prime \(p\) and integers \(k,r\) with
```math
0\le r\le \left\lfloor \frac{k}{2}\right\rfloor,
```

this function returns the subgroup of $\mathrm{GL}_2(\mathbb Z/p^k\mathbb Z)$ consisting of the invertible upper-triangular matrices
```math
\begin{pmatrix}a&b\\0&c\end{pmatrix}
\qquad\text{such that}\qquad
c\equiv a\pmod {p^r}.
```

Equivalently, the condition is $v_p(c-a)\ge r$.

### `LiftGroups(G1,G2)`

Given subgroups $G_1\le \mathrm{GL}_2(\mathbb Z/N_1\mathbb Z)$ and $G_2\le \mathrm{GL}_2(\mathbb Z/N_2\mathbb Z)$, this function returns the subgroup of $\mathrm{GL}_2(\mathbb Z/N_1N_2\mathbb Z)$ whose reductions modulo $N_1$ and $N_2$ belong to $G_1$ and $G_2$, respectively. It constructs the full inverse images under the two reduction maps and then intersects them.

### `SubgroupFiberProduct(s1,s2)`

For parameter lists

```magma
s1 := [p1,k1,r1];
s2 := [p2,k2,r2];
```

this function constructs the two groups with `IsogGraphSubgroup` and returns their fiber product by calling `LiftGroups`.

### `OurGroup(seq)`

This auxiliary function interprets an entry of the list `S`:

- a list `[p,k,r]` represents `IsogGraphSubgroup(p,k,r)`;
- a pair `[[p1,k1,r1],[p2,k2,r2]]` represents the corresponding fiber product.

### `ModelXH(G)`

Given a subgroup $G$, this function:

1. creates the modular-curve record with `CreateModularCurveRec`;
2. prints its Cummins--Pauli name, genus, and field of definition;
3. computes weight-2 modular forms and cusp forms;
4. computes a projective model using `FindModelOfXG`;
5. when the genus is 1, converts the plane cubic into an elliptic curve and prints its \(j\)-invariant.

The function returns the modular-curve record.

## Groups and modular curves computed

The script treats the following cases:

| Parameters | Group notation | Cummins--Pauli name | Genus |
|---|---:|---:|---:|
| `[3,2,1]` | $H^1_9$ | `9B0` | 0 |
| `[2,4,2]` | $H^2_{16}$ | `16C0` | 0 |
| `[[2,1,0],[3,2,1]]` | $H^0_2\times H^1_9$ | `18E0` | 0 |
| `[5,2,1]` | $H^1_{25}$ | `25B0` | 0 |
| `[3,3,1]` | $H^1_{27}$ | `27A1` | 1 |
| `[2,5,2]` | $H^2_{32}$ | `32A1` | 1 |
| `[[2,2,1],[3,2,1]]` | $H^1_4\times H^1_9$ | `36C1` | 1 |
| `[7,2,1]` | $H^1_{49}$ | `49A3` | 3 |

Here the product notation indicates the subgroup obtained by imposing the two local conditions simultaneously via `SubgroupFiberProduct`.

## Summary of the output

The computation gives genus-1 models in the following three cases:

- `27A1`: an elliptic curve with \(j=0\);
- `32A1`: an elliptic curve with \(j=1728\);
- `36C1`: an elliptic curve with \(j=0\).

The case `49A3` has genus 3 and is represented by a plane quartic. The complete equations, fields of definition, and Magma output are recorded in [`model_XH_output.txt`](model_XH_output.txt).

