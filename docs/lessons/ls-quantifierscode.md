---
layout: default
title: QuantifiersCode
contributors: Alyssa Byrnes
---

## What We've Learned: Bringing It Back to Coding

## Python

### What is Python?

Python is one of the most popular coding languages.

## Methods

### What is a method?

Something that recieves and input, does something to it, and gives an output.

>A function is a type of method!

### Example

>$$f(x) = x + 2$$ is a function

In python it looks like:

    def f(x):
        return x + 2
        
A method defines an algorithm.

"return" exits the program and outputs $$x+2$$

## Common Objects in Python
- Integer: A Integer
- List: An ordered list of objects
    - $$[1,2,3]$$, $$[\textrm{``apples''}, 1, \texttt{True}]$$
    - This is a type of *tuple*!
- Boolean: Something that is either $$\texttt{True}$$ or $$\texttt{False}$$
    - A *proposition* is a boolean.
    - A *preposition* given an input is a boolean.
    
## Pseudocode

We sometimes use **pseudocode** to practice writing out methods/algorithms.

Pseudocode is something that looks like code, but wouldn't actually run in any language. It's a good way to write out algorithms without having to worry about syntax.

### Example

    f:
        input: integer x
        
        #We can add comments this way. A comment doesn't execute. It's for you to read when you look at your code.
        
        return x + 2
    
## Conditionals

A **conditional** checks some condition (expressed as a boolean) and uses it to decide what the program should do.

### Example

    example:
        input: boolean x
        
        if x: #Checks if x == True
            y = x + 1
        else:
            y = x + 2
        return y
        
### Example 2

    example:
        input: boolean x
    
        if !x: #Checks if x == False
            y = x + 2
        else:
            y = x + 1
        return y

## Loops

A **loop** lets you look at every element in a list and do something each time.

### Example - For Loop

    example:
        for x in [1,2,3,4]:
            print x + 5

>Prints out $$6,7,8,9$$

### Example - While Loop

    example:
        x = 1
        while x < 5:
            print x + 5
            x = x + 1

>Also prints out $$6,7,8,9$$

## Coding Existentials

### We are going to practice writing pseudocode for our existentials




## Exists

Let's say we have a list of booleans: $$P = [p1,p2,p3,p4]$$.

We want to check $$\exists p \in P, p$$.

We want a method that returns $$\texttt{True}$$ if at least one element in $$P$$ is $$\texttt{True}$$ and returns $$\texttt{False}$$ otherwise.

    example:
        input: list P
        for x in P:
            if x:
                return True
        #Loop exited
        return False

