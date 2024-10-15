+++
author = "Someone"
title = "experiments"
date = "2024-09-14"
description = "experimentalEyes"
math = true
+++

A review of Cox's book "[Planning of Experiments](https://archive.org/details/planningofexperi0000coxd)".
<!--more-->

Here's a summary of what catches my eyes in the chapters.

- [preliminaries](#preliminaries)
- [some key assumptions](#some-key-assumptions)
- [designs for the reduction of error](#designs-for-the-reduction-of-error)
- [use of supplementary observation to reduce error](#use-of-supplementary-observation-to-reduce-error)
- [randomization](#randomization)
- [basic ideas about factorial experiments](#basic-ideas-about-factorial-experiments)
- [design of simple factorial experiments](#design-of-simple-factorial-experiments)
- [choice of number of observations](#choice-of-number-of-observations)
- [choice of units, treatments, and observations](#choice-of-units-treatments-and-observations)
- [more about latin squares](#more-about-latin-squares)
- [incomplete factorial design](#incomplete-factorial-design)
- [fractional replication and confounding](#fractional-replication-and-confounding)
- [cross-over designs](#cross-over-designs)
- [some special problems](#some-special-problems)
- [takeaways](#takeaways)


## preliminaries

- The book tries to capture the essence of how to plan an experiment
- In experiments, it's generally about relative quantities, not absolute ones (i.e. X > Y - workouts, diets, crop yields, etc.)
- **Experimental units** (or just units) are the plots of land, persons working out/dieting, animals, etc. being acted upon
- **Treatments** are the things we want to compare (workout A vs B, advertisement X vs Y...)

Requirements for a good experiment:

* No systematic error (comparing apples to oranges, comparing machinery at different times of day but trying to make conclusions invariant over time, cough all of finance charlatan work cough cough...)
* Precision (garbage in, garbage out) - work with tools that satisfy budget, time, etc. requirements but are precise enough to not give crappy/skewed values (classic example is any work with sensors data - huuge problem like self-driving, climate change, etc.).
* Stress test results (i.e. obtain a good sketch of the distribution: if rainy + snowy, car accident probability = 3%... uh oh, back to drawing board)
* Simplicity: make experiments reproducible by being simple. Math is the best experiment - you just need a pen, paper, and a set of axioms. Healthcare/drugs/finance are generally the worst - expensive setups, manipulating data, incomplete stress tests, sparse units

## some key assumptions

The main assumptions for statistical analysis (according to Cox) are

> 1) observation = (quantity depending ONLY on particular unit) + (quantity depending on treatment)
He says to note that the effect is additive and not multiplicative or subtractive or any other operation. Why? I think 
$$\text{effect}\approx \text{unit}+\text{treatment},$$
so when comparing differences of treatments, we have 
$$\mathbb{E}[\text{treatment difference}] = \mathbb{E}[\text{treatment 1}] - \mathbb{E}[\text{treatment 2}]$$

This is all by linearity of expectation. Had there instead been a multiplicative effect, we'd not be able to infer the treatment difference as units depend on treatments. He does note that if you somehow realized that the effects are multiplicative, you could take the log of observations to make log-linear claims... but this can get messy when doing inference I think* (but don't know)

> 2) treatment effects are constant
> 
I do not think this is a hard requirement as we could borrow metrics in a functional space (using stochastic dominance for instance). Maybe he meant it's a random variable with some distribution $D$ that doesn't change over time, unit, etc. 
> 3) observation of one unit is not affected by treatment applied to other units
> 
I.e. segway into double-blind experimments - we don't want people watching other people and being swayed to change the observation.


## designs for the reduction of error

The goal of the chapter is to explain how we can reduce uncontrolled variation of error when delivering treatment. The main idea for reducing variation is known as blocking/grouping. 

In blocking, we group units that are as alike as possible and assign treatments at random within the group, AND make comparisons within groups, then we can control for a lot of unwanted variation.

![Grouping](/groupings.png)

Now Cox provides a series of examples, but I found these resources much more insightful/useful for learning.

1. https://online.stat.psu.edu/stat503/book/export/html/646
2. https://n.ethz.ch/~kahans/doe2021/ch-blocking.html
3. https://artowen.su.domains/courses/363/pairblock.pdf
4. https://artowen.su.domains/courses/363/responsesurface.pdf (when groups are not categorical/discrete)
5. https://scholar.harvard.edu/files/kasy/files/experimentaldesign.pdf


## use of supplementary observation to reduce error

A concomitant observation is one whose value for any experimental unit is independent of the arrangement of the treatments under comparison. We can use these in combination with ANOVA (to level out concomitant values for all units) or by analyzing the response surface as in (4).

## randomization

Basically, the chapter lectures why subjective methods should not be used to assign treatments to units. But there are nuances with randomization - you could imagine blocked experiments where randomization gives the treatment schedule AAABBB (but we might a priori suspect these groupings could have confounding effects). It's largely a philosphical discussion.

## basic ideas about factorial experiments

Factorial experiments are ones where there are several independent variables we'd like to play with at the same time. Examples range from chemistry (tweaking the amount of carbon vs magnesium vs etc.) to climbing (i.e. dynamic moves involve a combination of feet, hand, and eye positions/movements ongoing simultaneously).

They introduce dumb terminology (i.e. variable reassignment - an easy way to fool a naive person into thinking you know what you're talking about...):

**factor**: a treatment
**level**: the number of possible quantities/qualities of the factor (i.e. 10g vs 20g vs 100g whey protein)
**complete factorial experiment**: an experiment involving the testing of all combinations of factors (i.e. 1g vs 10g vs 100g phosphate and 30g vs 300g vs 30000g potassium = 9 experiments)
**interaction (rough defintion for factors A and B)**: the effect due to factor a depends on the particular level of factor B

| Factor A / Factor B | B1  | B2  | B3  | B4  | Row Average |
|---------------------|-----|-----|-----|-----|-------------|
| **A1**                  | 5   | 7   | 6   | 8   | 6.5         |
| **A2**                  | 4   | 6   | 7   | 5   | 5.5         |
| **A3**                  | 8   | 5   | 7   | 9   | 7.25        |
| **Column Average**  | 5.67| 6   | 6.67| 7.33|             |

This is a two-factor table with three levels of A and four levels of B. In total, there are 12 combinations in this complete factorial experiment. 

> If 
> $$\text{change in observation} = \text{average effect of change in A} + \text{average effect of change in B}$$ 
> then A and B are additive and there is no interaction.

This seems interesting, but you'll end up with a lot of false positives with that strict of a definition - there should be some epsilon wiggle room for precision errors or approximately non-interacting effects. But even then, this feels useful in large scale processes with low stakes (like advertising on the internet - color + body type + exposure) - intuition really feels more valuable IMO. Another way of doing this is by regression and a test of significance for the interaction term.

$$y = \alpha A + \beta B + \gamma\underbrace{AB}_{\text{interaction term}} $$

Much like in chemistry experiments, interactions can only pop up for certain levels of A and B (i.e. it's not very useful to say A and B interact if for only a couple out of 500+ possible pairs). Computation with interactions is also a pain - that's why I prefer intuition again and pocket aside the statistics unless it makes sense (also most of the time we care about specific quantities and not absolute/generic statements about factors).

## design of simple factorial experiments

Really nothing noteworthy here - maybe it should be noted that when there are too many levels, you should hold constant some of the less "valuable/important" factors (i.e. pruning/cleaning out what you think is unimportant from the start - feels like this goes against his rant on randomization though...)

## choice of number of observations
 
The main interesting bit here was that you could perform experiments sequentially (expanding size as necessary) to look at standard error and calibrate larger studies perhaps. He spent a lot of time just talking about how standard error is proportional to one divided by the square root of the number of observations (so include as many observations if you want to be more precise in your statements).

## choice of units, treatments, and observations

Short, pointless chapter.

## more about latin squares

Again, he must be grasping for straws to extend the book's length here...

## incomplete factorial design

Youden squares (subsets of Latin squares) could be interesting in spaces like advertising (i.e. you do not have enough time to test all variations). The other use case he discussed (i.e. where units are too small to fit all treatments) doesn't seem super important these days. I'd almost reckon you should probably split up your experiment and control for confounding effects more carefully (or get specific and set one constant)...

## fractional replication and confounding

Hogwash - I think these are outdated techniques.

## cross-over designs

He just suggests using Latin squares where the experimental units (subjects, animals, etc.) used contribute substantially to the uncontrolled variation. I'm not sure  why this needed its own chapter and name "cross-over designs".

## some special problems

Skipped.

## takeaways

It's a pretty good book - I like how examples are abundant and he explicates key thoughts in plain vanilla English for the most part (no fancy equations, words, etc.). If I were to rewrite it, I'd spend more time in the examples doing inference and talking about the strengths/weaknesses of the experiment (because no two are alike and they're not all perfect).

[^1]: [Planning of Experiments](https://archive.org/details/planningofexperi0000coxd)
