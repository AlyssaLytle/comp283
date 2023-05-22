---
title: Propositional Logic
theme: dracula
center: false
transition: 'none'
---


## Learning Objectives
<div id="content">

-  Express statements in symbolic form, using the logic operations of negation, and, inclusive or, implies, if and only if (iff), and exclusive or (and their symbols: $\neg, \land, \lor, \rightarrow, \leftrightarrow,$ and $\oplus$) to express statements without ambiguity.
-  Create truth tables in order to recognize *tautologies* and *logically equivalent* expressions, including De Morgan’s rules and conditional expressions.
-  Demonstrate how to use these methods to solve a logic puzzle.


</div>
## Propositions and Basic Operations
<div id="content">
A *proposition* is a sentence to which one and only one of the terms $\texttt{True}$ or $\texttt{False}$ can be applied. 

Which of the following are propositions?

-  We are currently in Chapel Hill. 
-  $1 + 1 = 2$ 
-  $2 + x = 4$ 
-  It is hot outside. 


</div>
## Propositions and Basic Operations
<div id="content">
A *proposition* is a sentence to which one and only one of the terms $\texttt{True}$ or $\texttt{False}$ can be applied. 

Which of the following are propositions?

-  We are currently in Chapel Hill. - Yes
-  $1 + 1 = 2$ - Yes
-  $2 + x = 4$ - No
-  It is hot outside. - No



</div>
## Order Of Operations
<div id="content">
- Negations: $\neg$
- Conjunctions: $\land$
- Disjunctions: $\lor$

Everything else can be written as a combination of the above three, but in general, it's best to always clarify order of operations using parentheses!


</div>
## Proving Equivalences
<div id="content">

Logical Equivalences can be proven two different ways:

1. Using Truth Tables
2. Directly, using other logical equivalences


</div>
## Proving Equivalences - Example 1
<div id="content">
We can prove the first part of DeMorgan's Law <br> ($\neg (p \land q) \equiv \neg p \lor \neg q$) using a truth table.

$\begin{array}{|c|c|c|c|c|c|c|}
\hline
p  & q & \neg p & \neg q & p \land q & \neg(p \land q) & \neg p \lor \neg q \\
\hline
T & T  \\
T & F  \\
F & T  \\
F & F  \\
\hline
\end{array}$

<!-- 

</div>
## Proving Equivalences
<div id="content">
We can prove the first part of DeMorgan's Law <br> ($\neg (p \land q) \equiv \neg p \lor \neg q$) using a truth table.

$\begin{array}{|c|c|c|c|c|c|c|}
\hline
p  & q & \neg p & \neg q & p \land q & \neg(p \land q) & \neg p \lor \neg q \\
\hline
T & T & F & F \\
T & F & F & T \\
F & T  & T & F \\
F & F & T & T \\
\hline
\end{array}$


</div>
## Proving Equivalences
<div id="content">
We can prove the first part of DeMorgan's Law <br> ($\neg (p \land q) \equiv \neg p \lor \neg q$) using a truth table.

$\begin{array}{|c|c|c|c|c|c|c|}
\hline
p  & q & \neg p & \neg q & p \land q & \neg(p \land q) & \neg p \lor \neg q \\
\hline
T & T & F & F & T \\
T & F & F & T  & F\\
F & T  & T & F & F \\
F & F & T & T & F \\
\hline
\end{array}$


</div>
## Proving Equivalences
<div id="content">
We can prove the first part of DeMorgan's Law <br> ($\neg (p \land q) \equiv \neg p \lor \neg q$) using a truth table.

$\begin{array}{|c|c|c|c|c|c|c|}
\hline
p  & q & \neg p & \neg q & p \land q & \neg(p \land q) & \neg p \lor \neg q \\
\hline
T & T & F & F & T & F\\
T & F & F & T  & F & T\\
F & T  & T & F & F & T\\
F & F & T & T & F & T \\
\hline
\end{array}$ -->


</div>
## Proving Equivalences - Example 1
<div id="content">
We can prove the first part of DeMorgan's Law <br> ($\neg (p \land q) \equiv \neg p \lor \neg q$) using a truth table.

$\begin{array}{|c|c|c|c|c|c|c|}
\hline
p  & q & \neg p & \neg q & p \land q & \neg(p \land q) & \neg p \lor \neg q \\
\hline
T & T & F & F & T & F & F\\
T & F & F & T  & F & T & T\\
F & T  & T & F & F & T & T\\
F & F & T & T & F & T & T \\
\hline
\end{array}$

The columns for $\neg(p \land q)$ and $\neg p \lor \neg q$ are equal, so this means $\neg(p \land q)$ and $\neg p \lor \neg q$ are *logically equivalent*!


</div>
## Proving Equivalences - Example 2
<div id="content">
Prove $(a \land \neg b) \rightarrow c \equiv \neg a \lor b \lor c$ directly using existing logical equivalences.
\begin{array}{|c|c|}
\hline
\textbf{Equivalence} & \textbf{Rule Used}\\
\hline
(a \land \neg b) \rightarrow c & \textbf{Given} \\
\ldots \\
\equiv \neg a \lor b \lor c & \\
\hline
\end{array}


</div>
## Proving Equivalences - Example 2
<div id="content">
Prove $(a \land \neg b) \rightarrow c \equiv \neg a \lor b \lor c$ directly using existing logical equivalences.
\begin{array}{|c|c|}
\hline
\textbf{Equivalence} & \textbf{Rule Used}\\
\hline
(a \land \neg b) \rightarrow c & \textbf{Given} \\
\hline
 & \\ \hline
 & \\ \hline
 & \\ 
\hline
\end{array}


</div>
## Proving Equivalences - Example 2
<div id="content">
Prove $(a \land \neg b) \rightarrow c \equiv \neg a \lor b \lor c$ directly using existing logical equivalences.
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
\end{array}


</div>
## Other Considerations
<div id="content">

- A truth table computes all possible combinations of $n$ propositions, so a truth table always has how many rows?

propositions = $\{p\}$

truth values = $\{\texttt{True}, \texttt{False}\}$

Truth table:

$\begin{array}{|c|}
\hline
p    \\
\hline
T  \\
F \\
\hline
\end{array}$

2 rows... 



</div>
## Other Considerations
<div id="content">

- A truth table computes all possible combinations of $n$ propositions, so a truth table always has how many rows?

propositions = $\{p, q\}$

truth values = $\{\texttt{True}, \texttt{False}\}$

Truth table:

$\begin{array}{|c|c|}
\hline
p  & q  \\
\hline
T & T \\
T & F \\
F & T \\
F & F \\
\hline
\end{array}$

4 rows... 



</div>
## Other Considerations
<div id="content">

- A truth table computes all possible combinations of $n$ propositions, so a truth table always has how many rows?

propositions = $\{p,q,...\}$ $\leftarrow$ $n$ propositions 

truth values = $\{\texttt{True}, \texttt{False}\}$

?


</div>
## Other Considerations
<div id="content">

- A truth table computes all possible combinations of $n$ propositions, so a truth table always has how many rows?

propositions = $\{p,q,...\}$ $\leftarrow$ $n$ propositions 

truth values = $\{\texttt{True}, \texttt{False}\}$

$2^n$ rows!



</div>
## Tautologies
<div id="content">
-  Notice that a combination of propositions using operators (e.g. $p \land q$ makes a new proposition. These can also be called *compound propositions*. 
-  A compound proposition with a truth table where all the values in the last column are $\texttt{True}$ is called a *tautology*. 
- An example of this is $p \lor \neg p$. 

$\begin{array}{|c|c|c|}
\hline
p  & \neg p & p \lor \neg p  \\
\hline
T & F & T \\
F & T & T \\
\hline
\end{array}$

For all values, $p \lor \neg p$ evaluates to $\texttt{True}$!


</div>
## Translating English Sentences
<div id="content">
To translate logic to and from English sentences, it is important to know the common phrases for the operators. 

-  $\neg p$ (Negation): "not $p$"
-  $p \land q$ (Conjunction): "$p$ and $q$"
-  $p \lor q$ (Disjunction): "$p$ or $q$"
-  $p \oplus q$ (Exclusive Or): "$p$ xor $q$"; "$p$ or $q$, but not both"
-  $p \rightarrow q$ (Conditional/Implication): "$p$ implies $q$"; "if $p$ then $q$"; "$q$ if $p$"
-  $p \leftrightarrow q$ or $p$ iff $q$ (Biconditional): "$p$ if and only if $q$"


</div>
## Using Logic For Problem Solving 
<div id="content">
The rest of these slides are optional, but they demonstrate how logic can be used for problem solving!


</div>
## Using Logic For Problem Solving 
<div id="content">
### Knights and Knaves (Raymond Smullyan)
On an island, every inhabitant is a knight who always tells the truth, or a knave who always lies. You meet three inhabitants, Alice, Bob, and Chris.

- Alice says: Bob is a knave or Chris is a knight.
- Bob says: Alice is a knight if, and only if, Chris is a knave.

Can you determine uniquely what each of Alice, Bob, and Chris are?


</div>
## Using Logic For Problem Solving
<div id="content">
### Knights and Knaves (Raymond Smullyan)

1. Define convenient variables for propositions.
2. Transform what they say into statements that *always* should evaluate to $\texttt{True}$. These are the rules of our world.
3. Make a truth table – With 3 people, we have $2^3$ rows
4. Check if a unique row makes both statements true. 


</div>
