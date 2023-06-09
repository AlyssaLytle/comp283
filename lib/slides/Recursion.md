---
title: Recursion
theme: dracula
center: false
transition: 'none'
contributors: Alyssa Byrnes
---


## Recursion
<div id="content">

There is still one type of proof we need to cover... but first we're going to take a little bit of a detour.

It is helpful to understand **recursion** before we move on to the next kind of proof!


</div>


## What is recursion?
<div id="content">

**Recursion** is the idea of solving a problem by breaking it into smaller problems.

### Example - Factorials:

- Another familiar function we know is $n! = n \cdot (n-1) \cdot \ldots \cdot 2 \cdot 1$
- We can rewrite this as $n! = n\cdot (n-1)!$.
- This is a **recursive** definition because we are computing $n!$ by first computing $(n-1)!$.


</div>

## Recursion in Coding
<div id="content">

Here is an example of what recursion would look like in a programming language like Python.

Say we want to write a program that returns $n!$.

    Def factorial:
        input: natural number n
        if n == 0: #base case
            return 1
        else: #recursive rule
            return n * factorial(n-1) 
        

</div>


## Why do we use recursion?
<div id="content">

- Breaking a problem into smaller pieces can make it easier to solve.
- Breaking a problem into smaller pieaces can also make it easier to reason about, making it easier to prove properties about it! 
- Many programming languages heavily rely on recursive definitions (haskell, racket, scheme, etc.)
- Other programming languages support it by letting a function call itself. 


</div>


## Defining recursion
<div id="content">

We just gave an example of a function that is defined recursively.

You can also recursively define sets, relations, tuples, lists, sequences, etc...

There are two main parts of any recursive definition:

1. The base case: the initial element/value of what you're trying to define
2. The recursive rule: tells you how to generate the next element/value given previous ones.

### Example: Factorials

1. The base case: $0! = 1$
2. The recursive rule: $n! = n \cdot (n-1)!$


</div>



## The Fibonacci numbers
<div id="content">

- The Fibonacci numbers are a very famous sequence of numbers that are defined via a recursive function.

1. The base case: $F(0) = 0, F(1) = 1$
2. Recursive rule: For $n < 1$, $F(n) = F(n-1) + F(n-2)$.

</div>


## Other Example - Powersets: 

<div id="content">

- We can define powersets recursively:
- $\mathscr{P}(X + \{c\} ) = \mathscr{P}(X) \cup (\mathscr{P}(X) + \{c\})$
- E.g. $\mathscr{P}(\{1,2,3\}) = \mathscr{P}(\{1,2\} + \{3\}) = \mathscr{P}(\{1,2\}) \cup (\mathscr{P}(\{1,2\}) + \{3\})$
- This is essentially saying we can build a powerset by unioning two smaller sets. We are building something by combining two smaller things. That's what makes this definition **recursive**.


### Definition

1. The base case: $\mathscr{P}(\{ \}) = \{\}$
2. The recursive rule: $\mathscr{P}(X + \{c\}) = \mathscr{P}(X) \cup (\mathscr{P}(X) + \{c\})$

</div>


## Defining Functions and Methods Recursively
<div id="content">

I want to define a method $copy$ such that for all $n \in \mathbb{N}$, $copy(n)=n$

For this, we are going to use the fact that $n = 1 \cdot n = 1 + 1 + \ldots + 1$, $n$ times.

1. The base case: $copy(0) = 0$
2. Recursive rule: For $n<0$, $copy(n) = 1 + copy(n-1)$


</div>


## Defining Lists Recursively
<div id="content">

- We are going to give an example of how we can define a list and some functions on a list recursively
- Say all elements of our list are in set $A$
- The set of all possible lists $L$ can be defined as $L = \bigcup_{k\geq0}A^k$ 
(Aka all possible permutations of length $k \geq 0$ of the elements in $A$.)
- We can also define this recursively.

1. Base case: Empty list $\langle ~ \rangle$
2. Recursive rule: For any element $a \in A$ and all lists $l \in L$, $cons(a,l)$ is a list in $L$.

- Basically, $cons(a,l)$ takes $a$ and attaches it to list $l$
- You can think of "$cons$" as short for "constructor".

</div>


## Defining Lists Recursively
<div id="content">

1. Base case: Empty list $\langle ~ \rangle$

2. Recursive rule: For any element $a \in A$ and all lists $l \in L$, $cons(a,l)$ is a list in $L$.

- Basically, $cons(a,l)$ takes $a$ and attaches it to list $l$


### Examples
- $\langle b \rangle = cons(b, \langle ~ \rangle)$
- $\langle a, b \rangle = cons(a, cons(b, \langle ~ \rangle))$
- $\langle a, b, c \rangle = cons(a, cons(b, cons(c, \langle ~ \rangle)))$

</div>


## Useful Partial Functions
<div id="content">

- $head(cons( a,l )) = a$
- $tail(cons( a,l )) = l$
- Note that $head$ returns an element and $tail$ returns a list!

### Examples

- $\langle a, b, c \rangle = cons(a, cons(b, cons(c, \langle ~ \rangle)))$
- $head(cons(a, cons(b, cons(c, \langle ~ \rangle)))) = a$
- $tail(cons(a, cons(b, cons(c, \langle ~ \rangle)))) = cons(b, cons(c, \langle ~ \rangle)) = \langle b, c \rangle$

</div>


## Strings and Languages
<div id="content">

- Strings and Languages are likely going to come up later in your computer science education, so it's good to be familiar with these definitions!
- A **string** is a list containing characters from a given **alphabet** $\Sigma$
- The set of all possible strings that can be made from an alphabet is $\Sigma^*$
- A **language** is a set of strings $L \subseteq \Sigma^*$

</div>


