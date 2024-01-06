+++
author = "Someone"
title = "metrics"
date = "2024-01-05"
description = "limitingLimitsLore"
math = true
+++

A review of Rudin's terrible definition of a metric space. 
<!--more-->

- [definitions](#definitions)
- [critique](#critique)
- [references](#references)

## definitions

<hr style="border:1.5px solid black">

> **[^1]**: A set $X$, whose elements we shall call points, is said to be a metric space if with any two points $p$ and $q$ of $X$, there is associated a real number $d(p,q)$, called the distance from $p$ to $q$, such that
> 
> (a) $d(p,q)>0$ if $p\geq q$; $d(p,p)=0$;
> 
> (b) $d(p,q)=d(q,p)$;
> 
> (c) $d(p,q)\leq d(p,r) + d(r,q)$, for any $r\in X$.
> 
> Any function with these three properties is called a distance function, or a metric.

<hr style="border:1.5px solid black">

> **[^2]**: A metric space is the pair of two things: a set $X$, whose elements are called points, and a distance, i.e. a single-valued, nonnegative, real function $\rho(x,y)$, defined for arbitrary $x$ and $y$ in $X$ and satisfying the following conditions:
>
> 1) $\rho(x,y)=0$ if and only if $x=y$,
>
> 2) (axiom of symmetry) $\rho(x,y)=\rho(y,x)$,
>
> 3) (triangle axiom) $\rho(x,y)+\rho(y,z)\geq \rho(x,z)$.
>
> The metric space itself, i.e. the pair $X$ and $\rho$, will usually be denoted by $R=(X,\rho)$.


## critique

First thought - how is [^1] the most popular book for a first course in analysis? The issue (maybe speaking from too much time doing software) is that it is not modular nor expository. There should first be a definition of a metric (a tool for measuring and defining the geometry on a set). Then afterwards, the following one-liner would define a metric space.

> A metric space is a tuple consisting of a set and a metric whose domain is that set.

Rudin's second chapter (and this definition) also suffer from a lack of examples - [^2], [^3], and even Terrance Tao's analysis book provide a lot of examples and non-examples of metrics and metric spaces. 

Along the lines of Halmos and Knuth, I think that mathematical expository writing should use as much english language as possible rather than symbolic manipulation in the presentation of such fundamental concepts.

## references

[^1]: [Rudin's "Principles of Mathematical Analysis"](https://archive.org/details/principlesofmath0000walt)
[^2]: [Kolmogorov and Fomin's "Elements of the Theory of Functions and Functional Analysis"](https://archive.org/details/elementsoftheory0000kolm_l7l2)
[^3]: [Haaser and Sullivan's "Real Analysis"](https://archive.org/details/realanalysis0000haas)

