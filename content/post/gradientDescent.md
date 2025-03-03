+++
author = "Someone"
title = "descent"
date = "2024-12-08"
description = "gd"
math = true
+++

Yet another metaphor (this time it's gradient descent).
<!--more-->


## intuition

> Imagine a hiker trying to descend a mountain on an overcast day. Because of the haziness, the hiker cannot rely on knowing the full landscape of the mountain. Instead, they have to look around and explore promising areas with "downward" slope.

![Hiker](/hiker.jpg)

## some caveats

* We need the mountain to not have too many undulations and changes in slope otherwise the hiker may get stuck in bowls around the mountain that are not in fact the base.
* If a hiker steps towards the face of a cliff, they would fall off and die. But if they have an inkling of climbing ability, they can repel down.
![Honnold](/honnold.jpg)
* At some point in time, a hiker will reach a flat(ish) region and call it a day. They will not measure the slope at their feet until they find the exact bottom.
* The hiker has to decide how many steps he takes before rescanning the area for the steepest path down the mountain (it's tricky to get this right)

## formalization

I will not bother formalizing what zillions have already done better. Instead, I will simply link references.

**Book References**
* [Yurii Nesterov's "Lectures on Convex Optimization"](https://link.springer.com/book/10.1007/978-3-319-91578-4)
* [Arkadi Nemirovski and Aharon Ben-Tal's "Lectures on Modern Convex Optimization"](https://www2.isye.gatech.edu/~nemirovs/LMCOLN2023Spring.pdf)

**Lecture References**
* [Stanford's CS168 Notes](https://theory.stanford.edu/~tim/s16/l/l5.pdf)
* [Ruder's Literative Review](https://arxiv.org/pdf/1609.04747)

## code

Vanilla Gradient descent (constant step size, real-valued, convex $f$)
```python
def f(x):
    return x**2

def grad_f(x):
    return 2*x

def step_size(t):
    return 0.02

# If unknown f(x*), then compare f(x_t) and f(x_t-1) instead
opt_x = 0
acceptable_err = 0.001
guess = f(5)
i = 0
while abs(guess - opt_x) > acceptable_err:
    guess = guess - step_size(i) * grad_f(guess)
    i += 1

print(guess)
```

or the PyTorch equivalent

```python
import torch

def f(x):
    return x**2

guess = torch.tensor([5.0], requires_grad=True)
optimizer = torch.optim.SGD([guess], lr=0.02)
opt_x = 0
acceptable_err = 0.001
while abs(guess - opt_x) > acceptable_err:
    optimizer.zero_grad()
    f(guess).backward()
    optimizer.step()

print(guess.item())
```

## research

Where is research these days?

* Still plenty of applications left to explore: game theory, time series, distributed systems, quantum computing, etc.
* Step size regimes, algorithmic improvements (albeit far few in between)
* RL-specific optimization problems get a lot of attention because of LLMs

In my opinion, the theory of optimization is generally solved (and quite intuitive), but applications are still plenty abundant and worth pursuing.
