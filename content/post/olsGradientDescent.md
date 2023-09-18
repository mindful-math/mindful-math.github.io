+++
author = "Someone"
title = "ols descent"
date = "2023-09-09"
description = "interestingInterrelatedIdeas"
math = true
+++

A mashup of gradient descent and least squares.
<!--more-->

- [audience](#audience)
- [setup](#setup)
- [problem](#problem)
- [autoregressions tangent](#autoregressions-tangent)
- [lingering questions](#lingering-questions)

## audience
This is written towards someone who has taken a first course in statistics alongside a first course in linear algebra (and time series wouldn't hurt). The main takeaway is:
> Gradient descent applied to the squared loss for a linear model converges to the OLS solution **if your step size is small enough**.

## setup
An engineer observes noisy observations of a linear model, 

$$ y=Xw^* + \varepsilon ,$$ 

where $X\in\mathbb{R}^{n\times n}$ represents the data matrix (I'm assuming the number of features equals the number of data points for simplicity), $w^\*\in\mathbb{R}^{n} $ represents the true weight vector, and $\varepsilon \in \mathbb{R}^n$ represents some noise. Below is example data an engineer may come across with Gumbel error on measurements.

![Gumbel Errors](/exampleData.png)

Suppose $X$ is **ill-conditioned**, i.e. its condition number $\lambda_{\max}/\lambda_{\min}\gg 1$, then $\hat{w} =X^{-1}y $ **is not** a good approximation of $w^\*$ and in fact $\lVert \hat{w}-w^\*\rVert_{2}$ is huge! Wait... what... why? Well,

$$ \lVert \hat{w}  - w^\*\rVert_{2} = \lVert X^{-1}y - w^\* \rVert_{2} = \lVert X^{-1}(Xw^\* + \varepsilon) - w^\*\rVert_{2}=\lVert X^{-1}\varepsilon \rVert_{2}\leq \frac{1}{\lambda_{\min}}\lVert \varepsilon\rVert_2.$$

So more or less if $\lambda_{\min}$ is super tiny or our error, $\varepsilon$, is high, then this is a pretty lousy estimate for $w^\*$. What can the engineer do instead? 

<center> G -> r -> a -> d -> i -> e -> n -> t D -> e -> s -> c -> e -> n -> t. </center>


What is gradient descent? Well imagine we are pouring water into a glass. 


![Water](/drink.gif)

Because the glass is curved like a cone, the water naturally gravitates towards the bottom of the cup. Or more mathematically, the change in position of water with respect to time is proportional to the gradient/slope of the cup:

$$ \frac{d X}{dt} \propto -\nabla_X f(X).$$

If we discretize this, we get 

$$ X_{k} - X_{k-1} = -\eta \nabla_{X} f(X)\iff \underbrace{X_{k} = X_{k-1} - \eta \nabla_{X} f(X)}_{\text{Gradient Descent!}}$$

where $\eta$ controls how big of a step we take in the opposite direction of the gradient - this is known as the learning rate.

Our engineer wants to use these dynamics to optimize the weight vector $w$! The engineer needs a function whose gradients help guide the process towards the minimum like the water cup. A natural shape to consider is a parabola whose n-dimensional extension is known as a paraboloid. The squared L2 norm accomplishes this:

$$ \mathcal{L}(w) = \lVert y-Xw\rVert_{2}^{2}=\sum\limits_{i=1}^{n} (y_{i} - (Xw)_{i})^{2}.$$

Graphically, if $w$ is two-dimensional, the loss function looks almost like the glass above!

![loss-function](/lossFunction.png)

If we apply these dynamics to the weight vector problem, we get

$$ w_{k} \leftarrow w_{k-1} - \eta \underbrace{ X^{\intercal}(Xw_{k-1} - y)}\_{\nabla_{w} \mathcal{L}(w_{k-1}) }.$$

TBH, here an engineer stops caring about the math and pops out an estimate for $w^*$. But we're not *just* engineers.

## problem

 > How close does the gradient descent estimate get to the OLS estimate?
$$ \hat{w}\_{\text{OLS}}= \mathrm{argmin}\_{ w\in\mathbb{R}^{n}} \lVert y-Xw\rVert_{2}^{2} = (X^{\intercal} X)^{-1}X^{\intercal} y.$$

First, let's rearrange the equation: 

$$ w_{k} \leftarrow w_{k-1} + \eta X^{\intercal}(y - Xw_{k-1}) = (I_n - \eta X^{\intercal}X)w_{k-1} + \eta X^{\intercal}y.$$

Notice that $X^{\intercal} X$ is positive semi-definite (PSD) since $w^{\intercal} X^\intercal X w= \lVert Xw\rVert_{2}^{2}\geq 0$ for all $w\in\mathbb{R}^{n}$ (norms measure length). By spectral theorem, we can diagonalize this so 

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

But you may say why not then just set $\eta$ to be something super tiny so that it's nearly impossible to be greater than $2/\lambda_{\max}$ - well, that slows down convergence if we inch along. More discussion on this is another notebook. 

## autoregressions tangent

A autoregressive equation is an iterative sequence that can be recursively solved: 

$$ a_{k}\leftarrow \alpha a_{k-1}=\alpha (\alpha a_{k-2})=\alpha(\alpha (\alpha a_{k-3}))=\cdots =\alpha^k a_0.$$

This is finite for all $k\in\mathbb{N}$ if $|\alpha|\leq 1$.Below, we visualize this for several $\alpha$.

![autoregressive-graphs](/autoregressive_overlay.gif)

Remember an autoregressive equation from gradient descent?! No - well, it's this:

$$ P(I-\eta D)^{k}P^{\intercal} w\_{0} + \sum\limits\_{i=0}^{k-1} P(I - \eta D)^{i}P^{\intercal} \times \eta X^{\intercal}y.$$

This update forms a set of $n$ autoregressions! In this instance, the $(1-\eta\lambda_{i})$ for the $i$th equation controls if the sequence explodes or shrivels! 

## lingering questions

1. Convergence guarantees for gradient descent? How do these relate to the geometry of the loss and step size chosen?
2. What happens if we add a non-constant step size instead? How?
3. What happens if we introduce other dynamics like acceleration/gravity present when water falls down? What other algorithms are useful for this kind of problem?
4. What happens for non-square matrices? And could you explain conditioning better?
5. What about implementation?!? Could you code this? No - that's for you to find out :)
