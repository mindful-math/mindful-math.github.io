+++
author = "Someone"
title = "detection"
date = "2024-01-27"
description = "detectingdelectabledivisorsderangingdemons"
math = true
+++

A review of [this paper](https://arxiv.org/pdf/2401.12070.pdf) on an LLM detection test.
<!--more-->

- [setup](#setup)

## setup

Let $V=\\{v_1, v_2, \dots, v_n\\}$ denote an LLM's vocabulary and let $s=[x_1,\dots,x_l]$ denote the tokenized text to be tested. Then, the paper defines the log-perplexity of the tokenized text $s$ as the average of the negative log next-token probabilities. 

$$ \log \mathrm{PPL}(s) = -\frac{1}{l} \sum\limits_{i=1}^l \lg\left( P(x_i|x_1,\dots,x_{i-1}) \right).$$

Then the paper defines the cross-entropy as 

$$ \mathrm{somethin}$$



