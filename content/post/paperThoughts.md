+++
author = "Someone"
title = "ruminations"
date = "2026-04-09"
description = "asdf"
math = true
+++

Some papers and thoughts on progress in math. 
<!--more-->

## papers

- [Nazrin](https://arxiv.org/pdf/2602.18767): Interesting idea but one I'm not sold on is valuable (a replacement for a hammer essentially)
- [STP: Self-play LLM Theorem Provers](https://arxiv.org/pdf/2502.00212): Loved this idea (a lot like bacteria and microbiomes / evolutionary bio) for math
- [Tactic Dependence Graphs](https://arxiv.org/pdf/2503.24036): Also loved this - basically, let's save off important subgraph structures and strip gunk away for future searches
- [Lean-auto](https://arxiv.org/pdf/2505.14929): Not a fan; very verbose and academic and I got lost in the sauce

## thoughts

- I like self-play but what about alignment. You need to ground their exploration in some reward and "more difficult" theorems meaning more dense/long graphs is perhaps arbitrary and a waste of our time.
- I'd like to understand how models organize these memories and when/why they get stuck in output and when it makes sense to shift over to a new context or new model entirely. Super interesting ideas here but not tractable.
- Lean is just another language at the end of the day... it's not something specific to math that is a savior for all of math. We are asking LLMs for programs and Lean requires them to make up names for tactics and theorems that are intuitive to us. theorem_X_Y_Z sucks and there's an alignment problem as I noted above. Perhaps we are asking for LLMs to clean up and efficiently prune the vast space of math already discovered. Then what low-hanging fruit (if any) remain? That's the question.
- I don't think RLHF is the answer here for alignment. I think humans have our own knowledge graphs and LLMs have their own way of organizing data. This is the natural struggle I see with LLMs. The goal is not for the teacher (LLM) to dumb down the responses forever for the students but to adaptively bring up the student's comprehension and ability over time. If a student queries the teacher about Ito's lemma N times in a similar fashion, the student is not learning and the teacher needs to mix it up and bring in different sources of inspiration that may match the student's interests OR help the student commit that to memory with quizes and other tactics. The issue is that we have an unbounded space of areas to get better in and so without stating these things in advance for contexts of queries, the LLM does not know how to get a student moving in the right direction. I worry we should not treat these LLMs as omniscient gods (as AI companies are trying to do to gobble up money) but rather as mediocre/decent teachers that know a little about a lot of things and can serve as guiding stars pointing you in the right direction and also as good research buddies to pair with when humans are not available to expand on the space (or query to know if it's been done or not). This can end up with us realizing we're all not worth sh*t, but that's okay!
- LLMs do not help people understand concepts better without understanding the person themselves which requires data BUT these companies are slimy a**holes and you should never give them this data. If LLMs knew what you know and don't know, they could raise the collective conscious of everyone but this can manipulate masses as social media currently does with similar algorithms to RLHF for keeping you wired/tied to your devices. We need to figure out with differential privacy or guarantees (HAH - never...) from these companies that they will anonymize this data or the government will get these technologies.