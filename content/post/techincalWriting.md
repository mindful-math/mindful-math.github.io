+++
author = "Someone"
title = "writing"
date = "2023-12-09"
description = "technicalTricks"
math = true
+++

A overview of tricks discussed by [Knuth](https://jmlr.csail.mit.edu/reviewing-papers/knuth_mathematical_writing.pdf) and [Halmos](https://faculty.washington.edu/heagerty/Courses/b572/public/HalmosHowToWrite.pdf). 
<!--more-->

- [tactical advice](#tactical-advice)
  - [do not number lists if information is not ranked](#do-not-number-lists-if-information-is-not-ranked)
  - [avoid consecutively using "this", "also", "it", etc.](#avoid-consecutively-using-this-also-it-etc)
  - [do not list flavorless equations (homework style)](#do-not-list-flavorless-equations-homework-style)
  - [do not use the same notation for two different things (and the converse)](#do-not-use-the-same-notation-for-two-different-things-and-the-converse)
  - [go away with inline horizontal mathematical fractions (and complex exponents)](#go-away-with-inline-horizontal-mathematical-fractions-and-complex-exponents)
  - [edit in spirals](#edit-in-spirals)
- [broad advice](#broad-advice)
  - [say something substantial](#say-something-substantial)
  - [do not introduce too many ideas](#do-not-introduce-too-many-ideas)
  - [write to a very specific audience in mind](#write-to-a-very-specific-audience-in-mind)

## tactical advice

These subsections enumerate concrete issues you can lint your papers for.

### do not number lists if information is not ranked

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
<hr style="border:1.5px solid black">

### avoid consecutively using "this", "also", "it", etc.

> If repeated too often, a reader can lose track of an author's message. Variable assignment in programming follows a similar cardinal rule - frequent reassignment of variables causes confusion and chaos.

<details>
<summary> examples </summary>

**good**:

The sum of deleted intervals in the Cantor set is geometrically decaying,

$$ \sum\limits_{i=0}^\infty \frac{1}{3}\left(\frac{2}{3}\right)^i = \frac{1/3}{1-2/3} = 1.$$

As this sums to one, the Cantor set must have measure zero.

**bad**:

This forms a geometrically decaying series and its sum is given below

$$ \sum\limits_{i=0}^\infty \frac{1}{3}\left(\frac{2}{3}\right)^i = \frac{1/3}{1-2/3} = 1.$$

This shows that this set has measure zero.

</details>
<br>
<hr style="border:1.5px solid black">

### do not list flavorless equations (homework style)

> Many readers skim over formulas on their first reading of your text. Commentary interwoven with formulas significantly boosts comprehension. If a formula is truly "trivial" to the target audience, then and only then is it fine to exclude.

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
<hr style="border:1.5px solid black">

### do not use the same notation for two different things (and the converse)

> In research, our goal should be to maximize the span of our work while minimizing redundancies and the size of our notation. Repeated, unclear, or nonstandard notation exponentially increases the chance that a paper will not be read. The [Zen of Python](https://peps.python.org/pep-0020/) applies here as well.

<details>
<summary> examples </summary>

**good**:

- $\ln(\ln(n))\cdot \left(\sum\limits_{i=1}^n \binom{n}{i}x^i\right)\cdot \left(\sum\limits_{j=1}^n  jx^j\right)$
- $\sum\limits_{i=1}^{\lfloor m/2\rfloor} \sum\limits_{j=2i}^{m} \prod\limits_{k=0}^{i-1} \binom{m-2k}{2} j^{m-2}$

**bad**:

- $\log\left(\log(n)\times i\times j\times k\right)\cdot \left(\sum\limits_{i=1}^n \binom{n}{i}x^i\right)\cdot \left( x^2 + 2x^2 + \cdots nx^n \right)$
  - $\log$ here has what base ($2$, $e$, etc.)?
  - Does $\times$ refer to the cross product and multiplication here? 
  - Does $i$ refer to the standard basis vector $(1,0,0)$ and/or a natural number under the summation?
  - The above also misses consistency by using sigma notation as well as an expanded out summation.

</details>
<br>
<hr style="border:1.5px solid black">

### go away with inline horizontal mathematical fractions (and complex exponents)

> Horizontal fractions shrinks the font and makes it very difficult to read. Slashes are perfect alternatives in this case.

<details>
<summary> examples </summary>

**good**: 

- $(1-x)/(1+\cos(x))$ is a perfect counterexample to this statement.
- This kernel, $\exp(-|x-\mu|^3)$, belongs to the exponential power distributions.

**bad**: 

- $\frac{1-x}{1+\cos(x)}$ is a perfect counterexample to this statement.
- This kernel, $e^{-|x-\mu|^3}$, belongs to the exponential power distributions.

</details>
<br>
<hr style="border:1.5px solid black">

### edit in spirals

> It is important to edit your paper or book in spirals. Write section 1, break, rewrite section 1 and write section 2, break, etc. I have never heard of this before Halmos' paper, but spiraling edits is conducive to creating flow (readers care primarily about flow in the earlier chapters/sections of course).

<details>
<summary> examples </summary>

- In each spiral, rewrite and do NOT break out your red pen and start editing! Editing occurs right before you hand it off to colleagues/journals for submission and right after their feedback.
- Halmos recommends that in each NEW section, you write your heart out and violate all the principles outlined here. Just write and write until you cannot, but make sure you end the day on a good note to kickstart the engine for tomorrow.
- Halmos explains this strategy [here](https://faculty.washington.edu/heagerty/Courses/b572/public/HalmosHowToWrite.pdf) on page 9/30.

</details>
<br>
<hr style="border:1.5px solid black">

## broad advice
These subsections illustrate general principles you should carry in mind when writing.

### say something substantial

> The problem with the internet and 21st century research summarized in three words. It is hard to say something about nothing; however, many researchers are now, more than ever, incentivized by tenure and promotions to crank out papers regardless of substance.
<details>
<summary> examples </summary>

**good**:

- [An Introduction to Probability Theory and Its Applications](https://archive.org/details/dli.ernet.5666/page/n13/mode/2up) by William Feller is my personal favorite mathematics book. It's unbelievably substantive and well-written and I highly recommend for anyone interested in probability.
- [Theory of Statistical Estimation](https://digital.library.adelaide.edu.au/dspace/bitstream/2440/15207/1/85.pdf) by Ronald Fisher is a beautifully written exposition on classical statistics (consistency, sufficiency, etc.). To be honest, most modern day statistics books just copy paste what he writes here.
- [The Extent and Consequences of P-Hacking in Science](https://journals.plos.org/plosbiology/article?id=10.1371/journal.pbio.1002106&) is a surprisingly great read on p-hacking in the sciences. There is a clear message the authors set out to achieve. 

**bad**:

AI is so bloated - the field is becoming an empirical mess. Here are just two examples violating this principle.
- [Deep Learning for COVID-19](https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=9136710) is an example paper that just rambles on and on for 20 pages with nothing novel to say.
- [TA-GATES](https://proceedings.neurips.cc/paper_files/paper/2022/file/d0ac28b79816b51124fcc804b2496a36-Paper-Conference.pdf) describes an encoding scheme for neural architectures. I'm so tired of reading empirical papers like this that just throw schemes on the wall and name them in an attempt to satisfy their university's publishing requirements. This doesn't necessarily violate the principle of having something to say, but concisely saying it.

</details>
<br>
<hr style="border:1.5px solid black">

### do not introduce too many ideas

> Keep it simple and stupid (KISS). A mile wide and an inch deep is not the goal - no one cares you can write "Hello World" in 150 programming languages. This caution is primarily directed towards authors writing books.

<details>
<summary> examples </summary>

**good**:

- [An Introduction to Probability Theory and Its Applications](https://archive.org/details/dli.ernet.5666/page/n13/mode/2up) by William Feller is also amazing in this regard. He glides and links many disparate (at the time the book was published) ideas into one unifying theory full of lucid examples and exercises.
- [Ron Rivest's](https://dl.acm.org/doi/pdf/10.1145/359997.360000) discussion on self-organizing search heuristics has a very clear linear flow without spontaneous ideas floating around.

**bad**:

- [Elements of Statistical Learning Theory](https://link.springer.com/book/10.1007/978-0-387-84858-7) or ESL by Hastie, Tibshirani, and Friedman is a mess to be honest. Albeit a controversial choice, ESL introduces too many surface level ideas without any substance. It cannot even serve as an encyclopedia for researchers because it misses a zillion ideas introduced since then.

</details>
<br>
<hr style="border:1.5px solid black">

### write to a very specific audience in mind

> You need to pick a specific audience like professional statisticians, undergraduate math majors, your neighbors, etc. This guides your formality, tone, how much motivation you give the reader, the details you choose to show and hide, etc. When writing a book or article, state the audience very clearly upfront unless the audience is 100% implicitly understood (i.e. publishing in a prestegious math journal).

<details>
<summary> examples </summary>

**good**:

- [Donald Knuth's](https://www.taylorfrancis.com/books/mono/10.1201/9781315139470/classification-regression-trees-leo-breiman) "The Art of Computer Programming" series is a phenomenal exposition for beginning graduate or junior students studying math and/or computer science. 
- [An Introduction to Probability Theory and Its Applications](https://archive.org/details/dli.ernet.5666/page/n13/mode/2up) by William Feller - he writes "... [I hope that this book] will continue to find readers who read it merely for enjoyment and enlightment". When a author writes a line like this, you know they are writing from their heart and the book is bound to be a blast. Furthermore, Feller like Knuth, had a sea of useful critics like Doob, Donsker, and Chung to help him shape the book into what it now is. The moral of these two stories is that you follow this process until you reach 3. successfully or death (whichever comes first):

1. Find a target and a good crowd of experts that know this target
2. Shoot 
3. In the unlikely chance you hit your target, terminate the algorithm.
4. Otherwise, listen to expert advice. Get set up again and go back to 1 or 2.

**bad**:

- [Walter Rudin's](https://maa.org/press/maa-reviews/principles-of-mathematical-analysis) "Principles of Mathematical Analysis" is a great book and a rite of passage for most math students; however, its audience needs to be more concretely laid out. A student should have taken a proofs course and probably a set theory or point-set topology course prior to partaking in this adventure. The book is a good example of setting a target but hitting something else.
- [Aminian and Xu's](https://www.amazon.com/Machine-Learning-System-Design-Interview/dp/1736049127) "Machine Learning System Design Interview" is a horrible read. It's surface level architecture notes NOT useful for engineers interested in senior architect roles. 

</details>
<br>
<hr style="border:1.5px solid black">
