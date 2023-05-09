---
layout: default
title: Propositional Logic
contributors: Alyssa Byrnes
---

# Propositional Logic


## Learning Objectives

-  Express statements in symbolic form, using the logic operations of negation, and, inclusive or, implies, if and only if (iff), and exclusive or (and their symbols:  $$  \neg, \land, \lor, \implies, \iff,  $$   and  $$ \oplus $$ ) to express statements without ambiguity.
-  Distinguish between inclusive and exclusive 'or'.
-  Create truth tables in order to recognize tautologies and logically equivalent expressions, including De Morgan’s rules and conditional expressions.
-  Meet properties of logic operations and rules of logical inference, both of which help us rewrite expressions while preserving their truth values.
-  Encounter Boolean algebra and circuit notations for the same logical expressions.
-  Demonstrate how to use at least one of these methods to solve a logic puzzle.

## Propositions and Basic Operations
A *proposition* is a sentence to which one and only one of the terms  $$ \texttt{True} $$   or  $$ \texttt{False} $$  can be applied. 

Which of the following are propositions?

-  We are currently in Chapel Hill. - Yes
-   $$ 1 + 1 = 2 $$  - Yes
-   $$ 2 + x = 4 $$  - No
-  It is hot outside. - No



## Negation

A *Truth Table* for negation would look like the following: 

 $$ \begin{array}{|c|c|}
\hline
p  & \neg p  \\
\hline
T & F \\
F & T \\
\hline
\end{array} $$ 

What this is saying is: "When  $$ p $$  is  $$ \texttt{True} $$ ,  $$ \neg p $$  is  $$ \texttt{False} $$ , and when  $$ p $$  is  $$ \texttt{False} $$ ,  $$ \neg p $$  is  $$ \texttt{True}$$.''

Here is an example of a negated proposition.

-   $$ p $$ : "Today is Monday.''
-   $$ \neg p $$ : "Today is not Monday.'' 
-  *ALTERNATIVELY:*  $$ \neg p $$ : "It is not the case that today is Monday.''


## Conjunction

A Truth Table for conjunction would look like the following:
 $$ \begin{array}{|c|c|c|}
\hline
p  & q & p \land q  \\
\hline
T & T & T \\
T & F & F \\
F & T & F \\
F & F & F \\
\hline
\end{array} $$ 

Here is an example of conjunction.

-   $$ p $$ : "It is sunny today.''
-   $$ q $$ : "It is Monday.''
-   $$ p \land q $$ : "It is sunny today and today is Monday.''

The conjunction ( $$ p \land q $$ ) is  $$ \texttt{True} $$  on sunny Mondays, but it is  $$ \texttt{False} $$  on any non-sunny day ( $$ p $$  is  $$ \texttt{False} $$ ), and it is  $$ \texttt{False} $$  on any day that is not Monday ( $$ q $$  is  $$ \texttt{False} $$ ).


## Disjunction

A Truth Table for disjunction would look like the following:
 $$ \begin{array}{|c|c|c|}
\hline
p  & q & p \lor q  \\
\hline
T & T & T \\
T & F & T \\
F & T & T \\
F & F & F \\
\hline
\end{array} $$ 

Here is an example of disjunction.

-   $$ p $$ : "It is sunny today.''
-   $$ q $$ : "It is Monday.''
-   $$ p \lor q $$ : "It is sunny today or today is Monday.''

The disjunction ( $$ p \lor q $$ ) is  $$ \texttt{True} $$  on sunny Mondays, on any sunny day ( $$ p $$  is  $$ \texttt{True} $$ ), and on any Monday ( $$ q $$  is  $$ \texttt{True} $$ ). It is  $$ \texttt{False} $$  on any day where it is both not sunny and not Monday.


## Exclusive Or

A Truth Table for exclusive or would look like the following:
 $$ \begin{array}{|c|c|c|}
\hline
p  & q& p \oplus q  \\
\hline
T & T & F \\
T & F & T \\
F & T & T \\
F & F & F \\
\hline
\end{array} $$ 

Here is an example of exclusive or.

-   $$ p $$ : "It is sunny today.''
-   $$ q $$ : "It is Monday.''
-   $$ p \oplus q $$ : "It is sunny today or today is Monday, but not both.''

The exclusive or ( $$ p \oplus q $$ ) is  $$ \texttt{True} $$  on any sunny day ( $$ p $$  is  $$ \texttt{True} $$ ) and on any Monday ( $$ q $$  is  $$ \texttt{True} $$ ), EXCEPT for on sunny Mondays (both  $$ p $$  and  $$ q $$  are  $$ \texttt{True} $$ ). Additionally, it is  $$ \texttt{False} $$  on any day where it is both not sunny and not Monday.


## Conditionals
The *conditional statement*  $$ p \implies q $$  is False when  $$ p $$  is  $$ \texttt{True} $$  and  $$ q $$  is  $$ \texttt{False} $$ , and True otherwise.  $$ p $$  is called the hypothesis and  $$ q $$  the conclusion. This can also be called *implication*.

Some English phrases for this would be:

-  If  $$ p $$ , then  $$ q$$.
-   $$ p $$  implies  $$ q$$.
-   $$ q $$  if  $$ p$$.

A Truth Table for implication would look like the following:
 $$ \begin{array}{|c|c|c|}
\hline
p  & q & p \implies q  \\
\hline
T & T & T \\
T & F & F \\
F & T & T \\
F & F & T \\
\hline
\end{array} $$ 


Here is an example of implication.

-   $$ p $$ : "It is sunny.''
-   $$ q $$ : "I walk to campus.''
-   $$ p \implies q $$ : "If it is sunny, then I walk to campus.''

The implication ( $$ p \implies q $$ ) is  $$ \texttt{False} $$  if it is sunny and I do NOT walk to campus. Otherwise, it is  $$ \texttt{True}$$. 

If it is not sunny ( $$ p $$  is  $$ \texttt{False} $$ ) and I still walk to campus ( $$ q $$  is  $$ \texttt{True} $$ ), this implication is still  $$ \texttt{True}$$.


## Biconditionals
The *biconditional statement* ("if and only if" or "iff")  $$ p \iff q $$  is  $$ \texttt{True} $$  when  $$ p $$  and  $$ q $$  have the same truth value, and  $$ \texttt{False} $$  otherwise.

A Truth Table for implication would look like the following:
 $$ \begin{array}{|c|c|c|}
\hline
p  & q & p \iff q  \\
\hline
T & T & T \\
T & F & F \\
F & T & F \\
F & F & T \\
\hline
\end{array} $$ 





Here is an example of a biconditional.

-   $$ p $$ : "It is sunny.''
-   $$ q $$ : "I walk to campus.''
-   $$ q \iff p $$ : "I walk to campus if and only if it is sunny.''

The biconditional ( $$ p \iff q $$ ) is  $$ \texttt{True} $$  if it is sunny and I walk to campus or if it is not sunny and I don't walk to campus. Otherwise, it is  $$ \texttt{False}$$. 

Unlike the previous example, if it is not sunny ( $$ p $$  is  $$ \texttt{False} $$ ) and I still walk to campus ( $$ q $$  is  $$ \texttt{True} $$ ), this biconditional is  $$ \texttt{False}$$.


## Useful Logical Equivalences
One useful logical equivalence is *DeMorgan's Law*. It states:
 $$  $$  \neg (p \land q) \equiv \neg p \lor \neg q  $$  $$ 
 $$  $$  \neg (p \lor q) \equiv \neg p \land \neg q  $$  $$ 

Another useful equivalence is:

 $$  $$  p \implies q \equiv \neg p \lor q  $$  $$ 

## Proving Equivalences
We can *prove* the first part of DeMorgan's Law ( $$ \neg (p \land q) \equiv \neg p \lor \neg q $$ ) using a truth table.

 $$ \begin{array}{|c|c|c|c|c|c|c|}
\hline
p  & q & \neg p & \neg q & p \land q & \neg(p \land q) & \neg p \lor \neg q \\
\hline
T & T & F & F & T & F & F\\
T & F & F & T  & F & T & T\\
F & T  & T & F & F & T & T\\
F & F & T & T & F & T & T \\
\hline
\end{array} $$ 




## Other considerations + Terminology
-  Notice that a combination of propositions using operators (e.g.  $$ p \land q $$  makes a new proposition. These can also be called *compound propositions*. 
-  If two compound propositions have the same truth tables, they are considered *logically equivalent*.
    - For example, today we showed  $$ \neg (p \land q) $$  and  $$ \neg p \lor \neg q $$  are logically equivalent!
-  A compound proposition with a truth table where all the values in the last column are  $$ \texttt{True} $$  is called a *tautology*. 
    - An example of this is  $$ p \lor \neg p$$. 

 $$ \begin{array}{|c|c|c|}
\hline
p  & \neg p & p \lor \neg p  \\
\hline
T & F & T \\
F & T & T \\
\hline
\end{array} $$ 

For all values,  $$ p \lor \neg p $$  evaluates to  $$ \texttt{True} $$ !

## Translating English Sentences
To translate logic to and from English sentences, it is important to know the common phrases for the operators. 

-   $$ \neg p $$  (Negation): "not  $$ p $$ "
-   $$ p \land q $$  (Conjunction): " $$ p $$  and  $$ q $$ "
-   $$ p \lor q $$  (Disjunction): " $$ p $$  or  $$ q $$ "
-   $$ p \oplus q $$  (Exclusive Or): " $$ p $$  xor  $$ q $$ "; " $$ p $$  or  $$ q $$ , but not both"
-   $$ p \implies q $$  (Conditional/Implication): " $$ p $$  implies  $$ q $$ "; "if  $$ p $$  then  $$ q $$ "; " $$ q $$  if  $$ p $$ "
-   $$ p \iff q $$  or  $$ p $$  iff  $$ q $$  (Biconditional): " $$ p $$  if and only if  $$ q $$ "

### Example
Here's an example of breaking up an English language sentence.

Start with the sentence: "You cannot ride the roller coaster if you are under 4 feet tall.''

Then, you break your sentence to the smallest propositions possible.


 $$ a $$  = "You can ride the roller coaster''

 $$ b $$  = "you are under 4 feet tall''

Now your sentence is: Not  $$ a $$  if  $$ b$$.


Here's an example of breaking up an English language sentence.

Start with the sentence: "You cannot ride the roller coaster if you are under 4 feet tall.''

Then, you break your sentence to the smallest propositions possible.

 $$ a $$  = "You can ride the roller coaster''

 $$ b $$  = "you are under 4 feet tall''

Now your sentence is: Not  $$ a $$  if  $$ b$$.

So you know you can write it as:  $$ b \implies \neg a$$.



### Pro Tip:

- If it doesn't directly match any of the phrases listed, use truth tables to see what it matches.
- Sometimes it takes a little experimenting/practice

## Using Logic For Problem Solving
### Knights and Knaves (Raymond Smullyan)
On an island, every inhabitant is a knight who always tells the truth, or a knave who always lies. You meet three inhabitants, Alice, Bob, and Chris.

- Alice says: Bob is a knave or Chris is a knight.
- Bob says: Alice is a knight if, and only if, Chris is a knave.

Can you determine uniquely what each of Alice, Bob, and Chris are?

1. Define convenient variables for propositions.
2. Transform what they say into statements that *always* should evaluate to  $$ \texttt{True}$$. These are the rules of our world.
3. Make a truth table – With 3 people, we have  $$ 2^3 $$  rows
4. Check if a unique row makes both statements true. 

### 1. Define convenient variables for propositions.

 $$ A = $$  "Alice is a knight",  $$ B = $$  "Bob is a knight", $$ C= $$  "Chris is a knight"

 $$ \neg A = $$  "Alice is a knave",  $$ \neg B = $$  "Bob is a knave", $$ \neg C= $$  "Chris is a knave"

### 2. Transform what they say into statements that *always* should evaluate to  $$ \texttt{True}$$. These are the rules of our world.

- Alice says: Bob is a knave or Chris is a knight.
- Bob says: Alice is a knight if, and only if, Chris is a knave.

Propositions:  $$ \{A = $$  "Alice is a knight",  $$ B = $$  "Bob is a knight", $$ C= $$  "Chris is a knight",
 $$ \neg A = $$  "Alice is a knave",  $$ \neg B = $$  "Bob is a knave", $$ \neg C= $$  "Chris is a knave"\}

- Alice says:  $$ \neg B \lor C $$ 
- Bob says:  $$ A \iff \neg C $$ 

You might be inclined to make these statements your rules of the world, but these rules are only true if Alice and Bob are telling the truth (aka they are knights). 

-  $$ A \implies (\neg B \lor C) $$   $$ \leftarrow $$  This holds whether or not Alice is a liar.
-  $$ B \implies (A \iff \neg C) $$   $$ \leftarrow $$  This holds whether or not Bob is a liar.

### 3. Make a truth table

Propositions:  $$ \{A = $$  "Alice is a knight",  $$ B = $$  "Bob is a knight", $$ C= $$  "Chris is a knight",
 $$ \neg A = $$  "Alice is a knave",  $$ \neg B = $$  "Bob is a knave", $$ \neg C= $$  "Chris is a knave"\}

Rules of the World:  $$ A \implies (\neg B \lor C) $$  and  $$ B \implies (A \iff \neg C) $$  

 $$ \begin{array}{|c|c|c|c|c|}
\hline
A & B & C &  A \implies (\neg B \lor C) & B \implies (A \iff \neg C) \\
\hline
T & T & T & T & F\\
T & T & F & F & T\\
\color{blue}T & \color{blue}F & \color{blue}T & \color{blue}T &\color{blue}T\\
\color{blue}T & \color{blue}F & \color{blue}F &\color{blue} T &\color{blue}T\\ 
\color{blue}F & \color{blue}T & \color{blue}T &  \color{blue}T &\color{blue}T\\
F & T & F & T &F\\
\color{blue}F & \color{blue}F & \color{blue}T & \color{blue}T &\color{blue}T\\
\color{blue}F & \color{blue}F & \color{blue}F & \color{blue}T &\color{blue}T\\
\hline
\end{array} $$ 

All of the values in blue are assignments that could work!


**Let's test one of these!**

### Testing Our Solution... 
 $$ A = T, B = F, C = T $$ 

So, Alice is a knight, Bob is a knave, and Chris is a knight.

- Alice says: Bob is a knave or Chris is a knight.
    -  $$ A \implies (\neg B \lor C) $$  
    plug in the truth values...
    -  $$ T \implies (\neg(F) \lor T) $$  evaluates to True!

- Bob says: Alice is a knight if, and only if, Chris is a knave. 
    -  $$ B \implies (A \iff \neg C) $$ 
    plug in the truth values...
    -  $$ F \implies (T \iff \neg T) $$ evaluates to True!

Both of our rules hold in this world with these assignments, so we know that this solution works!

### Why this isn't a good problem... 

This problem isn't explicit enough, so we found ourselves making an assumption.

When we solved it, we assumed that if someone is lying, they don't actually know whether or not what they are saying is the truth, so their claim could either be true or false. This is why we were able to use implication.

- Alice says: Bob is a knave or Chris is a knight.
    -  $$ A \implies (\neg B \lor C) $$  
    
However, what if we assumed that if someone is lying, they know their claim is false? Then we would have to explain our rules using a biconditional.

- Alice says: Bob is a knave or Chris is a knight.
    -  $$ A \iff (\neg B \lor C) $$  

Therefore, our answer is correct for what we *assume* the rules of the world are, but that might not match the author of the puzzle's original intention. This shows the benefit of logic! We can use it to address these ambiguities!







