+++
author = "Someone"
title = "git"
date = "2023-08-25"
description = "gettingGitGorgeous"
+++

This article covers basic git operations.
<!--more-->

## workflow 

POV: You're a new developer brought on for an ongoing project MLPants: the future of pants. Here's a picture of what that broadly looks like.

## First Step - `git clone`

MLPants is a repository hosted on either a third-party: Gitlab, Github, etc. (or a combination of the above) or a custom server hosting the bare repository. After obtaining access to the MLPants repository, you want to bring that access to your computer. `git clone` accomplishes this. Here are some variants:

```bash 
# Option 1: http[s]
git clone http[s]://host.xz[:port]/path/to/mlpants.git/ --recurse-submodules=<pathspec> 

# Option 2: ssh
git clone ssh://[user@]host.xz[:port]/path/to/mlpants.git/ --recurse-submodules=<pathspec>
``` 

HTTPS requests are less likely to get blocked by MLPants corporate firewalls, so generally option 1 is the way to go. There are many more possibilities here, but ignorance is bliss. `--recurse-submodules` is the only flag 
   
- `git clone https://<something>/mlpants.git --recurse-submodules=<pathspec>` is equivalent to running `git clone https://<something>/mlpants.git && git submodule update --init --recursive <pathspec>` (so it *could* be a useful flag to save a line of code)
   - None of the other flags [here](https://git-scm.com/docs/git-clone) seem like typical day-to-day ones.
2. After cloning, you play around with the system and accrue some familarity - design patterns used, tools, etc.
3. Then, you either assign yourself to a ticket (maybe for an open-source library) or your boss does (in enterprise). Let us say this is ticket `451`.
4. Create a branch name. A simple convention I saw on StackOverflow: `<category>/<ticket num>/<name>`. In our example, let us say we are working on adding an analytics dashboard for our application (a feature). Then a nice branch name would be `feature/451/analytics-dashboard`. The `<name>` field should be sort and spaces separated by hyphens or dashes. The category is generally enumerated from a list like below:
<center>

| category | description |
| ----- | ----- |
| bugfix | For fixing a bug |
| feature | For adding/editing/etc. a feature. |
| tempfix | For fixing a critical bug with a temporary solution. |
| wip |   For work that won't be done soon      |
|  junk or experiment    | For experimental work |
</center>

6. `git switch --create feature/451/analytics-dashboard` is the more modern version of `git branch --force feature/451/analytics-dashboard && git switch feature/451/analytics-dashboard`. It basically creates a new branch off the r
   1. But to make this even nicer, I recommend `git config --local push.autoSetupRemote true` which allows you to just write `git push` as opposed to `git push --set-upstream <remote> feature/451/analytics-dashboard`. 
   2. `push.autoSetupRemote` set to true will automaticaly add `--set-upstream` - basically, if no upstream conflicts exist (someone else pushing changes beforehand on the same branch), it will push to the upstream branch
   3. I'm not 100% certain of the following, but sometimes, you may need `git config --global push.default <simple | current | upstream | matching>`. If `push.autoSetupRemote` is set to true and `current` is specified, then `git push` pushes the current branch but does not set up remote tracking. If set to `upstream` or `simple`, then `git push` pushes the current branch and sets up remote tracking. If set to `matching`, then `git push` will update all local branches that share the same name and matching branches whilst setting up remote tracking. If you have several branches with the same name accidently, like "develop", then this will cause some headaches as you try to retrace your steps to reset develop on remote if the changes aren't the right ones.
7. Edit files and code as you go:
   1. `git add `

```bash
[push]
        autoSetupRemote = true
```




