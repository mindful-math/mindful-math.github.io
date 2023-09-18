+++
author = "Someone"
title = "representer theorem"
date = "2023-09-14"
description = "tikhonovTacticalTrees"
math = true
+++

Some intuition on regularization in statistical theory.
<!--more-->

## audience
A student with a good grasp of calculus and a really good grasp of linear algebra (or just some functional analysis) can handle this. But why put up with this? Well, we will unpack and provide intuition with examples on the representer theorem. I think it's modular enough for one sitting :).

## result

> **representer theorem**: Suppose $\mathcal{H}$ is a reproducible kernel Hilbert space with a reproducing kernel $K:X\times X\rightarrow \mathbb{R}$ ($X$ represents the space where samples $x_1,\dots,x_n$ are drawn from). Then 
$$ \mathrm{argmin}\_{f(\cdot)\in\mathcal{H}}\left[  \frac{1}{n}\sum\limits_{i=1}^{n} \mathcal{L}(f(x\_{i}), y\_{i}) + \lambda\lVert f\rVert\_{\mathcal{H}}^2\right] = \sum\limits_{i=1}^{n} \alpha_i K(\cdot, x_i).$$

Ew what - just calculus and linear algebra my @s$ - close... WAIT STAY! It's actually intuitive and I'll unpack this terse, cryptic (for non-math inclined folk) theorem below.

## building intuition

Let's build intuition with a Q&A session I did myself when I first saw this.

> Q1: WTH is a reproducible kernel Hilbert space?

Break it down word by word:

**Hilbert space**: A Banach space equipped with an inner product. 

> Q1a: What's a Banach space?

It's a complete normed space. 

> Q1a1: What do you mean by completeness?

By definition, a metric space $(X, d)$ is complete iff every Cauchy/fundamental sequence converges to an element in $X$. A Cauchy sequence is a sequence of points in $X$, $\{x_1,x_2,\dots\}$, such that for any $\epsilon > 0$, there exists an $N(\epsilon)$ such that for all $n,m\geq N(\epsilon)$, we have 

$$ d(x_m,x_n)<\epsilon.$$

To be completely candid, this is a fancy way of saying we **want the space to not have holes**. Here's an example: let $X=(0,1]$ and

$$ x_n=\frac{1}{n},\qquad n\geq 1$$

so $x_n$ *should* converge to zero right - easy?? Uh, no sir - problemo 있어: $0\notin X$. 

This is important in ML because we want **optimal models to exist in the space we're searching**! It's a technical condition because we're 99\% of the time working with some nice real space.

> Q1a2: What do you mean by a normed space?

A normed space $X$ is a space where "length" is well-defined for each element. Formally, a space $X$ is said to be normed if for every $x\in X$, we have a non-negative number $\lVert x\rVert$, the norm of $x$, which satisfies three properties:

1. $\lVert x\rVert = 0$ iff $x=0$
2. $\lVert \alpha x\rVert = |\alpha |\lVert x\rVert$ for $\alpha\in\mathbb{F}$ (usually our field is just $\mathbb{R}$)
3. $\lVert x + y\rVert\leq \lVert x\rVert + \lVert y\rVert$

Notice that we can define a metric (or distance) between any two $x,y\in X$ by $d(x,y)=\lVert x - y\rVert$. And so, a normed space can always be made into a metric space.

> Q1b: What's an inner product?

An inner product is a function that takes two elements in a space $X$ and outputs a single number ($X\times X\rightarrow \mathbb{R}$). 

For applied folk, the prime example of a inner product is the dot product from linear algebra. The dot product is awesome because:

 1. You get a sense of the **angle** **between** any two **vectors**: $$ \langle a, b\rangle = a\cdot b = \lVert a \rVert \lVert b\rVert\cos(\theta)$$
 2. You get a sense of the **length of vectors** - in the above, $a\cdot a=\lVert a\rVert_2^2$. The inner product of a vector with itself gives us the squared norm/length.
 3. And in general, we get a sense of the **geometry** of the **space**.

> Q2: Okay okay... so a Hilbert space in practice is more or less a vector space over some nice field like $\mathbb{R}$ where we have the norm to help us measure lengths. Then what is the pretentious sounding **Reproducing Kernel** Hilbert space?

That sesquipedalian name 




https://www.mit.edu/~9.520/scribe-notes/cl7.pdf

https://www.mit.edu/~9.520/scribe-notes/cl5.pdf

https://people.eecs.berkeley.edu/~bartlett/courses/281b-sp08/7.pdf





