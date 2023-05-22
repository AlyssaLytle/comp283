---
title: QuantifiersCode
theme: dracula
center: false
transition: 'none'
contributors: Alyssa Byrnes
---


<div id="content">
</div>


## What We've Learned: Bringing It Back to Coding
<div id="content">


</div>


## Python
<div id="content">

### What is Python?

Python is one of the most popular coding languages.


</div>


## Methods
<div id="content">

### What is a method?

Something that recieves and input, does something to it, and gives an output.

>A function is a type of method!

### Example

>$f(x) = x + 2$ is a function

In python it looks like:

    def f(x):
        return x + 2
        
A method defines an algorithm.

"return" exits the program and outputs $x+2$


</div>


## Common Objects in Python
<div id="content">
- Integer: A Integer
- List: An ordered list of objects
    - $[1,2,3]$, $[\textrm{``apples''}, 1, \texttt{True}]$
    - This is a type of *tuple*!
- Boolean: Something that is either $\texttt{True}$ or $\texttt{False}$
    - A *proposition* is a boolean.
    - A *preposition* given an input is a boolean.
    

</div>


## Pseudocode
<div id="content">

We sometimes use **pseudocode** to practice writing out methods/algorithms.

Pseudocode is something that looks like code, but wouldn't actually run in any language. It's a good way to write out algorithms without having to worry about syntax.

### Example

    f:
        input: integer x
        
        #We can add comments this way. A comment doesn't execute. It's for you to read when you look at your code.
        
        return x + 2
    

</div>


## Conditionals
<div id="content">

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


</div>


## Loops
<div id="content">

A **loop** lets you look at every element in a list and do something each time.

### Example - For Loop

    example:
        for x in [1,2,3,4]:
            print x + 5

>Prints out $6,7,8,9$

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


