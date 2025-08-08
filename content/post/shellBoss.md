+++
author = "Someone"
title = "shell"
date = "2025-09-08"
description = "shellShock"
math = true
+++

Some useful shell commands and examples.
<!--more-->

## distribution of commands (today)

Don't judge me too hard, but (excluding `git`, `python`, `java`, etc.), these are my latest shell commands (ignore that the usages do not add up to 100).

| Command | Usage |
| ----- | ----- |
| ls | 15 |
| cd | 25 |
| clear | 6 |
| mv | 5 |
| rm | 5 |
| source | 6 |
| man | 4 |
| pwd | 2 |
| cp | 2 |
| mkdir | 2 |
| scp | 1 |
| cat | 1 |
| su | 1 |
| ssh | 1 |
| grep | 1 |
| chmod | 1 |
| whoami | 0 |

## ls

`ls` stands for list I believe and just lists the **file names** in the current directory. It hides dotfiles however unless you include the `-a` argument. I forget the meaning of `l`, `h` and, and `a` so I often check the manual :(.

### short term memory

```bash
>>> ls -R
# first lists files like `ls`
public
static
...

./public:
about
css

./public/about:
index.html
...
```

```bash
ls -S # sort by file size (descending)
ls -a # include dotfiles
ls -c # sort by latest edit
ls -lh # adds suffixes to denote file size (Byte, Kilobyte, etc.)
ls -r # reverses order sort (i.e. ls -rS sorts files by ascending file size)
```

## cd

`cd` stands for "change directory" and moves your `pwd` to whatever the argument specifies. I do not think I use any flags for `cd` but use tabs for autocompletion and `..` of course denotes moving to the parent directory.

### short term memory

```bash
>>> cd # with no arguments, this takes you to the $HOME directory
>>> cd - # takes you back to the previous directory
```



## wishlist

These are some commands that I would like to internalize in the future.

```
tar
gzip
pv
awk
nano
systemctl
netstat/ss
stat
mmv
sed
ping
ip
```