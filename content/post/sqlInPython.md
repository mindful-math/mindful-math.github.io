+++
author = "Someone"
title = "sql"
date = "2024-01-06"
description = "sqlmeql"
math = true
+++

Translating SQL expressions in Python; motivated by [this](https://cs61a.org/study-guide/sql/). 
<!--more-->

- [data definitions](#data-definitions)
- [aggregate functions](#aggregate-functions)

## data definitions

A database in base Python would look something like the following below. Structuring a legitimate math database (not the throwaway below) would be a interesting undertaking and I bet attempts have been made in the study of [proof assistants](https://en.wikipedia.org/wiki/Proof_assistant). 

```python
QuickMaths: dict[str, Iterable[dict]] = {
    "definition": [
        {
            "name": str,
            "statement": str,
            "field": str
        }
    ]
    "theorem": [
        {
            "creator": str,
            "statement": str,
            "proof": str, 
            "date": int,
            "name": str,
            "field": str
        }
    ],
    .
    .
    .
}
```

## aggregate functions

Aggregate functions are easy enough to define by Python's built-in functions. 



