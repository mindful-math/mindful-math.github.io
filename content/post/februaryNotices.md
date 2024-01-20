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


- Homotopical Combinatorics in entirety is new to me...
- [Zero forcing](https://arxiv.org/pdf/2204.01810.pdf) which sounds a lot like the study of cellular automata; read the article again as it was good
- [Category Theory for AI](https://cats.for.ai/) is just a plea to use more algebraic tools to describe and compose AI models; the article in AMS that mentions it, "The Structure of Meaning in Language: Parallel Narratives in Linear Algebra and Category Theory", is worth reading again on linear algebra and embeddings
- Disjuct matrices (another word for matrices with binary entries)
- Checkout [iterative hard thresholding](https://arxiv.org/pdf/0805.0510.pdf)
- Lossless expander graphs



## review

- Restricted Isometry Problem (RIP): 
  $$(1-\delta_k)\lVert x \rVert_{p}^{p} \leq \lVert Ax \rVert_{p}^{p}\leq (1+\delta_k)\lVert x \rVert_{p}^{p}$$
- Non-negative least absolute deviation (like LASSO but unconstrained): 
  $$\hat{x} = \arg\min_{z\geq 0} \lVert Az-y \rVert_{1}$$
- Compressed sensing sounds like linear algebra plus numerical analysis (or dimension reduction or encoder-decoder schemes or information theory or ...). You take a big vector, find some compression (or linear embedding) for the vector, and sometimes you want to reconstruct the original vector. Both [^1] and [^2] give an overview of this.
- Posets
- Meet-semilattices


## research

- Not much...

## references

[^1]: [Donoho's "Compressed Sensing"](https://www.cmor-faculty.rice.edu/~yzhang/caam699/Image%20papers/CompSensing.pdf)
[^2]: [Davenport's "Fundamentals of Compressive Sensing"](https://www.cmor-faculty.rice.edu/~yzhang/caam699/Image%20papers/CompSensing.pdf)
