+++
author = "Someone"
title = "technical writing"
date = "2023-08-25"
description = "technicalTricks"
math = true
+++

A overview of tricks discussed by Knuth [in this nice piece](https://jmlr.csail.mit.edu/reviewing-papers/knuth_mathematical_writing.pdf).
<!--more-->


## do not number lists if information isn't ranked

> Ordered lists are used if there is a logical ordering between bullets (time, importance, score, etc.). Using ordered lists with unordered elements (and vice-versa) can easily confuse the reader.

<details>
<summary> examples </summary>

**good**:

Hypothesis Testing consists of the following steps:
1. State the null and alternative hypothesis 
2. Collect data (by means of an experiment or by observation)
3. Determine an appropriate test statistic / test based on step 1 & 2
4. Compute the test statistic and p-value 

Here are some tricks for mathematical writing:
+ Separate distinct formulas by words
+ Do not start a sentence with symbols
+ Do not use logical symbols like $\forall, \exists, \therefore$ unless you're working in logic - replace with the corresponding English words "for all", "there exists", "therefore"

**bad**:

Hypothesis Testing consists of the following:
- State the null and alternative hypothesis 
- Collect data (by means of an experiment or by observation)
- Determine an appropriate test statistic / test based on the first and second part
- Compute the test statistic and p-value 

Here are some tricks for mathematical writing:
1. Separate distinct formulas by words
2. Do not start a sentence with symbols
3. Do not use logical symbols like $\forall, \exists, \therefore$ unless you're working in logic - replace with the corresponding English words "for all", "there exists", "therefore"
</details>
<br>

## avoid consecutively using "this", "also", "it", etc.

> If repeated too often, a reader can lose track of an author's message. Variable assignment in programming follows a similar cardinal rule - frequent reassignment of variables causes debugging nightmares.

<details>
<summary> examples </summary>

**good**:

The sum of deleted intervals in the Cantor set is geometrically decaying whose value is computed below:

$$ \sum\limits_{i=0}^\infty \frac{1}{3}\left(\frac{2}{3}\right)^i = \frac{1/3}{1-2/3} = 1.$$

As this sums to one, the Cantor set must have measure zero.

**bad**:

This forms a geometrically decaying series and its sum is given below

$$ \sum\limits_{i=0}^\infty \frac{1}{3}\left(\frac{2}{3}\right)^i = \frac{1/3}{1-2/3} = 1.$$

This shows that this set has measure zero...

</details>
<br>

## do not use "homework paper" style (i.e. just listing equations)

> While seemingly obvious, I see far too many bland papers with equations/proofs listed. Many readers skim over formulas on their first reading of your text. Commentary interwoven with formulas significantly boosts comprehension. If a formula is truly "trivial" to the target audience, it's fine to exclude this commentary

<details>
<summary> examples </summary>

**good**:

We can solve this problem by counting. Before painting the exterior of the cube black, there are

- $(n-2)^3$ cubes with zero faces showing
- $6(n-2)^2$ cubes with one face showing
- $4n(n-2)$ cubes with two faces showing
- $8\mathbb{I} \\\{n\geq 2\\\}$ cubes with three faces showing

Each of these $1\times 1\times 1$ sets of cubes can rotate while preserving the exterior color of the $n\times n\times n$ cube:

- If three faces are showing, 3 rotations are possible
- If two faces are showing, 2 rotations are possible
- If one face is showing, 4 rotations are possible
- If no faces are showing, 24 rotations are possible

In general, $n^3$ cubes can be placed in $n^3$ bins with $24$ rotations per cube giving us $24^{n^3}n^3!$ combinations. Thus, we obtain the probability that the exterior color is preserved:

$$\frac{24^{(n-2)^3}(n-2)^3!\times 4^{6(n-2)^2}\left(6(n-2)^2\right)!\times 2^{4n(n-2)}\left(4n(n-2)\right)!\times 3^{8\mathbb{I}\{n\geq 2\}}(8\mathbb{I}\{n\geq 2\})!}{24^{n^3}n^3!}$$

**bad**:

By counting, we obtain the desired probability:

$$ \frac{24^{(n-2)^3}(n-2)^3!\times 4^{6(n-2)^2}\left(6(n-2)^2\right)!\times 2^{4n(n-2)}\left(4n(n-2)\right)!\times 3^{8\mathbb{I}\{n\geq 2\}}(8\mathbb{I}\{n\geq 2\})!}{24^{n^3}n^3!} $$

</details>
<br>

## don’t use the same notation for two different things (and the converse)

> Notation is really an alphabet and in research, our goal is to use the most common, clear, and concise alphabet to maximize their audience and comprehension.
 
<details>
<summary> examples </summary>

**good**:

- asdf

**bad**:

- $\log\left(\log(n)\times i\times j\times k\right)=\infty$
- $\log$ has what base ($2$, $e$, etc.)?!? Does $\times$ refer to the cross product and multiplication here? 

</details>
<br>

