+++
author = "Someone"
title = "divisibility"
date = "2024-01-27"
description = "divisibledivisors"
math = true
+++

Some refreshments on divisibility stemming from [this book](https://bookstore.ams.org/mcl-25).
<!--more-->

- [new](#new)
- [review](#review)
- [research](#research)
- [references](#references)

In all of these cases, I am just working in base 10. I rediscovered how fun arithmetic is - these proofs were fun to come up with! Although written for myself, if you stumble on this article, I recommend trying them out for yourself (unless you've already gone through a first course in number theory).

## rules

<hr style="border:1.5px solid black">

> A number is divisible by 2 iff its last digit is divisible by 2.

<details>
<summary> proof </summary>
Given a number $x$, we can write it out as

$$ x = a_na_{n-1}\cdots a_0 = a_0 + \sum\limits_{i=1}^n 10^i a_i = a_0 + \underbrace{2\cdot 5\sum\limits_{i=1}^n 10^{i-1} a_i}_{M}$$

for some $n\geq 0$ where each $a_i\in\\{0,1,\dots,9\\}$. Note that $M$ is divisible by $2$, so $x | 2$ iff $x | a_0$ (the ones digit).

</details>
<br>
<hr style="border:1.5px solid black">

> A number is divisible by 3 iff the sum of its digits is divisible by $3$.

<details>
<summary> proof </summary>
Given a number $x$, we can write it out as

$$ x = \sum\limits_{i=0}^n 10^i a_i =\cdots $$

for some $n\geq 0$ where each $a_i\in\\{0,1,\dots,9\\}$. 

</details>
<br>
<hr style="border:1.5px solid black">

> A number is divisible by 4 iff its last two digits are divisible by $4$.

<details>
<summary> proof </summary>
Given a number $x$, we can write it out as

$$ x = \sum\limits_{i=0}^n 10^i a_i = \underbrace{a_0 + 10a_{1}}\_{M} + \underbrace{\sum\limits_{i=2}^n 10^i a_i}_{N} $$

for some $n\geq 0$ where each $a_i\in\\{0,1,\dots,9\\}$. Notice that as $4\cdot 25 = 100$, $N | 4$ and so $x|4$ iff $M|4$ (i.e. the two digits are divisible by 4). 

</details>
<br>
<hr style="border:1.5px solid black">

> A number is divisible by 5 iff its last digit is either $0$ or $5$.

<details>
<summary> proof </summary>
Given a number $x$, we can write it out as

$$ x = \sum\limits_{i=0}^n 10^i a_i = a_0 + \underbrace{5\cdot 2\sum\limits_{i=1}^n 10^{i-1} a_i}_{M} $$

for some $n\geq 0$ where each $a_i\in\\{0,1,\dots,9\\}$. Notice that as $M|5$, and so $x|5$ iff $a_0|5$ which is the case so long as $a_i\in\\{0,5\\}$.

</details>
<br>
<hr style="border:1.5px solid black">

> A number is divisible by 6 iff it is divisible by 2 and 3.

<details>
<summary> proof </summary>
This just follows from factorization

$$\frac{x}{6}=\frac{x}{2\cdot 3}=\frac{x}{2}\cdot \frac{x}{3}.$$

To be continued...


## problems


