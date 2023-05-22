---
title: Quantifiers
theme: dracula
center: false
transition: 'none'
contributors: Alyssa Byrnes
---


<div id="content">

</div>


## Quantifiers (Predicate Logic)
<div id="content">
### Chapter 4 in book


</div>


## Predicate Definition
<div id="content">
 A **predicate** is a
function that maps each possible input to either $\texttt{True}$ or $\texttt{False}$. 
 
### Example 

>Here are two predicates each taking their input $x$ from a set of days, $D$:

>$p(x) =$ "It rained in the morning on day $x$," and

>$q(x) =$ "I walked to campus on day $x$."

>We can combine these to write the statement "If it did not rain in the morning
on day $x$, then I walked to campus on day $x$" as $\neg p(x) \implies q(x)$ \footnote{{In the textbook, $\implies$ is written as $\rightarrow$ and $\neg x$ is written as $\bar{x}$.}} 


</div>


## Motivation
<div id="content">
 We are going to introduce the next concept with an example...

### Example 

>Let's say that my previous statement only applies on Mondays, Wednesdays, and Fridays. 

>How can we say this using what we already learned?

>$(\neg p($Mon$) \implies q($Mon$)) \land (\neg p($Wed$) \implies q($Wed$)) \land (\neg p($Fri$) \implies q($Fri$))$

>We can also express this using set notation.
>Say $D= \{$Mon, Wed, Fri$\}$.

>Similar to how you use a summation $\sum$ for a sequence of additions, we can use the big and $\bigwedge$ to represent a sequence of ands.

>$\bigwedge\limits_{d \in D} (\neg p(d) \implies q(d))$


</div>


## Motivation Continued - Universal Quantifier
<div id="content">

We can also write this using a **quantifier**.

The "for all" quantifier, denoted $\forall$, is used to reason about all elements of a set.
 
### Example Continued

We already showed that for $D= \{$Mon, Wed, Fri$\}$,

$(\neg p(\textrm{Mon}) \implies q(\textrm{Mon})) \land (\neg p(\textrm{Wed}) \implies q(\textrm{Wed})) \land (\neg p(\textrm{Fri}) \implies q(\textrm{Fri}))$

$\equiv \bigwedge\limits_{d \in D} (\neg p(d) \implies q(d))$


 There is another way we can say this.

$\forall d \in D, (\neg p(d) \implies q(d))$.


</div>


## Existential Quantifier
<div id="content">

We can do something similar with "or" statements. For this we will introduce another quantifier.

The "there exists" quantifier, denoted $\exists$, is used to reason about at least one element of a set.
 
### Example 

>Now let's say that for at least one day of Monday, Wednesday and Friday, if it's not raining on day $d$, then I walk to campus on day $d$.

>This can be written using logical or, big or, or with the "there exists" quantifier.

>$(\neg p(\textrm{Mon}) \implies q(\textrm{Mon})) \lor (\neg p(\textrm{Wed}) \implies q(\textrm{Wed})) \lor (\neg p(\textrm{Fri}) \implies q(\textrm{Fri}))$

>$\equiv \bigvee\limits_{d \in D} (\neg p(d) \implies q(d))$

>$\equiv \exists d \in D, (\neg p(d) \implies q(d))$


</div>


## Free and Bounded Variables
<div id="content">

 A variable specified with a specified domain is a **bounded variable**. 
 
 A variable without a specified domain is a **free variable**.
 
### Example 

>In the preposition $\forall x \in \mathbb{Z}, f(x,y)$,

>$x$ is a bounded variable and $y$ is a free variable.
 
### Example 

>For
$\sum\limits_{k=0}^{10} (k+n)$,

>$k$ is a bounded variable and $n$ is a free variable.



</div>


## Negation and Inference
<div id="content">

Since ‘for all’ is a big ‘and,’ and ‘exists’ is a big ‘or,’ de Morgan’s laws say that the
negation of one is the other (with its statement negated.) That is:

$\neg(\forall x, p(x)) \equiv \exists x, \neg p(x)$ and

$\neg(\exists x, p(x)) \equiv \forall x, \neg p(x)$


 Why are these true?

### Example 

>$\neg(\forall x, p(x))$ in English translates to "$p(x)$ does not hold for all $x$".

>This is equivalent to saying, "There exists an $x$ where $p(x)$ does not hold", or $\exists x, \neg p(x)$.

>Similarly, 
$\neg(\exists x, p(x))$ in English translates to "There does not exist $x$ such that $p(x)$ holds. 

>This is equivalent to saying "For all $x$, $p(x)$ does not hold", or $\forall x, \neg p(x)$.



</div>


## Nested Quantifiers
<div id="content">
 
### Example 
>This example is to help you get some practice with nested quantifiers and to understand that the order of them matters.

>Say that $loves(x,y)$ is true iff person $x$ loves person $y$.

>$\forall_{e \in P}$ $\exists_{s \in P}, loves(e,s)$ translates to "Everybody loves somebody."

>$\exists_{s \in P}$ $\forall_{e \in P}, loves(e,s)$ translates to "There is somebody that everybody loves."


</div>


## Other Notation
<div id="content">
Here are some other ways we can write things.

If we are talking about pairs of distinct integers, $i, j \in [1..n]$ with $i < j$,
we may even write $\forall_{1\leq i < j \leq n}$ or $\exists_{1\leq i < j \leq n}$.

If we are talking about elements $x$ and $y$ that are members of the same set $S$, we can write
$\forall_{x,y \in S}$ or $\exists_{x,y \in S}$. 


</div>


## In Class Assignment
<div id="content">
- I will pass out papers explaining the assignment. 
- Everyone should take ***two*** copies. 
- Fill out one copy of this worksheet. Write your name on the top and bring it to the front.
- You can work in groups/pairs!
- **You will not be graded for correctness--just participation!!!**
- We will then go over the answers. The second copy is for you to fill out and keep.


</div>


