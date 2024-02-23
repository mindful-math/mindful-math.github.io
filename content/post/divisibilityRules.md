+++
author = "Someone"
title = "divisibility"
date = "2024-01-27"
description = "divisibledivisors"
math = true
+++

Some refreshments on divisibility stemming from [this book](https://bookstore.ams.org/mcl-25).
<!--more-->

- [rules](#rules)
- [problems](#problems)

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

$$ x = \sum\limits_{i=0}^n 10^i a_i = \underbrace{\sum\limits_{i=0}^n (10^i-1)a_i}\_{M} + \underbrace{\sum\limits_{i=0}^n a_i}\_{N}.$$

for some $n\geq 0$ where each $a_i\in\\{0,1,\dots,9\\}$. Thus $x|3$ iff it divides both $M$ and $N$. It suffices to show that $M|3$ as $N|3$ is our divisibility rule. Notice that 

$$ \sum\limits_{i=0}^n (10^i-1)a_i =  (10-1)\sum\limits_{i=0}^n \sum\limits_{j=0}^{i-1} 10^j a_i$$

which tells us that $M|3$ as there is a factor of $9$.

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
This just follows from factorization as

$$\frac{x}{6}=\frac{x}{2\cdot 3}=\frac{x}{2}\cdot \frac{x}{3}.$$

</details>
<br>
<hr style="border:1.5px solid black">

> A number is divisible by 8 iff its last three digits are divisible by 8.

<details>
<summary> proof </summary>
Note that $10/8=1.25$, $100/8=12.5$, and $200/8=25$ implying that $1000|8$. The rest of the proof mirrors our divisibility rule for 4.

</details>
<br>
<hr style="border:1.5px solid black">

> A number is divisible by 11 iff the sum of digits in the evens place minus the sum of digits in the odd places is divisible by 11 or 0.

<details>
<summary> proof </summary>
This is a bit complicated, but the idea is somewhat similar to what we did with 3 and 9 except that we end up with an alternating series that we need to break up: $10^ia_i=(10+1)(10^{i-1}-10^{i-2}+\cdots + 1)$. I'll do this next round.

</details>
<br>
<hr style="border:1.5px solid black">

## problems

This section includes my answers to problems in the book "Mathematics via Problems Part 1: Algebra".

> Show that the number $1\cdots 1$, consisting of 1992 ones, is divisible by $111111$.

<details>
<summary> solution </summary>
The critical step is to see that

$$\underbrace{1\cdots 1}\_{n \text{ ones}}=\sum\limits_{i=0}^{n-1} 10^i.$$

From here, notice that 

$$ \frac{1\cdots 1}{111111}=\frac{\sum\limits_{j=0}^{1991} 10^j}{\sum\limits_{i=0}^5 10^i}. $$

Then as $1992/6=332$, we can rewrite the numerator to prove that $1\cdots 1 | 111111$

$$ \frac{\sum\limits_{j=0}^{331} 10^{6j}\sum\limits_{i=0}^5 10^i}{\sum\limits_{i=0}^5} = \sum\limits_{j=0}^{331} 10^{6j}.$$



</details>
<br>
<hr style="border:1.5px solid black">

