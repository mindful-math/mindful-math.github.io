+++
author = "Someone"
title = "cnns"
date = "2026-02-07"
description = "limitingLimitsLore"
math = true
+++

Decrypting bad vocab in CNNs. 
<!--more-->

- [definitions](#definitions)

## definitions

> **Kernel**: A locally-weighted moving average.

This is ridiculous terminology by the DL community. We convolve two functions and the "kernel" is a function we apply to each image/time-series/data to smooth it, sharpen it, etc. (a transformation) that weights values nearby each other. To be fair, statisticians use "correlation" and "cross-correlation" as instances of a normalized dot product.

> **Stride**: A downsampling of the convolution integral/sum

Stride has a nice physical meaning and is used in computer science but I really just think it's likened more to widening the aperture in a camera (at f/11 or higher, we see the large brush strokes of the image but miss out on the fine, rich local detail). Generally a stride of size $P$ means that in each dimension means that we convolve the kernel with our data with the initial position at $0,P,\dots,\lfloor n/P\rfloor$ for each dimension. You can specify this differently for each dimension if you want to feel special for once.

> **Zero padding**: We extend the domain of a function and set the range to zero.

 "Zero padding of size xyz" - shut up with your pseudoscience / blabbering... We are just extending the original domain and setting values of zero because we don't have signal here but would like to define our convolution over wider ranges of the input without needing to shrink the "kernel". A zero padding size of $P$ for a K-d tensor adds $KP$ to each dimension of zeros - really dumb terminology IMO...  
