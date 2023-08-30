+++
author = "Someone"
title = "matrix algebra"
date = "2023-08-27"
description = "madMatrixMethods"
math = true
+++

Some intuition on matrices & basic operations.
<!--more-->

- [audience](#audience)
- [setup](#setup)
- [matrix vector multiplication](#matrix-vector-multiplication)
- [matrix addition (and subtraction)](#matrix-addition-and-subtraction)
- [scalars and matrices](#scalars-and-matrices)
- [matrix multiplication](#matrix-multiplication)
- [other properties](#other-properties)
- [references](#references)


## audience
This is geared towards students taking a first course in linear algebra. Anyone above this level will not benefit from going further.

## setup

There are three goods at the Farmer's market: broccoli, chicken, and black tea. Our budget is \$100 and prices are listed below

| Food | Unit Cost (USD) |
| ----- | ----- |
| Broccoli | 5 |
| Chicken | 10 |
| Black Tea | 1 |

Furthermore, we want at most $a$ calories and at least $b$ grams of protein. The nutritional profiles are displayed below

| Food | Unit Calories | Unit Grams of Protein | 
| ----- | ----- | ----- |
| Broccoli | 20 | 1 | 
| Chicken | 100 | 20 | 
| Black Tea | 5 | 0 | 

We can write out these requirements as a system of equations. Let a unit of broccoli be represented by $x$, a unit of chicken be represented by $y$, and a unit of black tea be represented by $z$. Then that system, algebraically, looks like the following

$$
\begin{matrix}
5x + 10y + z \leq 100, \\\\
20x + 100y + 5z \leq a, \\\\
x+20y + 0z \geq b.
\end{matrix}
$$

Let's look at the first inequality visually. In the figure below, the blue plane represents the line $5x+10y+z=100$. To the left of this plane in green, are the points $(x,y,z)$ such that $5x+10y+z<100$. To the right of the plane in red are the points $(x,y,z)$ such that $5x+10y+z>100$ (these do not match our price requirements). 
<center>

![calories](/post/constraint.png)
</center>

We want to satisfy **all** three requirements. A solution is contained in the intersection of space formed by the inequalities. Another way to represent our system is with matrices. The rows of the matrix represent the four requirements above while the columns represent the units of broccoli, chicken and black tea:

$$\underbrace{\begin{pmatrix} 5 & 10 & 1 \\\\ 20 & 100 & 5 \\\\ 1 & 20 & 0 \end{pmatrix} }\_{A}  \underbrace{\begin{pmatrix} x \\\\ y \\\\ z \end{pmatrix}}\_{\vec{x}} \begin{matrix} \leq \\\\ \leq \\\\ \geq \\\\ \geq \end{matrix} \underbrace{\begin{pmatrix} 100 \\\\ a \\\\ b \end{pmatrix}}\_{\vec{b}}.$$

Remember these symbols and definitions for the rest of the blog: $A$, $\vec{x}$, and $\vec{b}$. 

## matrix vector multiplication

The matrix $A$ above takes a vector $\vec{x}$, which represents the quantities of broccoli, chicken and black tea, and outputs the price, calories, and protein for that food. And this leads to the big picture:

> A matrix of size $m\times n$ ($m$ rows and $n$ columns), is a linear function that takes $n$ variables as input and outputs $m$ variables.

They're convenient ways of expressing higher-dimensional linear systems of equations. Matrix vector products, $f(\vec{x})=A\vec{x}$, are **just** like the one-dimensional analogue: $f(x)=ax$. The matrix $A$ behaves very similarly to the coefficient $a$. I will demonstrate this below.


## matrix addition (and subtraction)

For linear functions, we have that if $f(x)=ax$ and $g(x)=bx$, then $(f+g)(x)=(a+b)x$. Well, that is true with matrices - we'll show this by continuing the market analogy.

Suppose that inflation is now hitting the Farmer's market - units of broccoli are 5\% more expensive, units of chicken are 15\% more expensive, and black tea is actually 5\% less expensive. Moreover, assume that nutritionists actually discovered that chicken has 20\% more protein than reported before and broccoli actually has 6\% less calories if eaten raw. Then, our system of equations becomes:

$$ 
\begin{matrix}
5(1.05)x + 10(1.15)y + (0.95)z \leq 100, \\\\
20(0.94)x + 100y + 5z \leq a, \\\\
x+20(1.2)y + 0z \geq b
\end{matrix}
$$

Matrix addition adds the elements of the the matrices we are interested in elementwise: i.e. the first row, first column of $A$ and $\Delta A$ below form the first row, first column of the new matrix $A_{\text{A}}$.

$$ 
\underbrace{\begin{pmatrix} 5 & 10 & 1 \\\\ 20 & 100 & 5 \\\\ 1 & 20 & 0 \end{pmatrix}}\_{A} + 
\underbrace{\begin{pmatrix} 0.05\cdot 5 & 0.15\cdot 10 & -0.05\cdot 1 \\\\ -0.06\cdot 20 & 0 & 0 \\\\ 0 & 0.2\cdot 20 & 0 \end{pmatrix}}\_{\Delta A} = 
\underbrace{\begin{pmatrix} 5(1.05) & 10(1.15) & 1(0.95) \\\\ 20(0.94) & 100 & 5 \\\\ 1 & 20(1.2) & 0 \end{pmatrix}}\_{A_{\text{new}}}.
$$ 

## scalars and matrices

For a constant $c$, we know 1. $cf(x)=cax$ and 2. $c(f+g)(x)=c(a+b)x=cax+cbx$. Multiplication of a constant $c$ times a matrix $A$ is a lot like matrix addition in that the scalar is applied elementwise to all entries. With the above example,

$$
cA=
c \begin{pmatrix} 5 & 10 & 1 \\\\ 20 & 100 & 5 \\\\ 1 & 20 & 0 \end{pmatrix} = \begin{pmatrix} 5c & 10c & c \\\\ 20c & 100c & 5c \\\\ c & 20c & 0 \end{pmatrix}.
$$

With this and the previous property of addition, you can prove 2.

## matrix multiplication

With linear functions, we have a nice property that $f\circ g(x)=abx$ if $f(x)=ax$ and $g(x)=bx$. This is function composition - we take the output of $g$ and throw that as the input of $f$ and express this all together in one equation: $abx$. 

The same goes for matrices so long as the input of $f$ has the same dimensions as the output of $g$. To show this, let's work with the system of equations for the matrix $A$.

$$
f\circ f(\vec{x})=
f\left( A\vec{x}\right)=
f\left(\begin{pmatrix}
5(1.05)x + 10(1.15)y + (0.95)z \\\\
20(0.94)x + 100y + 5z \\\\
x+20(1.2)y + 0z
\end{pmatrix}\right)=
A^2x.
$$

## other properties

The following are going to be created in other posts or content is linked below. Reinventing the wheel is not always necessary.
- matrix transposition
- matrix inverses
- matrix "division"
- matrix "length"
- finding the "roots" of a matrix
- dot product

## references


 