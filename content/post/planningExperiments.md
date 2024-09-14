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

## preliminaries

- The book tries to capture the essence of how to plan an experiment
- Care about the relative quantities, not the absolute quantities (i.e. X > Y - workouts, diets, crop yields, etc.)
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

The goal of the chapter is to explain how we can reduce uncontrolled variation when estimating treatment comparisons. First and foremost when conducting an experiment, envision where your variation could arise from as a set of premises. 

Here's the deal. Suppose 



## use of supplementary observation to reduce error

## randomization

## basic ideas about factorial experiments

## design of simple factorial experiments

## choice of number of observations

## choice of units, treatments, and observations

## more about latin squares

## incomplete factorial design

## fractional replication and confounding

## cross-over designs

## some special problems

## preliminaries



[^1]: [Einstein's Mass-Energy Equivalence](https://en.wikipedia.org/wiki/Mass%E2%80%93energy_equivalence)
