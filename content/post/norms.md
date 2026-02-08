+++
author = "Someone"
title = "norms"
date = "2026-02-08"
description = "limitingLimitsLore"
math = true
+++

Some reference visuals for normed regularization. 
<!--more-->

- [definitions](#definitions)

## definitions

Normed regularization adds a term like $\lVert w\rVert_p$ that is the lp norm of your weights to your original objective function. There are two hyperparameters you introduce here - the norm itself which controls the family of models/weights you guide the model towards along with the penalization attached to this norm term when minimizing that controls how much we care to guide the weights in the direction specified by the norm & original loss function.

## $\ell_0$
This norm encourages extreme sparsity - the norm counts the number of nonzero elements in the weight vector. You cannot differentiate it (gradient is zero everywhere) and so you solve this combinatorially.\n

![l0](/p_norm_ell_0.png)

## $\ell_1$
This norm has sharp edges and a constant gradient for non-zero weights that expedite them in the direction of the origin (sparsity).\n

![l1](/p_norm_ell_1.png)

## $\ell_2$
This norm likewise encourages smaller weights but its spherical structure and vanishing gradient near the origin encourage non-zero, small weights.\n

![l2](/p_norm_ell_2.png)

## $l_\infty$
I forgot to add a picture of this, but it takes the maximum of each component and ensures weights are uniformly bounded but not necessarily minimized.

## references

* Claude generated the plots here; I love handing off trivial things like this - matplotlib is just more syntax I don't need to solve problems
