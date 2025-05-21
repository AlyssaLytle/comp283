---
layout: default
title: Practice and Review 0
contributors: Alyssa Byrnes
---

# Review and Practice 0

Here are the practice problems to prepare you for the quiz! I will try and cover as many as possible, but please come to the review session with requests! We can also review problems from the lessons, but I encourage you to use office hours for this as well!

## Date and Time: Thurs, May 22 at 12 pm
* [Zoom Link](https://unc.zoom.us/j/91069874856)
* [Recording Link](/)



## Problems

### 1-3 Logic 

1. Prove $$a \leftrightarrow b \equiv (a \rightarrow b) \land (b \rightarrow a)$$ using a truth table.

2. True or False: You can prove compound propositions $$X$$ and $$Y$$ are logically equivalent by showing $$X \leftrightarrow Y$$ is a tautology. Explain your answer.
(Hint, try this for the equivalence $$p \rightarrow q \equiv \neg p \lor q$$)

3. True or False: $$((a \lor b) \oplus \neg b) \lor \texttt{True}$$ always evaluates to $$\texttt{True}$$ regardless of the values of $$a$$ and $$b$$. Explain your answer.


### 4. Sets, Quantifiers, + Relations 
For this problem, let:

* $$S$$ be the set of all coins I possess. It could potentially contain any coin type from any country of the world.
* $$C$$ be the set of coin purses (Coins go IN these)
* Let $$p(x)$$ be a predicate:  $$\forall x \in S$$, $$p(x)$$ is True $$\leftrightarrow x$$ is a penny. 
* Let $$e(x)$$ be a predicate:  $$\forall x \in S$$, $$e(x)$$ is True $$\leftrightarrow x$$ is a euro. 
* Let $$IN(x,c)$$ be a predicate:  $$\forall x \in S, \forall c \in C$$, $$In(x,c)$$ is True $$\leftrightarrow$$ coin $$x$$ is in coin purse $$c$$. 
* Let $$q(c)$$ be a function that returns the number of coins in coin purse $$c$$.

Express the following using predicate logic:

> 4.1. No penny is a euro.

> 4.2. There are coin purses of different sizes.

> 4.3. There is a coin purse for every coin.

> 4.4. No coin is without a coin purse. (Extra question: can there be an empty coin purse?)

> 4.5 There does not exist a purse without a coin. (Use $$IN$$ for this, not $$q(c)$$.)

> 4.6. A coin purse with a euro must contain at least two coins.


### 5. More Relations

Let the relation $$R = \{(x,y) \mid x,y \in \mathbb{N} \land x + y = 10 \}$$.

Justify your answers for the following using the formal definition of a symmetric relation given in class. If your answer is no, provide a counter example.

> 5.1 Is $$R$$ symmetric? 

> 5.2 Is $$R$$ reflexive? 

> 5.3 Is $$R$$ transitive? 



## Solutions

### 1. Logic 

$$
\begin{array}{|c|c|c|c|c|c|}
\hline
a  & b & a \to b & b \to a & a \leftrightarrow b  & (a \to b) \land (b \to a)  \\
\hline
T & T & T & T & \color{green} T & \color{green} T  \\
T & F & F & T & \color{green} F & \color{green} F  \\
F & T & T & F & \color{green} F & \color{green} F \\
F & F & T & T & \color{green} T & \color{green} T  \\
\hline
\end{array}
$$

Since the last two columns are equivalent, this shows that $$a \leftrightarrow b$$ and $$(a \to b) \land (b \to a)$$ are equivalent for all possible values of $$a$$ and $$b$$ and therefore *logically equivalent*.


### 2. Logic 
True!

Let's try this for $$X = p \rightarrow q$$  and $$Y =\neg p \lor q$$

$$
\begin{array}{|c|c|c|c|c|c|}
\hline
  &  &  & X & Y & X \leftrightarrow Y    \\

\hline
p  & q & \neg p & p \to q & \neg p \lor q & \big(p \to q \big) \leftrightarrow \big( \neg p \lor q \big) \\
\hline
T & T & F & T & T & T \\
T & F & F & F & F & T \\
F & T & T & T & T & T \\
F & F & T & T & T & T \\
\hline
\end{array}
$$

As you can see, if two columns (in this case $$X$$ and $$Y$$) are equal (aka logically equivalent), then $$X \leftrightarrow Y$$ will always evaluate to $$\texttt{True}$$ (aka it's a tautology)! 

### 3. Logic

This is True. You can demonstrate this with a truth table, but you can also just reason that any X that is "or"ed with a $$\texttt{True}$$, will always be $$\texttt{True}$$. 

In other words, for any compound proposition $$X$$, $$X \lor \texttt{True} = \texttt{True}$$.

### 4. 

*There can be multiple correct answers for these statements, so please feel free to run them by us in the review session or on EdStem!*

#### 4.1 
> "For all coins, if a coin is a penny, then it is not a euro."

> $$\forall x \in S, p(x) \to \neg e(x)$$ 

> "There does not exist a coin that is both a penny and a euro."

> $$\neg \exists x \in S, p(x) \land e(x)$$ 

#### 4.2
>"It is not the case that all coin purses are the same size."

> $$\neg \big( \forall c_1, c_2 \in C, q(c_1) = q(c_2)
    \big)$$

> "There exist coin purses of different sizes."

> $$ \exists c_1, c_2 \in C, q(c_1) \neq q(c_2) $$

#### 4.3
> "For every coin, there exists a coin purse that that coin is in."

> $$\forall x \in S, \exists c \in C, IN(x,c)$$

#### 4.4 

> "There does not exist a coin that isn't in a purse."

> This is just the same statement as above. We can transform it by adding a double negation.

> $$\neg \neg \big(\forall x \in S, \exists c \in C, IN(x,c)\big)$$

#### 4.5

> "There does not exist a purse that has no coins."

> $$ \neg \exists c \in C, \forall x \in S, \neg IN(x,c)$$

#### 4.6

> "For all coin purses, if there is a coin in the purse that is a euro, then the purse must contain at least 2 coins."

> $$\forall x \in S, c \in C, \big(IN(x,c) \land e(x)\big) \to q(c) \geq 2$$

### 5. 

*Solution coming soon.*