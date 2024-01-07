+++
author = "Someone"
title = "notices"
date = "2023-12-29"
description = "januaryNotices"
math = true
+++

Takeaways from AMS's January edition of the [Notices](https://www.ams.org/journals/notices/202401/202401FullIssue.pdf?cat=fullissue&trk=fullissue202401).
<!--more-->

- [new](#new)
- [review](#review)
- [research](#research)

## new

- The [LMFDB](https://www.lmfdb.org/) (L-functions and Modular Forms Database) contains some interesting applets and calculators. The research is so left-field from what I know, so I don't know how useful this is for me.
- [The Stacks Project](https://stacks.math.columbia.edu/) is something I will probably never touch for algebraic geometry - I found the site awkward to navigate.
- Laplace-Beltrami Operator (where $g$ denotes the determinant of the metric $g$ written in local coordinates):

$$ \mathrm{div } \nabla,\qquad \frac{1}{\sqrt{\det g}} \partial_{x_i}\left( \sqrt{\det g} g_{ij} \partial_{x_j} \right)$$

- The Levi-Civita connection - an operator that allows us to differentiate vector fields on a manifold (didn't get this far in calculus lol)
- The Hodge Laplacian (I remember 1-forms faintly, but not this guy):

$$ -(d d^* + d^*d)\alpha,\qquad \alpha= v^b $$

- What are musical isomorphisms that move between vector fields and 1-forms(!!)? 
- Deformation tensors:

$$ (\mathrm{Def } v)_{ij} = \frac{1}{2}\left( \nabla_i v_j + \nabla_j v_i \right) $$

- Stochastic Action Principle and Lagrangian Paths (see Arnaudan and Cruzeiro for more info)
- Iwasawa theory: "the backbone of number theory"
- The fractional Laplacian:

$$ (-\Delta)^s f(x) = C_{n,s}\int\limits_{\mathbb{R}^n} \frac{f(x) - f(\xi)}{|x-\xi|^{n+2s}}\;d\xi $$

- Hodge theory of matroids (cough June Huh cough)


## review

- Incompressible Navier-Stokes equation (I don't even remember the motivation for this equation):

$$ \partial_t u - \Delta u + u\cdot \nabla u + \nabla p = 0,\qquad \mathrm{div } u = 0 $$

- Utility of the Laplacian operator:

$$ \Delta f(x_1,\dots,x_n) = \sum\limits_{i=1}^n \left(\frac{\partial f}{\partial x_i}\right)^2$$

- Ricci operators
- Hyperbolic planes: $\mathbb{H}_2$

## research

- Computer proof verification wired up in math undergraduate proof courses akin to OK software used at Berkeley in CS61A
  - Software has taken off because the feedback loop is much shorter than in mathematics (math requires an "expert" to verify your proof - this is bs and not scalable)
  - The issue is that this formal logic is in its early stages of development and there are startup costs to learning verbose and ugly languages like TLA+ or Lean
  - There are human-readable proofs and are machine-readable proofs; in CS, these already exist - the human-readable proofs are algorithms and the machine-readable proofs is the code attached to the paper
- MRC 2024 Week 2 (interpretable ML) or 3 (climate science); sign up before February 15th, 2024
