+++
author = "Someone"
title = "repetition"
date = "2025-03-01"
description = "spaced repetition"
math = true
+++

Review of online, open-sourced means of learning.

<!--more-->

## personal scratchpad

Some thoughts.
- Self-organizing knowledge into clusters that students are interested in learning would be epic. I wonder if the self-organizing research was a dead end because I don't see much talk of it - only embedding clustering.
- Maintaining these clusters as they evolve over time
- Recommending problems to users that are difficult works up until the research level and then you might have problems not tied to one cluster in particular
- Maybe we could organize problems as fuzzy / hierarchical clusters and the number of memberships contributes to its ELO (i.e. combining calculus with probability with time = stochastic calculus which is hard)
- A savy student might want to learn a cluster that overarches the most # of problems. For instance, developing mathematical maturity and programming ability might allow you to tackle most problems posed on the internet. They should realize that this cluster has many tentacles but if they learn the hardest subproblems (sampling the branches), then they can do this quite well
- Here's the dilemma that we need to figure out: students at the beginning need reinforcement (and learning is hindered initially by memorization - recalling facts, tactics, etc.), but after some time, learning transpires more so to a student's discipline and problem-solving abilities - combining various tactics together.
- For me learning comp math, the learning process was 1) tactics training (picking a problem type - induction, dynamic programming, geometry, etc.) and actively recalling the tactic in the problem, then when that tactic crystallizes into longer term memory, pivoting to another tactic until a base set of tactics are learned and you can sample problems that combine them together.
- How can I organize the database easily to have these categories, ELO ratings, etc.?

Some difficult questions.
a) Time-series / what representation for a student's knowledge (forgetting), concepts recalled, etc.
b) Hierarchical tagging of math problems (i.e. calculus, integration, etc.) and are ELOs tied to whole problem or just subsection of problem
c) Considering multiple users and how to supplement cold starts better (i.e. user similarity)
d) Ideally, I poach the artofproblemsolving contest data, autotag everything w/ LLM help
e) What to do with incorrect problem statements or missing solutions? Maybe RL w/ LLMs for right solutions??
f) Representing solutions? In math, there is often a visual one, a simple one, and a convoluted crank one. 
g) When to recommend reading, different sources, etc. for math?
h) What about topic drift - i.e. this problem features concepts C1 and C2 but later on we add C3 and this problem uses it?
i) What format is best to allow the user to learn - code, text, multiple choice, free response, etc.?
j) **Think**: In reality, it would be best to create a problem market - i.e. figure out which skills / things people need (as a function of quantity and money). If customers are paying for a niche skill at rating x or higher, then a user might gear their training towards that with the possibility that no one cares about that skill by the time they master it. Ideally, companies and customers would open-source their problems with a dollar tag associated with problems (and some vote). Then problem-solvers have financial incentive to help them out and both parties win.


## competitor analysis

LLM Solvers
- There are a zillion links to LLM solvers for math problems
- I really think people are overlooking human intelligence and not thinking creatively about how we could combine the two together or just improve our own education
- There's a huge gap in products because it's so F*#* hard to create something useful
- Math requires careful meditation which really means no screens for extended periods of time
- Pricing varies; curious what skills people will pay for in future...

KhanAcademy
- Great videos. Simple, explicative, and visual explanations of content
- Forums beneath videos for q&a (sorting as well); transcripts for videos
- Primarily multiple choice w/ one answer right; lots of hints, explanations of each answer
- Content revolves around existing topics taught (i.e. middle school, high school courses)
- I'm not a fan. Seems to easy and rewards driven to actually help you become a problem solver
- Nonprofit; supported by donors/companies

AoPSOnline
- Community forums post difficult problems; organize by category (contest, school, etc.); forums for discussing problems with tex support
- Contest courses are like $400+/month... ($34/lesson)
- Wikis are pretty darn extensive: https://artofproblemsolving.com/wiki/index.php/Resources_for_mathematics_competitions
- Full of books, articles, forum posts, etc. for getting better at contest problems
- Difficult to parse because solution isn't always provided... I see lots of hints, etc. but no guarantees users actually arrived at solution vs half-assed attempts
- To be fair, olympiad contests literally revolve around grades being given by rockstar professors and no software w/ discussions about problem correctness...
- So far, this is the best resource to getting stronger but it's daunting for beginners and users cannot see history of progress / solves (likely to forget concepts unknowingly)
- Similar to Leetcode pay-structure (but all problems are free); courses/camps are $$

Codeforces
- Similar to AoPSOnline - there is a problem set page w/ tags & num users who solved and blog/forum posts by users
- Unlike AoPSOnline, there is a rating tag that is sometimes unfilled
- There is an awesome catalog section like the AoPS wiki but more thorough broken down by various tags
- There is a contest section
- This is a pretty epic site actually. Maybe I need to spend some time here thinking about what they do before trying to recreate myself
- They've got rating history, git graph of submissions, but again problem recommendations are like non-existent which probably allows individual tactics to atrophy without you even knowing it
- Languages supported: c++, c, c#, python, java, js, d, go, haskell, kotlin, ocaml, delphi, pascal, perl, php, rust, ruby, scala  
- Topics supported: k-sat, algorithms (graph & math heavy), again generic "math" tag...
- Everything is free

LeetCode
- Explore page features courses on skills/concepts users might want to acquire - data structures, sql, system design, etc. but they cost like $80+
- Explore has non-paid courses but they're often paywalled beyond a certain section for subscribers only...
- Content in explore seems like cookie cutter stuff of lecture/video, LLM-generated descriptions, and problems/solutions for you to try (i.e. what codeforces/aops/mit offer for free)
- Problems page is fairly thorough. There are company tags, organized problem lists for topics (like interview 150, sql 50, etc.)
- There are concept tags (string, hash table, etc.), acceptance (0, 100), solution, difficulty
- Contest page like codeforces
- Discuss section; usually just snobbery around total comp/interview questions...
- Paywalled p-sets for companies (google, uber, etc.)
- Languages supported: bash, sql, python, js, java, c++, c, c#, rust, go, racket, typescript, swift, ruby, scala, kotlin, erlang, elixir, dart
- Topics supported: concurrency, shell, database, design, usual algorithm problems
- Premium: 13.25/month (full year); 35/month; courses are not included (~$80/course)

MIT OpenCourseWare
- Most breadth and depth of content (aside from maybe codeforces for data structures & aops for math contests)
- Main issue: compiling answers / lack of autograders for basically all courses; some solutions exist but they're text and sparse
- Without skin in the game (i.e. grade, competition, etc.) and validation, it's very hard (if not possible) to make this your primary source of education
- Videos and problems are like the highest quality for difficult courses
- Everything is free

Wolfram
- Features AI-generated practice problems & answers (number theory, algebra, calculus, linear algebra, statistics)
- No proof-based problems; at the level of very early university / high school
- It's really just a symbolic calculator and graph tool. I don't care about it at all tbh..
- Step-by-step solutions $5-12/month

Anki
- Focused on memorization, but useful again for spaced repetition (I think memorization is required for being the best problem solver)
- Primarily language-focused decks available - french, japanense, korean, etc.
- Free

In summary, I think MIT, Codeforces, & LeetCode are the strongest competitors for the unrelenting student interested in solving all problems out there and getting better every day.

The other "competitors" are really focused on grade-school / very diluted and easy content. 

## lit review

[^1]
- "...suggests that spacing will benefit learning when the first learning episode has been forgotten"
- "If a person wishes to retain information for several years, a delayed review of at least several months seems likely to produce a highly favorable return on a time investment"

- How do you decide how long to study particular material before forgetting?
- Who in the world did this study and with what material? Is it dependent on the material chosen?
- What about problem solving in general and not routine memorization?

[^2]
- "The experiment was a 2 (trial type: read or drill) x 3 (learning trial spacing: wide medium, or narrow) x 2 (fill-in term during learning: variable or constant) x 2 (fill-in term during posttest: variable or constant) within-subjects design."
- Drills are three times more effective than reading
- Wider spacing leading to worse learning performance but better posttest performance was not supported by data
- This wasn't a very conclusive study (which maybe is a good thing). I am still unsure what wide medium & narrow are concretely

[^3]
- Spacing effect: periodic, spaced review of content improves long-term retention
- Review scheduling: deciding which content to present to a student at any given time
- Probability of recall is roughly $1/\exp\{\text{difficulty}\cdot\times\text{ time since last reviewed } / \text{ number of attempts}\}$
- That^ is Ebbinghaus' exponential forgetting curve. Basically, as difficulty increases or procrastination persists, your chance of recalling the given fact drops
- It's exponential like the concept of compound interest; so keep up the work no matter what
- I like this a lot. Maybe we calibrate the item difficulty as the ELO???
- If I want to learn concepts $\{c_1, c_2,\dots , c_n\}$, then it boils down to studying concepts proportional to ELO scores (works w/ skill systems like climbing or chess but not memorization where ELO is roughly uniform)
- Rasch model (and generalized power law ones) seem overly complex & parametric
- Kind of lame model; why RL dude... like seriously?
- Good works cited

[^4]
- Spaced repetition is like the dampening of a wave where the height of a wave represents the chance of recall
- 

[^5]
- asdf

[^6]
- asdf


## references
- [^1]: [Spacing effects in learning](https://files.eric.ed.gov/fulltext/ED505660.pdf)
- [^2]: [Spacing and Statistics](https://gwern.net/doc/psychology/spaced-repetition/2015-maas.pdf)
- [^3]: [Deep RL Learning](https://siddharth.io/files/deep-tutor.pdf)
- [^4]: [Spaced Repetition](https://gwern.net/spaced-repetition)
- [^5]: [Bandit Learning](https://people.umass.edu/~andrewlan/papers/16edm-bandits.pdf)
- [^6]: [Faster Teaching](https://cocosci.princeton.edu/tom/papers/fasterteaching.pdf)