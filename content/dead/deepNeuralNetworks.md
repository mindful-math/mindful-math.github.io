+++
author = "Someone"
title = "neural networks"
date = "2023-08-25"
description = "cs182a - sahai - fa23"
math = true
+++

An admissible solution set to cs182 at Berkeley.
<!--more-->

## homework 0

### 1. gradient descent doesn't go nuts with ill-conditioning

> Consider a linear regression problem where we observe noisy observations, $ y=Xw^* + \epsilon $, 
where $ X \in \mathbb{R}^{n\times n} $ represents the data matrix, $w^*\in\mathbb{R}^n$ represents the ground truth, and $\epsilon \in \mathbb{R}^n$ represents some noise. Suppose $X$ is ill-conditioned, i.e. that $\lVert X \rVert \frac{ \lVert w \rVert}{ \lVert Xw \rVert}\gg 1$ and denote its largest eigenvalue by $\lambda_{\max}$. Instead of estimating the weight vector by $X^{-1}y$, suppose we perform gradient descent:
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

### 2. regularization from the augmentation perspective
> Let us consider a particular OLS setup: there is a data matrix $X\in\mathbb{R}^{n\times d}$, a measurement vector $y\in\mathbb{R}^{n}$, a weight vector $w\in\mathbb{R}^{n}$ such that $w\sim \mathcal{N}(0_{d}, \Sigma)$, $\Sigma=(\Gamma^{\intercal}\Gamma)^{-1}$ is positive semi-definite, and a model
> $$ y_i=w^{\intercal}x_i + \epsilon ,\qquad \epsilon\sim\mathcal{N}(0,1).$$
> Suppose we augment the data matrix and measurement vector so
> $$ \hat{X} = \begin{pmatrix} X \\\\ \Gamma\end{pmatrix}\in\mathbb{R}^{(n+d)\times d},\qquad \hat{y}=\begin{pmatrix} y \\\\ 0_{d} \end{pmatrix}\in\mathbb{R}^{n+d}.$$
> Show that the OLS solution with these augmented components is equal to the maximum a posteriori (MAP) estimate by Tikhonov regularization:
> $$ \mathrm{argmin}\_{w\in\mathbb{R}^{n}} \lVert \hat{y} - \hat{X}w \rVert_{2}^{2} = \left(X^{\intercal}X + \Sigma^{-1}\right)^{-1}X^{\intercal}y.$$

This is a lame problem. We use algebra to get from the OLS solution of the left-hand side to get to the right:

\begin{align}
(\hat{X}^{\intercal}\hat{X})^{-1}\hat{X}^{\intercal}\hat{y} &= \begin{bmatrix} \begin{pmatrix} X^{\intercal} & \Gamma^{\intercal} \end{pmatrix} & \begin{pmatrix} X \\\\ \Gamma \end{pmatrix} \end{bmatrix}^{-1} \begin{pmatrix} X^{\intercal} & \Gamma^{\intercal} \end{pmatrix} \begin{pmatrix} y \\\\ 0_{d} \end{pmatrix} \\\\
&= ( X^{\intercal}X + \Gamma^{\intercal}\Gamma )^{-1} X^{\intercal}y
\end{align}

### 3. vector calculus review
> Suppose $x,c\in\mathbb{R}^{n}$, $A=(a_1,\dots, a_n)\in\mathbb{R}^{n\times n}$, and $\nabla_x f(x)=\langle \frac{\partial f}{\partial x_1},\dots,\frac{\partial f}{\partial x_n}\rangle$ is a row vector. Then show 
> 1. $\nabla_x (x^{\intercal} c) = c^{\intercal}$
> 2. $\nabla_x \lVert x\rVert_2^2=2x^{\intercal}$
> 3. $\nabla_x (Ax) = A$
> 4. $\nabla_x (x^{\intercal} A x)=x^{\intercal}(A+A^{\intercal})$
> 5. Under what condition is 4. equal to $2x^{\intercal}A$?

1. $\nabla_x (x^{\intercal} c) = \nabla_x \left(x_1c_1 + x_2c_2 + \cdots + x_nc_n\right)  = c^{\intercal}$
2. $\nabla_x \lVert x\rVert_2^2 = \nabla_x x^{\intercal}x = \nabla_x \left( x_1^2 + x_2^2 + \cdots + x_n^2\right) = 2x^{\intercal}$
3. $\nabla_x (Ax) = \nabla_x (a_1x_1 + a_2x_2 + \cdots a_nx_n) = A$
4. For some reason, KaTeX doesn't support align without numbering:
\begin{align} \nabla_x (x^{\intercal} A x) &= \nabla_x \sum_{i=1}^n\sum_{j=1}^n a_{ij}x_ix_j \\\\ &= \left\langle \sum_{i=1}^n a_{i1}x_i + \sum_{j=1}^n a_{1j}x_j,\dots, \sum_{i=1}^n a_{in}x_i + \sum_{j=1}^n a_{nj}x_j\right\rangle \\\\ &=x^{\intercal}(A+A^{\intercal}) \end{align}
5. When $A$ is symmetric, $x^{\intercal}(A+A^{\intercal})=2x^{\intercal}A$

### 4. relu elbow update under sgd
> 1. Find the location of the elbow - i.e. where the loss transitions from zero to something else.
> 2. Find the derivative of the loss with respect to $\phi(x)$.
> 3. Find the partial derivative of the loss with respect to $w$.
> 4. Find the partial derivative of the loss with resepct to $b$.
> 5. What happens to the slope and elbow of $\phi(x)$ when $\phi(x)=0$.
> 6. What happens to the slope and elbow of $\phi(x)$ when $w>0,x>0,$ and $\phi(x)>0$.  
> 7. What happens to the slope and elbow of $\phi(x)$ when $w>0,x<0,$ and $\phi(x)>0$.  
> 8. What happens to the slope and elbow of $\phi(x)$ when $w<0,x>0,$ and $\phi(x)>0$.  

1. $x=-b/w$ is where the "elbow" (the non-differentiable point of the loss) is located.
2. $$\frac{d\ell}{d\phi}=(\phi(x)-y)\phi'(x)=\begin{cases} (\phi(x)-y)w & wx + b > 0 \\\\ 0 & \text{otherwise} \end{cases}$$
3. $$ \frac{\partial\ell}{\partial w}= \begin{cases} (\phi(x)-y)x & wx + b > 0 \\\\ 0 & \text{otherwise} \end{cases}$$
4. $$ \frac{\partial\ell}{\partial b}= \begin{cases} \phi(x)-y & wx + b > 0 \\\\ 0 & \text{otherwise} \end{cases}$$
5. We have 
$$ \begin{bmatrix} w_{t+1} \\\\ b_{t+1} \end{bmatrix}\leftarrow \begin{bmatrix} w_{t} \\\\ b_{t} \end{bmatrix} - \eta(\phi_t - y)\begin{bmatrix} x\phi_t \\\\ \phi_t \end{bmatrix}=\begin{bmatrix} w_{t} \\\\ b_{t} \end{bmatrix}$$

and so the slope, $w_{t+1}$, and elbow, $-\frac{b_{t+1}}{w_{t+1}}$, stay the same as before.

6. $$ \begin{bmatrix} w_{t+1} \\\\ b_{t+1} \end{bmatrix}\leftarrow \begin{bmatrix} w_{t} \\\\ b_{t} \end{bmatrix} - \eta(\phi_t - y)\begin{bmatrix} x\phi_t \\\\ \phi_t \end{bmatrix}$$

and so the slope, $w_{t+1}$, decreases by a positive amount $\eta x\phi_t$. The elbow becomes

$$ -\frac{b_{t}-\eta\phi_{t}}{w_{t}-\eta x\phi_{t}}=\underbrace{\frac{-b_t}{w_t}}\_{\text{prior elbow}} \times\frac{1-\frac{\eta\phi_{t}}{b_{t}}}{1-\frac{\eta x\phi_{t}}{w_t}}$$

which moves right or left depending on exact values of $\phi_t, x$, and $w_t$.

7. It's the same update as above, but the slope increases by $\eta x\phi_t$ as $x$ is negative here. However the elbow is slightly different - here $\phi_t>0$ but $x<0$ implies that $b_t>w_tx$ and so the elbow will move towards the origin. 

8. The slope decreases by a positive amount $\eta x\phi_t$ while the elbow again will scale but it depends exactly on $w_t,b_t,x$, and $\phi_t$.

### 5. using pytorch to learn the color organ


### 6. homework process and study group

(a)