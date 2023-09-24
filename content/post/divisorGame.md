+++
author = "Someone"
title = "divisor games"
date = "2023-09-23"
description = "allAboutAcronyms"
math = true
+++

Some analysis and generalization of a divisor game.
<!--more-->

- [audience](#audience)
- [setup](#setup)
- [analysis](#analysis)
- [parity is power](#parity-is-power)
- [parity of admissible pairs](#parity-of-admissible-pairs)
- [example - 2022](#example---2022)


## audience

This is like elementary school math, but with a twist so it's open to all levels of students.

## setup

Suppose we are playing the following game. There are two players, A and B, and player A plays first. There is a board of numbers enumerated as shown below.

![circle-game](/circle.png)

Then players take turns drawing line segments between divisible numbers i.e. $(1, 2)$, $(1,n)$, etc. This continues until a triangle is formed where $n$ is a vertex. In the below example, the person who places the last edge won (between the points $2,\lfloor n/2\rfloor$, and $n$). 

![circle-win](/circle-win.png)

The question we are interested in is:

> Who wins? For what values of $n$, do the players have a winning strategy?

## analysis

Let me first introudce the idea of an admissible pairing. We call a pair of numbers $i,j<n$ **admissible** if $i\mid j$ or $j\mid i$ and the opponent cannot win on the subsequent turn. Here are some examples:
- $(1,i)$ for $i\in[n]$
- $(2,i)$ for $i\in[n]$ such that $i\mod 2=0$

and here are some non-examples:
- $(2,i)$ for $i\in[n]$ such that $i\mod 2\neq 0$
- $(n,i)$ if $(i,k)$ and $(k,n)$ are already connected.

Now, what are the total number of turns possible in this game? If we let $d(i)$ denote the number of proper divisors of $i$, then this would be given by the sum of proper divisors:

$$\sum\limits_{i=1}^{n} d(i).$$

We know if this number is even or odd (its parity) based on the number of perfect squares less than or equal to $n$. Let us denote this number by $\mathcal{P}(n)$:

$$ \mathcal{P}(n)=  \\# \left\\{i: k^2=i, i\leq n \right\\}.$$

Then we know

$$\sum\limits_{i=1}^{n} d(i)\mod 2 = \begin{cases} 0 & \mathcal{P}(n)\mod 2 = 0 \\\\ 1 &\text{otherwise}.  \end{cases}$$

because a perfect square has a odd number of proper divisors while other numbers have an even number of proper divisors. 

Now what about the set of **admissible** pairs to start with? Well, we discount the above by the number of divisors of $n$. Let $\mathcal{A}(n)$ denote the set of admissible pairs. Then

$$ \mathcal{A}(n) \mod 2 = \begin{cases} 0 & \left(\mathcal{P}(n)\mod 2 = 0\cap  d(n)\mod 2 = 0\right)\bigcup \left(\mathcal{P}(n)\mod 2 = 1\cap  d(n)\mod 2 = 1\right) \\\\  1 & \left(\mathcal{P}(n)\mod 2 = 0\cap  d(n)\mod 2 = 1\right)\bigcup \left(\mathcal{P}(n)\mod 2 = 1\cap  d(n)\mod 2 = 0\right)\end{cases}.$$

This is a convoluted way of saying that parity of admissible solutions depends on if the parity of the number of perfect squares and number of divisors aligns (even parity) or doesn't (odd parity). 

## parity is power

Why did I rant about parity above? Well let me give a simple example:

- Suppose we start with numbers $\{1,2,3, 4\}$. 
- Player A selects $(1,2)$.
- Player B selects $(1,3)$
- Player A selects $(1,4)$
- Player B selects $(2,4)$ winning the game

In this example, $\mathcal{P}(n)=2$ and $d(n)=2$ so we have an even number of admissible turns. We could walk through many other combinations - Player B will win. However if instead, we had an odd number of admissible turns to start, then it's easy to see that player A would win every occasion. Why? Well, each turn decrements the number of admissible solutions by 1 until we reach zero - the loser. With a higher $n$ however, we know intuitively it's not that simple who wins. There are some nuances to the game we must discuss.

## parity of admissible pairs

Suppose a player makes the pairing $(n,l)$. Then all pairs $(l,m)$, where $m\mid l$ or $l\mid m$, are no longer admissible - if played, these would allow the opposing player to win with the pair $(n,m)$. Now, in order to know who can and cannot win, we must understand the parity of these pairs. If they're all even or odd, it is straightforward to understand who can win and who cannot, but life rarely works out like that.

As $n\mid l$, we know that given a prime factorization of $n$: 

$$ n=n_{1}^{i_1}n_{2}^{i_2}\cdots n_{k}^{i_k},$$

that 

$$ l= n_{1}^{a_1}n_{2}^{a_2}\cdots n_{k}^{a_k},$$

where $a_{1}\in\\{0,1,\dots,i_1\\},\dots,a_{k}\in\\{0,1,\dots,i_k\\}$. Then the number of divisors of $l$ is given by, discounting one for the case where $l=n$ (i.e. $a_{1}=i_{1},\dots ,a_{k}=i_{k}$):

$$ (a_{1}+1)(a_{2}+1)\cdots (a_{k}+1)-1.$$

To know the parity of this set, we also need to consider the case where $m\mid l$ (i.e. $m$ is a multiple of $l$). This number is given by, discounting 1 for the case where $m=l$ and another for the case where $m=n$: 

$$ (i_{1}-a_{1}+1)(i_{2}-a_{2}+1)\cdots (i_{k}-a_{k}+1)-2.$$

Combining these two numbers together gives the number of admissible pairs lost when we make the pairing $(n,l)$:

$$ (a_{1}+1)(a_{2}+1)\cdots (a_{k}+1) + (i_{1}-a_{1}+1)(i_{2}-a_{2}+1)\cdots (i_{k}-a_{k}+1) - 3.$$

This ugly expression contains all the information we need to know if someone can win and if so, how. Sadly, this requires good old-fashioned case analysis which is quite cumbersome depending on the size of the prime factorization.

## example - 2022

To wrap up how we might take this generalization and apply it, consider the case where $n=2022$. We will show that player A has an advantage if they follow the following strategy:

- On player A's first turn, they connects $1$ and $2$. This prevents player B from connecting $1$ and $2022$.
- If player B is forced to (or carelessly) draws a second edge with a triangle containing $2022$, then player A connects the last edge to win.
- Otherwise, player A just plays any admissible pair.

As $44^2=1936<2022$, there are $44$ perfect squares with an even number of proper divisors and $2022-44=1978$ numbers with an odd number of divisors and so this sum is even. As $2022$ has $7$ proper divisors ($1,2,3,6,337,674,1011$), the number of admissible pairs to start is odd. 

Now let us show that will always be true throughout the sequence of the game so long as player A makes the pairing $(1, 2)$ at the start. Suppose that a player connects $2022$ to $p$. Then all pairs $(p,k)$ where $p\mid k$ or $k\mid p$ are subsequently no longer admissible. The prime factorization of $2022$ is

$$2022=2\times 3\times 337,$$

and so $p$ must be of the form 

$$2^{a}3^{b}337^{c},\qquad (a,b,c)\in\{0,1\}^3.$$

The number of proper divisors of $p$ is thus given by 

$$(a+1)(b+1)(c+1)-1,$$

while the number of multiples of $p$, discounting for $p$ and $2022$, is given by 

$$(2-a)(2-b)(2-c)-2.$$

And so, the number of possible admissible pairs we drop after connecting $2022$ and $p$ is given by 

$$(a+1)(b+1)(c+1)+(2-a)(2-b)(2-c)-3.$$

This number is even iff $a=b=c$ i.e. $p\in\\{0,2022\\}$ and odd otherwise. **Thus**, if player A plays $(1,2)$ at the start, player B can never play $(1,2022)$ which swaps the parity of admissible solutions from odd to even. This proves player A wins as we showed all other instances maintain parity of admissible solutions (which is odd - good for player A).
