---
layout: default
title: PropLogic
contributors: Alyssa Byrnes
---

## Learning Objectives

-  Express statements in symbolic form, using the logic operations of negation, and, inclusive or, implies, if and only if (iff), and exclusive or (and their symbols: $$\neg, \land, \lor, \rightarrow, \leftrightarrow,$$ and $$\oplus$$) to express statements without ambiguity.
-  Create truth tables in order to recognize *tautologies* and *logically equivalent* expressions, including De Morgan’s rules and conditional expressions.
-  Demonstrate how to use these methods to solve a logic puzzle.

## Propositions and Basic Operations
A *proposition* is a sentence to which one and only one of the terms $$\texttt{True}$$ or $$\texttt{False}$$ can be applied. 

Which of the following are propositions?

-  We are currently in Chapel Hill. - $$\color{green}\texttt{Yes}$$
-  $$1 + 1 = 2$$ - $$\color{green}\texttt{Yes}$$
-  $$2 + x = 4$$ - $$\color{red}\texttt{No}$$
-  It is hot outside. - $$\color{red}\texttt{No}$$


## Negation


A *Truth Table* for negation would look like the following:

$$\begin{array}{|c|c|}
\hline
p  & \neg p  \\
\hline
T & F \\
F & T \\
\hline
\end{array}$$

What this is saying is: <br>
"When $$p$$ is $$\texttt{True}$$, $$\neg p$$ is $$\texttt{False}$$, <br>
and when $$p$$ is $$\texttt{False}$$, $$\neg p$$ is $$\texttt{True}$$.''





Here is an example of a negated proposition:

-  $$p$$: "Today is Monday.''
-  $$\neg p$$: "Today is not Monday.'' 
-  *ALTERNATIVELY:* $$\neg p$$: "It is not the case that today is Monday.''







## Conjunction


A Truth Table for conjunction would look like the following:
$$\begin{array}{|c|c|c|}
\hline
p  & q & p \land q  \\
\hline
T & T & T \\
T & F & F \\
F & T & F \\
F & F & F \\
\hline
\end{array}$$


Here is an example of conjunction:

-  $$p$$: "It is sunny today.''
-  $$q$$: "It is Monday.''
-  $$p \land q$$: "It is sunny today and today is Monday.''



The conjunction ($$p \land q$$) is $$\texttt{True}$$ on sunny Mondays, but it is $$\texttt{False}$$ on any non-sunny day ($$p$$ is $$\texttt{False}$$), and it is $$\texttt{False}$$ on any day that is not Monday ($$q$$ is $$\texttt{False}$$).


## Disjunction

A Truth Table for disjunction would look like the following:
$$\begin{array}{|c|c|c|}
\hline
p  & q & p \lor q  \\
\hline
T & T & T \\
T & F & T \\
F & T & T \\
F & F & F \\
\hline
\end{array}$$


Here is an example of disjunction.

-  $$p$$: "It is sunny today.''
-  $$q$$: "It is Monday.''
-  $$p \lor q$$: "It is sunny today or today is Monday.''




The disjunction ($$p \lor q$$) is $$\texttt{True}$$ on sunny Mondays, on any sunny day ($$p$$ is $$\texttt{True}$$), and on any Monday ($$q$$ is $$\texttt{True}$$). It is $$\texttt{False}$$ on any day where it is both not sunny and not Monday.


## Exclusive Or

A Truth Table for exclusive or would look like the following:
$$\begin{array}{|c|c|c|}
\hline
p  & q& p \oplus q  \\
\hline
T & T & F \\
T & F & T \\
F & T & T \\
F & F & F \\
\hline
\end{array}$$

Here is an example of exclusive or.

-  $$p$$: "It is sunny today.''
-  $$q$$: "It is Monday.''
-  $$p \oplus q$$: "It is sunny today or today is Monday, but not both.''



The exclusive or ($$p \oplus q$$) is $$\texttt{True}$$ on any sunny day ($$p$$ is $$\texttt{True}$$) and on any Monday ($$q$$ is $$\texttt{True}$$), EXCEPT for on sunny Mondays (both $$p$$ and $$q$$ are $$\texttt{True}$$). Additionally, it is $$\texttt{False}$$ on any day where it is both not sunny and not Monday.


## Conditionals


The *conditional statement* $$p \rightarrow q$$ is False when $$p$$ is $$\texttt{True}$$ and $$q$$ is $$\texttt{False}$$, and True otherwise. $$p$$ is called the hypothesis and $$q$$ the conclusion. This can also be called *implication*.

Some English phrases for this would be:

-  If $$p$$, then $$q$$.
-  $$p$$ implies $$q$$.
-  $$q$$ if $$p$$.




A Truth Table for implication would look like the following:
$$\begin{array}{|c|c|c|}
\hline
p  & q & p \rightarrow q  \\
\hline
T & T & T \\
T & F & F \\
F & T & T \\
F & F & T \\
\hline
\end{array}$$


Here is an example of implication.

-  $$p$$: "It is sunny.''
-  $$q$$: "I walk to campus.''
-  $$p \rightarrow q$$: "If it is sunny, then I walk to campus.''


The implication ($$p \rightarrow q$$) is $$\texttt{False}$$ if it is sunny and I do NOT walk to campus. Otherwise, it is $$\texttt{True}$$. 

If it is not sunny ($$p$$ is $$\texttt{False}$$) and I still walk to campus ($$q$$ is $$\texttt{True}$$), this implication is still $$\texttt{True}$$.


## Biconditionals

The *biconditional statement* ("if and only if" or "iff") $$p \leftrightarrow q$$ is $$\texttt{True}$$ when $$p$$ and $$q$$ have the same truth value, and $$\texttt{False}$$ otherwise.

A Truth Table for implication would look like the following:
$$\begin{array}{|c|c|c|}
\hline
p  & q & p \leftrightarrow q  \\
\hline
T & T & T \\
T & F & F \\
F & T & F \\
F & F & T \\
\hline
\end{array}$$



Here is an example of a biconditional.

-  $$p$$: "It is sunny.''
-  $$q$$: "I walk to campus.''
-  $$q \leftrightarrow p$$: "I walk to campus if and only if it is sunny.''


The biconditional ($$p \leftrightarrow q$$) is $$\texttt{True}$$ if it is sunny and I walk to campus or if it is not sunny and I don't walk to campus. Otherwise, it is $$\texttt{False}$$. 


Unlike the previous example, if it is not sunny ($$p$$ is $$\texttt{False}$$) and I still walk to campus ($$q$$ is $$\texttt{True}$$), this biconditional is $$\texttt{False}$$.


## Order Of Operations
- Negations: $$\neg$$
- Conjunctions: $$\land$$
- Disjunctions: $$\lor$$

Everything else can be written as a combination of the above three, but in general, it's best to always clarify order of operations using parentheses!

## Logical Equivalences

Logical expressions that result in the same truth values are considered *logical equivalences*.

- One useful equivalence is *DeMorgan's Law*. It states: 
$$ \neg (p \land q) \equiv \neg p \lor \neg q $$
$$ \neg (p \lor q) \equiv \neg p \land \neg q $$
- Another useful equivalence is: 
$$ p \rightarrow q \equiv \neg p \lor q $$



### Common Logical Equivalences

$$
\begin{array}{l l}
\textbf{Commutative Laws} &
p \lor q \equiv q \lor p \\
 & p \land q\equiv q \land p \\
\hline 
\textbf{Associative Laws} &
(p \lor  q) \lor r \equiv  p \lor  (q \lor  r) \\

& (p \land q) \land r\equiv p \land  (q \land  r)\\
\hline 
\textbf{Distributive Laws}&
p \land  (q \lor  r) \equiv  (p \land  q ) \lor  (p \land  r)\\


 & p \lor  (q \land  r) \equiv  (p \lor  q) \land (p \lor r) \\
\hline 
\textbf{Identity Laws} &

p \lor  F\equiv p\\

& p \land  T \equiv p\\
\hline 
\textbf{Negation Laws} &
p\land \neg p\equiv F\\

& p\lor \neg p\equiv T\\
\hline 
\textbf{Idempotent Laws}&

p \lor  p \equiv p\\


& p\land p \equiv p\\
\hline 
\textbf{Domination Laws}&

p \land F \equiv F\\

& p \lor  T \equiv T\\
\hline 
\textbf{Absorption Laws} &
p \land (p\lor  q)\equiv p\\

& p \lor  (p \land  q) \equiv  p\\
\hline 
\textbf{DeMorgan's Laws} &

 \neg (p \lor  q) \equiv  (\neg p) \land  (\neg q)\\

& \neg (p \land  q) \equiv  (\neg p) \lor  (\neg q)\\
\hline 
\textbf{Double Negation Law} &
\neg (\neg p)\equiv p\\
\hline 
\textbf{Implication} & 
p \implies q \equiv \neg p \lor q\\
\end{array}
$$

## Proving Equivalences

Logical Equivalences can be proven two different ways:

1. Using Truth Tables
2. Directly, using other logical equivalences

### Example 0
We can prove the first part of DeMorgan's Law <br> ($$\neg (p \land q) \equiv \neg p \lor \neg q$$) using a truth table.

$$\begin{array}{|c|c|c|c|c|c|c|}
\hline
p  & q & \neg p & \neg q & p \land q & \neg(p \land q) & \neg p \lor \neg q \\
\hline
T & T  \\
T & F  \\
F & T  \\
F & F  \\
\hline
\end{array}$$

<!-- 
## Proving Equivalences
We can prove the first part of DeMorgan's Law <br> ($$\neg (p \land q) \equiv \neg p \lor \neg q$$) using a truth table.

$$\begin{array}{|c|c|c|c|c|c|c|}
\hline
p  & q & \neg p & \neg q & p \land q & \neg(p \land q) & \neg p \lor \neg q \\
\hline
T & T & F & F \\
T & F & F & T \\
F & T  & T & F \\
F & F & T & T \\
\hline
\end{array}$$

## Proving Equivalences
We can prove the first part of DeMorgan's Law <br> ($$\neg (p \land q) \equiv \neg p \lor \neg q$$) using a truth table.

$$\begin{array}{|c|c|c|c|c|c|c|}
\hline
p  & q & \neg p & \neg q & p \land q & \neg(p \land q) & \neg p \lor \neg q \\
\hline
T & T & F & F & T \\
T & F & F & T  & F\\
F & T  & T & F & F \\
F & F & T & T & F \\
\hline
\end{array}$$

## Proving Equivalences
We can prove the first part of DeMorgan's Law <br> ($$\neg (p \land q) \equiv \neg p \lor \neg q$$) using a truth table.

$$\begin{array}{|c|c|c|c|c|c|c|}
\hline
p  & q & \neg p & \neg q & p \land q & \neg(p \land q) & \neg p \lor \neg q \\
\hline
T & T & F & F & T & F\\
T & F & F & T  & F & T\\
F & T  & T & F & F & T\\
F & F & T & T & F & T \\
\hline
\end{array}$$ -->



$$\begin{array}{|c|c|c|c|c|c|c|}
\hline
p  & q & \neg p & \neg q & p \land q & \neg(p \land q) & \neg p \lor \neg q \\
\hline
T & T & F & F & T & F & F\\
T & F & F & T  & F & T & T\\
F & T  & T & F & F & T & T\\
F & F & T & T & F & T & T \\
\hline
\end{array}$$

The columns for $$\neg(p \land q)$$ and $$\neg p \lor \neg q$$ are equal, so this means $$\neg(p \land q)$$ and $$\neg p \lor \neg q$$ are *logically equivalent*!

### Example 1

Prove $$(a \land \neg b) \rightarrow c \equiv \neg a \lor b \lor c$$ directly using existing logical equivalences.
$$
\begin{array}{|c|c|}
\hline
\textbf{Equivalence} & \textbf{Rule Used}\\
\hline
(a \land \neg b) \rightarrow c & \textbf{Given} \\
\hline
 \equiv \neg (a \land \neg b) \lor c & \textbf{Implication} \\
 \hline
 \equiv  \neg a \lor \neg \neg b \lor c & \textbf{DeMorgan's} \\ \hline
\equiv \neg a \lor b \lor c & \textbf{Double Negation}\\
\hline
\end{array}$$

## Other Considerations

- A truth table computes all possible combinations of $$n$$ propositions, so a truth table always has how many rows?

### Example 0

propositions = $$\{p\}$$

truth values = $$\{\texttt{True}, \texttt{False}\}$$

Truth table:

$$\begin{array}{|c|}
\hline
p    \\
\hline
T  \\
F \\
\hline
\end{array}$$

2 rows... 


### Example 1
propositions = $$\{p, q\}$$

truth values = $$\{\texttt{True}, \texttt{False}\}$$

Truth table:

$$\begin{array}{|c|c|}
\hline
p  & q  \\
\hline
T & T \\
T & F \\
F & T \\
F & F \\
\hline
\end{array}$$

4 rows... 


### Example 2

- A truth table computes all possible combinations of $$n$$ propositions, so a truth table always has how many rows?

propositions = $$\{p,q,...\}$$ $$\leftarrow$$ $$n$$ propositions 

truth values = $$\{\texttt{True}, \texttt{False}\}$$

$$2^n$$ rows!


## Tautologies
-  Notice that a combination of propositions using operators (e.g. $$p \land q$$ makes a new proposition. These can also be called *compound propositions*. 
-  A compound proposition with a truth table where all the values in the last column are $$\texttt{True}$$ is called a *tautology*. 
- An example of this is $$p \lor \neg p$$. 

$$\begin{array}{|c|c|c|}
\hline
p  & \neg p & p \lor \neg p  \\
\hline
T & F & T \\
F & T & T \\
\hline
\end{array}$$

For all values, $$p \lor \neg p$$ evaluates to $$\texttt{True}$$!

## Translating English Sentences
To translate logic to and from English sentences, it is important to know the common phrases for the operators. 

-  $$\neg p$$ (Negation): "not $$p$$"
-  $$p \land q$$ (Conjunction): "$$p$$ and $$q$$"
-  $$p \lor q$$ (Disjunction): "$$p$$ or $$q$$"
-  $$p \oplus q$$ (Exclusive Or): "$$p$$ xor $$q$$"; "$$p$$ or $$q$$, but not both"
-  $$p \rightarrow q$$ (Conditional/Implication): "$$p$$ implies $$q$$"; "if $$p$$ then $$q$$"; "$$q$$ if $$p$$"
-  $$p \leftrightarrow q$$ or $$p$$ iff $$q$$ (Biconditional): "$$p$$ if and only if $$q$$"

### Example

Here's an example of breaking up an English language sentence.

- Start with the sentence: "You cannot ride the roller coaster if you are under 4 feet tall.''
- Then, you break your sentence to the smallest propositions possible.
- $$a$$ = "You can ride the roller coaster''
- $$b$$ = "you are under 4 feet tall''
- Now your sentence is: Not $$a$$ if $$b$$.
- So you know you can write it as: $$b \rightarrow \neg a$$.
- Notes:
    - If it doesn't directly match any of the phrases listed, use truth tables to see what it matches.
    - Sometimes it takes a little experimenting/practice


## Using Logic For Problem Solving 
The rest of these slides are optional, but they demonstrate how logic can be used for problem solving!

## Using Logic For Problem Solving 
### Knights and Knaves (Raymond Smullyan)
On an island, every inhabitant is a knight who always tells the truth, or a knave who always lies. You meet three inhabitants, Alice, Bob, and Chris.

- Alice says: Bob is a knave or Chris is a knight.
- Bob says: Alice is a knight if, and only if, Chris is a knave.

Can you determine uniquely what each of Alice, Bob, and Chris are?

## Using Logic For Problem Solving
### Knights and Knaves (Raymond Smullyan)

1. Define convenient variables for propositions.
2. Transform what they say into statements that *always* should evaluate to $$\texttt{True}$$. These are the rules of our world.
3. Make a truth table – With 3 people, we have $$2^3$$ rows
4. Check if a unique row makes both statements true. 

## Using Logic For Problem Solving
### Knights and Knaves (Raymond Smullyan)

$$1.$$ Define convenient variables for propositions.

- $$A =$$ "Alice is a knight" 
- $$B =$$ "Bob is a knight"
- $$C=$$ "Chris is a knight"


- $$\neg A =$$ "Alice is a knave" 
- $$\neg B =$$ "Bob is a knave"
- $$\neg C=$$ "Chris is a knave"


## Using Logic For Problem Solving


$$2.$$ Transform what they say into statements that *always* should evaluate to $$\texttt{True}$$. These are the rules of our world.

- Alice says: Bob is a knave or Chris is a knight.
- Bob says: Alice is a knight if, and only if, Chris is a knave.



## Using Logic For Problem Solving


$$2.$$ Transform what they say into statements that *always* should evaluate to $$\texttt{True}$$. These are the rules of our world.

- Alice says: Bob is a knave $$\lor$$ Chris is a knight
- Bob says: Alice is a knight $$\leftrightarrow$$ Chris is a knave

(Propositions: 

$$\{A =$$ "Alice is a knight", $$B =$$ "Bob is a knight",$$C=$$ "Chris is a knight",
$$\neg A =$$ "Alice is a knave", $$\neg B =$$ "Bob is a knave",$$\neg C=$$ "Chris is a knave"\})



## Using Logic For Problem Solving


$$2.$$ Transform what they say into statements that *always* should evaluate to $$\texttt{True}$$. These are the rules of our world.

- Alice says: $$\neg B \lor C$$
- Bob says: $$A \leftrightarrow \neg C$$

(Propositions: 

$$\{A =$$ "Alice is a knight", $$B =$$ "Bob is a knight",$$C=$$ "Chris is a knight",
$$\neg A =$$ "Alice is a knave", $$\neg B =$$ "Bob is a knave",$$\neg C=$$ "Chris is a knave"\})





## Using Logic For Problem Solving



$$3.$$ Make a truth table

Rules of the World: $$A \rightarrow (\neg B \lor C)$$ and $$B \rightarrow (A \leftrightarrow \neg C)$$ 

$$\begin{array}{|c|c|c|c|c|}
\hline
A & B & C &  A \rightarrow (\neg B \lor C) & B \rightarrow (A \leftrightarrow \neg C) \\
\hline
T & T & T & T & F\\
T & T & F & F & T\\
\color{green}T & \color{green}F & \color{green}T & \color{green}T &\color{green}T\\
\color{green}T & \color{green}F & \color{green}F &\color{green} T &\color{green}T\\ 
\color{green}F & \color{green}T & \color{green}T &  \color{green}T &\color{green}T\\
F & T & F & T &F\\
\color{green}F & \color{green}F & \color{green}T & \color{green}T &\color{green}T\\
\color{green}F & \color{green}F & \color{green}F & \color{green}T &\color{green}T\\
\hline
\end{array}$$




## Using Logic For Problem Solving


$$4.$$ Check if a unique row makes both statements true. 

<!-- Rules of the World: $$A \rightarrow (\neg B \lor C)$$ and $$B \rightarrow (A \leftrightarrow \neg C)$$  -->

$$\begin{array}{|c|c|c|c|c|}
\hline
A & B & C &  A \rightarrow (\neg B \lor C) & B \rightarrow (A \leftrightarrow \neg C) \\
\hline
T & T & T & T & F\\
T & T & F & F & T\\
\color{green}T & \color{green}F & \color{green}T & \color{green}T &\color{green}T\\
\color{green}T & \color{green}F & \color{green}F &\color{green} T &\color{green}T\\ 
\color{green}F & \color{green}T & \color{green}T &  \color{green}T &\color{green}T\\
F & T & F & T &F\\
\color{green}F & \color{green}F & \color{green}T & \color{green}T &\color{green}T\\
\color{green}F & \color{green}F & \color{green}F & \color{green}T &\color{green}T\\
\hline
\end{array}$$

<!-- $$\begin{array}{|c|c|c|c|c|}
\hline
A & B & C &  A \rightarrow (\neg B \lor C) & B \rightarrow (A \leftrightarrow \neg C) \\
\hline
T & T & T & T & F\\
T&T&F&F&T\\
\color{green}T & \color{green}F & \color{green}T & \color{green}T &\color{green}T\\
T & F & F & T & T\\ 
F & T & T &  T &T\\
F & T & F & T &F\\
F & F & T & T & T\\
F & F & F & T &T\\
\hline
\end{array}$$ -->

**All of the values in green are assignments that could work! Let's test one of these!**
 

## Testing A Solution... 

$$A = T, B = F, C = T$$

So, Alice is a knight, Bob is a knave, and Chris is a knight.

- Alice says: Bob is a knave or Chris is a knight.
    - $$A \rightarrow (\neg B \lor C)$$ 
    - $$T \rightarrow (\neg(F) \lor T)$$ evaluates to True!

- Bob says: Alice is a knight if, and only if, Chris is a knave. 
    - $$B \rightarrow (A \leftrightarrow \neg C)$$
    - $$F \rightarrow (T \leftrightarrow \neg T)$$ evaluates to True!

Both of our rules hold in this world with these assignments, so we know that this solution works!


## Why this isn't a good problem... 

This problem isn't explicit enough, so we found ourselves making an assumption.

When we solved it, we assumed that if someone is lying, they don't actually know whether or not what they are saying is the truth, so their claim could either be true or false. This is why we were able to use implication.

- Alice says: Bob is a knave or Chris is a knight.
    - $$A \rightarrow (\neg B \lor C)$$ 
    
However, what if we assumed that if someone is lying, they know their claim is false? 


If we assume that if someone is lying, they know their claim is false, then we would have to explain our rules using a *biconditional*.

- Alice says: Bob is a knave or Chris is a knight.
    - $$A \leftrightarrow (\neg B \lor C)$$ 

Therefore, our answer is correct for what we *assume* the rules of the world are, but that might not match the author of the puzzle's original intention. This shows the benefit of logic! We can use it to address these ambiguities!










