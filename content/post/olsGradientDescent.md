+++
author = "Someone"
title = "ols and gradient descent"
date = "2023-09-7"
description = "interestingInterrelatedIdeas"
math = true
+++

An algebraic relation between gradient descent and OLS.
<!--more-->

- [audience](#audience)
- [setup](#setup)
- [problem](#problem)
- [vector autoregressions tangent](#vector-autoregressions-tangent)

## audience
This is written towards someone who has taken a first course in statistics alongside a first course in linear algebra. A first course in time series or dynamical systems would enhance your takeaway as well. The main takeaway is that:
> Gradient descent applied to the squared loss for a linear model converges to the OLS solution **if** we choose a small enough step size.

## setup
An engineer observes noisy observations of a linear model, 

$$ y=Xw^* + \varepsilon ,$$ 

where $X\in\mathbb{R}^{n\times n}$ represents the data matrix (I'm assuming the number of features equals the number of data points for simplicity), $w^\*\in\mathbb{R}^{n} $ represents the true weight vector, and $\varepsilon \in \mathbb{R}^n$ represents some noise. Here is an example dataset we may get where $\varepsilon$ is Gumbel with mode -1 and scale 10.

![Gumbel Errors](/exampleData.png)

Suppose $X$ is **ill-conditioned**, i.e. its condition number $\lambda_{\max}/\lambda_{\min}\gg 1$, then $\hat{w} =X^{-1}y $ **is not** a good approximation of $w^\*$ and in fact $\lVert \hat{w}-w^\*\rVert_{2}$ is huge! Wait... what... why? Well,

$$ \lVert \hat{w}  - w^\*\rVert_{2} = \lVert X^{-1}y - w^\* \rVert_{2} = \lVert X^{-1}(Xw^\* + \varepsilon) - w^\*\rVert_{2}=\lVert X^{-1}\varepsilon \rVert_{2}\leq \frac{1}{\lambda_{\min}}\lVert \varepsilon\rVert_2.$$

So more or less if $\lambda_{\min}$ is super tiny or our error, $\varepsilon$, is high, then this is a pretty lousy estimate for $w^\*$. What can the engineer do instead? 

<center> G -> r -> a -> d -> i -> e -> n -> t D -> e -> s -> c -> e -> n -> t. </center>


What is gradient descent? Well imagine we are pouring water into a glass like below. 


![Water](/drink.gif)

Because the glass is curved like a cone, the water naturally gravitates down to the bottom of the cup in the center. A fancier way to describe this process is to say that the change in position of the water with respect to time is proportional to the gradient/slope of the cup:

$$ \frac{d X}{dt} \propto -\nabla_X f(X).$$

And if we discretize this, we get that 

$$ X_{k} - X_{k-1} = -\alpha \nabla_{X} f(X)\iff \underbrace{X_{k} = X_{k-1} - \alpha \nabla_{X} f(X)}_{\text{Gradient Descent!}}$$

where $\eta$ controls how big of a step we take at each iteration. In optimization, this is known as the learning rate.

Our engineer wants to transport these water dynamics to help us optimize our weight vector $w$! Like the water cup's curvature, they need a function whose gradients help guide the process towards the minimum. A natural shape to consider is a parabola whose n-dimensional extension is known as a paraboloid. The squared L2 norm accomplishes just that:

$$ \mathcal{L}(w) = \lVert y-Xw\rVert_{2}^{2}=\sum\limits_{i=1}^{n} (y_{i} - (Xw)_{i})^{2}.$$

Graphically, if $w$ is two-dimensional, the loss function looks almost like the glass above!

![loss-function](/lossFunction.png)

Then if we try applying the dynamics to finding the optimal weight vector, we get that

$$ w_{k} \leftarrow w_{k-1} - \eta \underbrace{ X^{\intercal}(Xw_{k-1} - y)}\_{\nabla_{w} \mathcal{L}(w_{k-1}) }.$$

So to be honest, this is where the engineer stops caring about the math, plugs this into Python or C++ and pops out an estimate for $w^*$. But we're just getting started!!

## problem

 > How close does the gradient descent estimate get to the OLS solution?
$$ \hat{w}\_{\text{OLS}}= \mathrm{argmin}\_{ w\in\mathbb{R}^{n}} \lVert y-Xw\rVert_{2}^{2} = (X^{\intercal} X)^{-1}X^{\intercal} y.$$


Okay boss let's do it! First, let's rearrange the gradient descent update: 

$$ w_{k} \leftarrow w_{k-1} + \eta X^{\intercal}(y - Xw_{k-1}) = (I_n - \eta X^{\intercal}X)w_{k-1} + \eta X^{\intercal}y.$$

Notice that $X^{\intercal} X$ is positive semi-definite (PSD) since $w^{\intercal} X^\intercal X w= \lVert Xw\rVert_{2}^{2}\geq 0$ for all $w\in\mathbb{R}^{n}$ (i.e. norms are always non-negative - they're measuring length). By spectral theorem, we can diagonalize this so 

$$X^\intercal X = PDP^{\intercal}.$$

Here, $P$ denotes the orthonormal matrix of eigenvectors, $[v_{1},\dots, v_{n}]$, and $D=\mathrm{diag}(\lambda_1,\dots,\lambda_n)$. Thus we can rewrite $I_n - \eta X^{\intercal}X$ as 

\begin{align}
   I_n - \eta X^{\intercal}X &= I_n - \eta PDP^{\intercal} \\\\
   &= P(I-\eta D)P^{\intercal}.
\end{align}

The second equality follows again since $P^{\intercal}P=I$. From this, we can iteratively expand the gradient descent update:

\begin{align}
   w_{k} &= P(I-\eta D)P^{\intercal} w_{k-1} + \eta X^{\intercal}y \\\\
   &= P(I-\eta D)P^{\intercal} \left[ P(I-\eta D)P^{\intercal} w_{k-2} + \eta X^{\intercal}y \right] + \eta X^{\intercal}y \\\\
   & \vdots \\\\
   &= \underbrace{P(I-\eta D)^{k}P^{\intercal} w\_{0} + \sum\limits\_{i=0}^{k-1} P(I - \eta D)^{i}P^{\intercal} \times \eta X^{\intercal}y}\_{\text{Remember this one - it's cool!!}} \\\\\
   &= \sum\limits_{j=1}^{n} (1-\eta\lambda_{j})^{k} v_{j}v_{j}^{\intercal}w_{0} + \sum\limits_{i=0}^{k-1} \sum\limits_{j=1}^{n} (1-\eta\lambda_{j})^{i}v_{j}v_{j}^{\intercal} \times \eta X^{\intercal}y \\\\
   &= \sum\limits_{i=0}^{k-1} \sum\limits_{j=1}^{n} (1-\eta\lambda_{j})^{i}v_{j}v_{j}^{\intercal} \times \eta X^{\intercal}y \\\\
   &= \sum\limits_{j=1}^{n} \sum\limits_{i=0}^{k-1} (1-\eta\lambda_{j})^{i}v_{j}v_{j}^{\intercal} \times \eta X^{\intercal}y \\\\
   &= \sum\limits_{j=1}^{n} v_{j}v_{j}^{\intercal}\frac{1-(1-\eta\lambda_{j})^{k}}{1-(1-\eta\lambda_{j})} \times \eta X^{\intercal}y \\\\
   &= \sum\limits_{j=1}^{n} \frac{1}{\lambda_{j}} v_{j}v_{j}^{\intercal}\left(1-(1-\eta\lambda_{j})^{k}\right) \times X^{\intercal}y
\end{align}

As $k\rightarrow\infty$, 

$$\left(1-(1-\eta\lambda_{j})^{k}\right)\rightarrow \begin{cases} 1 & |\eta|\leq \frac{2}{\lambda\_{i}} \\\\ \infty & \text{otherwise}. \end{cases}$$

Note that it's $2/\lambda\_{i}$ and not $1/\lambda\_{i}$ because $\left(1-(1-\eta\lambda_{j})^{k}\right)$ will oscillate between negative and positive values but dampen over time for $\eta\in(\frac{1}{\lambda_{i}}, \frac{2}{\lambda_{i}})$. And so ultimately, 

$$
w_{k} \xrightarrow{ k \to \infty} 
\begin{cases} 
(X^{\intercal}X)^{-1}X^{\intercal}y & \eta\in(0,\frac{2}{\lambda_{\max}}) \\\\
\infty & \text{otherwise}
\end{cases}
$$

**because** 

$$
\sum\limits_{j=1}^{n} \frac{1}{\lambda_{j}} v_{j}v_{j}^{\intercal}\left(1-(1-\eta\lambda_{j})^{k}\right) \times X^{\intercal}y\rightarrow \sum\limits_{j=1}^{n} \frac{1}{\lambda_{j}} v_{j}v_{j}^{\intercal}\times X^{\intercal}y=(X^{\intercal}X)^{-1}X^{\intercal}y
$$

> **So we've shown that with a carefully chosen step size, we arrive at the OLS solution with gradient descent!!!**

But you may say why not then just set $\eta$ to be something super tiny so that it's nearly impossible to be greater than $2/\lambda_{\max}$ - well, that guarantees convergence but how many iterations would that require? That requires some more convergence analysis that I'll leave for another notebook :). 

## vector autoregressions tangent

A autoregression is a type of iterative sequence like 

$$ a_{k}\leftarrow \alpha a_{k-1}=\alpha (\alpha a_{k-2})=\alpha(\alpha (\alpha a_{k-3}))=\cdots .$$

It can be recursively expressed as $\alpha^{k}$ times the starting point $a_{0}$. This process is finite for all $k\in\mathbb{N}$ provided $|\alpha|\leq 1$. We can also visualize it below for several $\alpha$. The black and red $\alpha$ are less than one and they are quickly converging to zero whilst the green and blue $\alpha$ are diverging quite quickly.

![autoregressive-graphs](/autoregressive_overlay.gif)

Remember that equation I told you to remember?! No - well, I added it below again anyhow

$$ P(I-\eta D)^{k}P^{\intercal} w\_{0} + \sum\limits\_{i=0}^{k-1} P(I - \eta D)^{i}P^{\intercal} \times \eta X^{\intercal}y.$$

This is a set of $n$ autoregressions packaged up in a vector! Similar to the autoregressions above, the $(1-\eta\lambda_{i})$ for the $i$th equation is what controls whether or not the $i$th sequence converges. 

When we package up a set of $n$ autoregressions, we get a vector autoregression (VAR). A set of $n$ autogressions gives us the easiest example of a vector autoregression, but we can also consider cases where the matrix is not diagonalizable!

<div style="text-align: center;">
<em>안녕히가세요!!</em>
</div>

