+++
author = "Someone"
title = "ols and gradient descent"
date = "2023-09-7"
description = "interestingInterrelatedIdeas"
math = true
+++

An algebraic relation between gradient descent and OLS.
<!--more-->

## audience
This is written towards someone who has taken a first course in statistics alongside a first course in linear algebra. A first course in time series or dynamical systems would enhance your takeaway as well. The main takeaway is that:
> Gradient descent applied to the squared loss for a linear model converges to the OLS solution **if** we choose a small enough step size.

## setup
An engineer observes noisy observations of a linear model, 

$$ y=Xw^* + \varepsilon ,$$ 

where $X\in\mathbb{R}^{n\times n}$ represents the data matrix (I'm assuming the number of features equals the number of data points for simplicity), $w^\*\in\mathbb{R}^{n} $ represents the true weight vector, and $\varepsilon \in \mathbb{R}^n$ represents some noise. Here is an example dataset we may get where $\varepsilon$ is Gumbel with mode -1 and scale 10.

![Gumbel Errors](/exampleData.png)

Suppose $X$ is **ill-conditioned**, i.e. its condition number $\lambda_{\max}/\lambda_{\min}\gg 1$, then $\hat{w} =X^{-1}y $ **is not** a good approximation of $w^\*$ and in fact $\lVert \hat{w}-w^\*\rVert_{2}$ is huge! Wait... what... why? Well,

$$ \lVert \hat{w}  - w^\*\rVert_{2} = \lVert X^{-1}y - w^\* \rVert_{2} = \lVert X^{-1}(Xw^\* + \varepsilon) - w^\*\rVert_{2}=\lVert X^{-1}\varepsilon \rVert_{2}\leq \frac{1}{\lambda_{\min}}\lVert \varepsilon\*\rVert_2.$$

So more or less if $\lambda_{\min}$ is super tiny or our error, $\varepsilon$, is high, then this is a pretty lousy estimate for $w^\*$. What can the engineer do instead? 

<center> G->r->a->d->i->e->n->t D->e->s->c->e->n->t. </center>


To optimize anything, the engineer has to first pick a candidate loss function. The squared L2 norm is a great start:

$$ \mathcal{L}(w) = \lVert y-Xw\rVert_{2}^{2}.$$





$$ w_{k+1} \leftarrow w_{k} + \eta X^{\intercal}(y - Xw_{k}) $$

where $\eta$ represents the learning rate and is sufficiently small. Show that for $k>0$, we have
$$ \lVert w_{k} \rVert_{2} \leq \lVert w_{k-1} \rVert_{2} + \eta \lambda_{\max} \lVert y \rVert_{2}.$$

Okay boss. Let's rearrange the gradient descent update first: 

$$ w_{k+1} \leftarrow w_{k} + \eta X^{\intercal}(y - Xw_{k}) = (I_n - \eta X^{\intercal}X)w_{k} + \eta X^{\intercal}y.$$

Notice that $X^{\intercal} X$ is positive semi-definite (PSD) since $w^{\intercal} X^\intercal X w= \lVert Xw\rVert_{2}^{2}\geq 0$ for all $w\in\mathbb{R}^{n}$. By spectral theorem, we can diagonalize this so 

$$X^\intercal X = PDP^{\intercal}.$$

In the above, $P$ denotes the orthonormal matrix of eigenvectors, $v_{1},\dots, v_{n}$, and $D=\mathrm{diag}(\lambda_1,\dots,\lambda_n)$. Thus we can rewrite $I_n - \eta X^{\intercal}X$ as 

\begin{align}
   I_n - \eta X^{\intercal}X &= I_n - \eta PDP^{\intercal} \\\\
   &= P(I-\eta D)P^{\intercal}.
\end{align}

The second equality follows again since $P^{\intercal}P=I$. From this, we can iteratively expand the gradient descent update:

\begin{align}
   w_{k} &= P(I-\eta D)P^{\intercal} w_{k-1} + \eta X^{\intercal}y \\\\
   &= P(I-\eta D)P^{\intercal} \left[ P(I-\eta D)P^{\intercal} w_{k-2} + \eta X^{\intercal}y \right] + \eta X^{\intercal}y \\\\
   & \vdots \\\\
   &= P(I-\eta D)^{k}P^{\intercal} w_{0} + \sum\limits_{i=0}^{k-1} P(I - \eta D)^{i}P^{\intercal} \times \eta X^{\intercal}y \\\\\
   &= \sum\limits_{j=1}^{n} (1-\eta\lambda_{j})^{k} v_{j}v_{j}^{\intercal}w_{0} + \sum\limits_{i=0}^{k-1} \sum\limits_{j=1}^{n} (1-\eta\lambda_{j})^{i}v_{j}v_{j}^{\intercal} \times \eta X^{\intercal}y \\\\
   &= \sum\limits_{i=0}^{k-1} \sum\limits_{j=1}^{n} (1-\eta\lambda_{j})^{i}v_{j}v_{j}^{\intercal} \times \eta X^{\intercal}y \\\\
   &= \sum\limits_{j=1}^{n} \sum\limits_{i=0}^{k-1} (1-\eta\lambda_{j})^{i}v_{j}v_{j}^{\intercal} \times \eta X^{\intercal}y \\\\
   &= \sum\limits_{j=1}^{n} v_{j}v_{j}^{\intercal}\frac{1-(1-\eta\lambda_{j})^{k}}{1-(1-\eta\lambda_{j})} \times \eta X^{\intercal}y \\\\
   &= \sum\limits_{j=1}^{n} \frac{1}{\lambda_{j}} v_{j}v_{j}^{\intercal}\left(1-(1-\eta\lambda_{j})^{k}\right) \times X^{\intercal}y
\end{align}

Now what about the asymptotic behavior of this sequence? 

$$
w_{k} \xrightarrow{ k \to \infty} 
\begin{cases} 
(X^{\intercal}X)^{-1}X^{\intercal}y & \eta\in(0,\frac{2}{\lambda_{\max}}) \\\\
\infty & \text{otherwise}.
\end{cases}
$$

So we've shown that with a carefully chosen step size, we arrive at the OLS solution with gradient descent. So to be honest, I got sidetracked from the result Sahai wants here and just did my own thing. Sahai's question really just needs (3), $|1-\eta\lambda_{i}|\le 1$ for all $i$ provided $\eta\in(0,\frac{2}{\lambda_{\max}})$, Cauchy-Schwarz, and the triangle inequality:

\begin{align}
\lVert w_{k} \rVert_{2} &= \lVert (I_n - \eta X^{\intercal}X)w_{k-1} + \eta X^{\intercal}y\rVert_{2} \\\\
&\le \lVert (I_n - \eta X^{\intercal}X)w_{k-1}\rVert_{2} + \lVert \eta X^{\intercal}y \rVert_{2} \\\\
&\le \lVert w_{k-1} \rVert_{2} + \eta\lambda_{\max}\lVert y\rVert_{2}
\end{align}