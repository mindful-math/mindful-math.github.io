+++
author = "Someone"
title = "notices"
date = "2024-01-19"
description = "februaryNotices"
math = true
+++

Takeaways from AMS's February edition of the [Notices](https://www.ams.org/journals/notices/202402/202402FullIssue.pdf?cat=fullissue&trk=fullissue202402).
<!--more-->

- [new](#new)
- [review](#review)
- [research](#research)
- [references](#references)

## new

- The Isbell adjunction: $F^*: \text{Set}^{C^{op}} \leftrightarrows (\text{Set}^D)^{op}: F_*$
- The nuclei of $f$ are objects fixed up to isomorphism under the composite functors $F^*F_*$ and $F_*F^*$ (analogous to left and right singular vectors of matrices)
- Factorizing a tesnor in the tensor product of vector spaces $V_1\otimes V_2\otimes\cdots\otimes V_n$ into what is called a **tensor train/matrix product state** can be interpreted as a sequence of $n-1$ compatible truncated SVDs
- Enriched category theory; a version of category theory when the set $C(x,y)$ of morphisms between two objects is no longer a set (it couuld be a partially ordered set, an Abelian group, or a topological space)
- Homotopical Combinatorics in entirety is new to me. It studies "combinatorial structures encoding aspects of equivariant homotopy theory, equivariant algebra, and abstract homotopy theory".
- [Zero forcing](https://arxiv.org/pdf/2204.01810.pdf) sounds a lot like the study of cellular automata
- [Category Theory for AI](https://cats.for.ai/) is just a plea to use more algebraic tools to describe and compose AI models
- Disjuct matrices (another word for matrices with binary entries)
- [Iterative hard thresholding](https://arxiv.org/pdf/0805.0510.pdf), [orthogonal matching pursuit](https://www.di.ens.fr/~mallat/papiers/MallatPursuit93.pdf), and [compressive sampling matching pursuit](https://www.sciencedirect.com/science/article/pii/S1063520308000638) are three popular algorithms aimed at finding sparse decompositions. The last algorithm's paper read the most smoothly for me (someone who does not know much about compression)
- Quantum control theory
- I like this idea: "When considering a mathematical object $X$ that has little or incomplete structure, one can replace $X$ by something like 'functions on $X$' which will have considerably more structure than $X$... The first example that comes to mind is $k^X$, the set of functions on a set $X$ valued in a field $k$, which forms a vector space..."
- In that article, they also have the fun description of a DNN:
$$ f:\mathbb{R}^{n} \xrightarrow{f_1} \mathbb{R}^{n_1}\cdots \xrightarrow{f_K} \mathbb{R}^{n_K} \xrightarrow{g} \mathbb{R}^m $$
where $f_i(x)=\sigma(M_i x + b_i)$ and $\sigma$ is a real-valued "activation" function.


## review

- Grpah theory in general; I need to review syntax and generate many examples for each one
- Integer linear programs (ILP) & Boolean satisfiability problems (SAT) are starting to fade from memory
- Electrical power networks and graph representations (as an example to follow through)
- Restricted Isometry Property (RIP): 
  $$(1-\delta_k)\lVert x \rVert_{p}^{p} \leq \lVert Ax \rVert_{p}^{p}\leq (1+\delta_k)\lVert x \rVert_{p}^{p}$$
- Non-negative least absolute deviation (like LASSO but unconstrained): 
  $$\hat{x} = \arg\min_{z\geq 0} \lVert Az-y \rVert_{1}$$
- Both [^1] and [^2] give an overview of compressed sensing - even Terrance Tao has worked on this problem.
- Posets
- Meet-semilattices
- Profunctors; a set-valued functor $f: C^{\text{op}}\times D\rightarrow \text{Set}.$
- Currying; I assume the authors are describing composition - "By simple currying, $m$ defines functions $X\rightarrow k^Y$ and $Y\rightarrow k^X$ defined by $x\mapsto m(x,-)$ and $y\mapsto m(-,y)$".


## research

- I would like to know how often the assumption that the measurement matrix $A$ is "an information-preserving projection or a bi-Lipschitz linear metric space embedding of all $k$-sparse vectors into $\mathbb{R}^m$" where it is information preserving so long as it satisfies the restricted isometry property and the nullspace property. This sounds like total BS... you cannot get sparse, linear, and information preserving with test data... Come on now - they should at least explain that the solution rapidly destabilizes if these conditions are not met and you're left with inconclusive evidence of what the signal is.
- Are there equivalent formulations of zero-forcing? Can we setup some kind of recursive scheme or is this similar to backpropagation? It feels very related to many differently named objects in different fields.
  

## references

[^1]: [Donoho's "Compressed Sensing"](https://www.cmor-faculty.rice.edu/~yzhang/caam699/Image%20papers/CompSensing.pdf)
[^2]: [Davenport's "Fundamentals of Compressive Sensing"](https://www.cmor-faculty.rice.edu/~yzhang/caam699/Image%20papers/CompSensing.pdf)
