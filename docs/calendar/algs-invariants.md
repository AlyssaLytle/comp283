---
layout: default
title: Introducing Algorithms and Invariants
contributors: 
    - Alyssa Byrnes
    - Conor Jones
---

# Algorithms

An *algorithm* is just a series of steps that return a result. They are usually used to help you get a more optimal result. (E.g. perform the task more accurately, faster, cheaper, etc.)

## Day-to-day examples

Some common examples of algorithms you might use in your day-to-day are:

- Following a meal prep guide to help you eat healthier and save money.
- Following a routine in the gym to maximize your fitness goals.
- Choosing your class schedule to fit your preferences. 

## Anatomy of an Algorithm

<img src="/comp283/static/figs/algorithm.png" width="600"/>

An algorithm is given at least one *input*,

it performs a *series of steps*,

and it returns a *result*.

Note that an algorithm may be influenced by its environment and it may  produce side-effects which influence its environment. (I'll give an example of this soon!)

Two important properities of an algorithm: 

- it is *finite* 
- it can handle an arbitrarily large input 

## Pseudocode

Sometimes, *pseudocode* can be helpful for expressing an algorithm! 
Pseudocode looks like code, but simplified and readable.

It is not meant to run on a computer, but rather it helps you outline what your algorithm is going to look like without going too bogged down in syntax.

You can reference your pseudocode to help you write actual code!

### Example: Finding the low card in a deck

Say I want to describe an algorithm to find the lowest card in the deck of cards. The general steps are:

- Go from left to right
- Remember the lowest card you’ve seen so far and compare it to the next cards

In pseudocode, you could express it like this:

```
INPUT: deck of cards
lowest_card = first card in deck
for each card in the deck:
	if current_card < lowest_card:
		lowest_card = current_card
RETURN lowest_card
```

# LS13: Algorithms

This activity will guide you through recognizing everyday algorithms, expressing them in structured logic, and beginning to justify them like a proof.

You will be sharing these algorithms on EdStem so your classmates can interact.

## Q1: Identify an Everyday Algorithm

What’s an example of an algorithm you use in your daily life?
Think of anything with a step-by-step process, for example: picking your outfit, walking to class, choosing a YouTube video, ordering food, etc.
Write 2–3 sentences describing what you do, in plain language.


