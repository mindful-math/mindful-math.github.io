+++
author = "Someone"
title = "metrics"
date = "2024-01-05"
description = "limitingLimitsLore"
math = true
+++

A bad and good definition of a metric space. 
<!--more-->

- [definitions](#definitions)
- [thoughts](#thoughts)
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


## thoughts

Rudin's[^1] definition is not modular and too cryptic. I think Kolmogorov was on a better path - first define a metric and then introduce a metric space as a tuple of a set and its metric. Taking inspiration from Knuth and Halmos, I also think Rudin's definition should be fleshed out with more english - it's an exposition of analysis, not a wikipedia entry...

## references

[^1]: [Rudin's "Principles of Mathematical Analysis"](https://archive.org/details/principlesofmath0000walt)
[^2]: [Kolmogorov and Fomin's "Elements of the Theory of Functions and Functional Analysis"](https://archive.org/details/elementsoftheory0000kolm_l7l2)
[^3]: [Haaser and Sullivan's "Real Analysis"](https://archive.org/details/realanalysis0000haas)

