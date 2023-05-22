---
title: Coding with Quantifiers
theme: dracula
center: false
transition: 'none'
contributors: Alyssa Byrnes
---


## Basic Concepts of Coding

## Functions
<div id="content">

### What is a function?

Something that recieves and input, does something to it, and gives an output.


### Example

>$f(x) = x + 2$ is a function

In Python it looks like:

    def f(x):
        return x + 2


"return" exits the program and outputs $x+2$


</div>


## Common Objects in Python
<div id="content">
- Integer: A Integer ($\mathbb{Z}$)
- List: An *ordered* set of objects
    - $[1,2,3]$, $[\textrm{``apples''}, 1, \texttt{True}]$
- Boolean: Something that is either $\texttt{True}$ or $\texttt{False}$
    - A *proposition* is a boolean.
    - A *predicate* given an input is a boolean.

</div>



## Conditionals
<div id="content">

A **conditional** checks some condition (expressed as a boolean) and uses it to decide what the program should do.

### Example

    example:
        input: boolean x
        
        if x: 
            y = x + 1
        else:
            y = x + 2
        return y

</div>

## Conditionals
<div id="content">

### Example 2

    example:
        input: boolean x
    
        if not x: 
            y = x + 2
        else:
            y = x + 1
        return y


</div>






## Loops
<div id="content">

A **loop** lets you look at every element in a list and do something each time.

### Example - For Loop

    example:
        for x in [1,2,3,4]:
            print x + 5

>Prints out $6,7,8,9$

</div>

## Loops
<div id="content">

### Example - While Loop

    example:
        x = 1
        while x < 5:
            print x + 5
            x = x + 1

>Also prints out $6,7,8,9$


</div>



## Coding Existentials
<div id="content">

### We are going to practice writing pseudocode for our existentials


</div>


<!-- 



## Exists
<div id="content">

Let's say we have a list of booleans: $P = [p1,p2,p3,p4]$.

We want to check $\exists p \in P, p$.

We want a method that returns $\texttt{True}$ if at least one element in $P$ is $\texttt{True}$ and returns $\texttt{False}$ otherwise.



</div>



## Exists
<div id="content">

Let's say we have a list of booleans: $P = [p1,p2,p3,p4]$.

We want to check $\exists p \in P, p$.

We want a method that returns $\texttt{True}$ if at least one element in $P$ is $\texttt{True}$ and returns $\texttt{False}$ otherwise.

    example:
        input: list P
        for x in P:
            if x:
                return True
        #Loop exited
        return False


</div>






## Forall
<div id="content">

Let's say we have a list of booleans: $P = [p1,p2,p3,p4]$.

We want to check $\forall p \in P, p$.

We want a method that returns $\texttt{True}$ if every element in $P$ is $\texttt{True}$ and returns $\texttt{False}$ otherwise.

Remember: $\forall p \in P, p \equiv \neg \exists p \in P, \neg P$.

So, we can also think of it as a method that returns $\texttt{False}$ if at least one element in $P$ is $\texttt{False}$ and returns $\texttt{True}$ otherwise.




</div>






## Forall
<div id="content">

Let's say we have a list of booleans: `P = [p1,p2,p3,p4]`.

We want to check $\forall p \in P, p$.

We want a method that returns $\texttt{True}$ if every element in $P$ is $\texttt{True}$ and returns $\texttt{False}$ otherwise.

Remember: $\forall p \in P, p \equiv \neg \exists p \in P, \neg P$.

So, we can also think of it as a method that returns $\texttt{False}$ if at least one element in $P$ is $\texttt{False}$ and returns $\texttt{True}$ otherwise.


</div> -->






