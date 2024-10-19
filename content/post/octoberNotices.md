+++
author = "Someone"
title = "notices"
date = "2024-10-19"
description = "notices"
math = true
+++

Takeaways from AMS's October edition of the [Notices](https://www.ams.org/journals/notices/202410/202410FullIssue.pdf?cat=fullissue&trk=fullissue202410).

<!--more-->

- [new](#new)
- [review](#review)
- [research](#research)

## new

- The quintic threefold (what does the term threefold mean)
$$ z_1^5 + z_2^5 + \cdots + z_5^5 = 0$$
- The moduli space of stable maps $M_{g,n}(X,\beta)$ is a set consisting of (isomorphic classes of) tuples of nodal curves of arithmetic genus $g$, $n$ distinct, non-nodal points on the curve, a morphism $f: C\rightarrow X$ where $f_*[C]=\beta$, and the tuples have finitely many automorphisms.
- Intersection theory - I think some subset of algebraic geometry that studies intersections within some ambient variety
- $\mathbb{R}\mathbb{P}^2$ (a compact ambient variety - is this just tongue in cheek for something isomorphic to $\mathbb{C}^n$)
- Smooth projective varieties, homology classes, Deligne Mumford stacks, stable maps, ... got lost early :)
- R-nets: subsets of vertices on a graph such that for all vertices in the R-net, there exists another vertex at most $R$ distance away (distance could change if we consider weighted graphs)
- Dowling Wilson Conjecture (bounds on number of lines that can be drawn through $n$ points more or less if we ignore linear algebra)

## review
- Equiangular lines - i.e. take $n$ lines and pick any two - if these are isomorphic angle-wise. Yufei Zhao considers the scaling limit of the max number of such lines divided by the dimension $d$. I love problems that don't hinge on lots of definition depth (cough first article cough)
- Gram matrices, Cholesky decomposition, Ramsey's theorem (something about a bound on colorings of a graph)
- Coq/Lean; any reason not to try making a simpler interface in Python/Java - the language is funky which is a huge lim fac...

## research
- I wonder if curve counting and deformation invariant studies has been connected with geometric deep learning and ML generally speaking. It reminds me a lot of robust structural optimization like

$$ \min\limits_{\beta}\lVert y-X((1+\delta)I)\beta\rVert_2^2,\qquad |\delta|\leq \epsilon$$

- Pair proving w/ Terrance Tao; sign me up to fix a bug in his proofs :)
