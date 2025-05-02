---
layout: default
title: ProofsCont
contributors: Alyssa Byrnes
---

## Review

- Statements you want to prove are usually of the form $$P \implies Q$$. 

- Sometimes this is obvious to see, and sometimes it takes a little reasoning.

- However, there are also times $$P$$ is not directly stated, so you can assume it means "everything you know about this subject is true" 

- In other words, $$P \implies Q$$ could be stated as "If everything I know about this subject is true, then $$Q$$." 

- What's difficult about this is that it's harder to know where to start (aka what to put on line $$1$$) because you don't have an obvious $$P$$.

## Finding P and Q

### Example

- "If $$x$$ is even, $$x^2$$ is even." 
- $$P:$$ $$x$$ is even 
- $$Q:$$ $$x^2$$ is even

- "There are infinitely many primes." 
- This can be restated as "For all $$a \in \mathbb{Z}$$, if $$a$$ is prime, then there exists a prime $$b \in \mathbb{Z}$$ such that $$b>a$$.''  
- $$P:$$ $$a \in \mathbb{Z}$$ is prime 
- $$Q:$$ There exists $$b \in \mathbb{Z}$$ such that $$b>a$$ 
    
- "$$x-1 < \left \lfloor{x}\right \rfloor$$" 
- $$P:$$ Everything you know about math is true 
- $$Q:$$ $$x-1 < \left \lfloor{x}\right \rfloor$$
    
## Rewrites

Here are some common rewrites you might see when constructing your proofs:

- $$n$$ is an even integer converts to $$n = 2t$$ for some $$t$$
- $$n$$ is an odd integer converts to $$n = 2t + 1$$ for some $$t$$
- $$n$$ is a rational number converts to $$n = \frac{a}{b}$$ where $$a$$ and $$b$$ are integers
- $$n$$ divides $$m$$ converts to $$m = nt$$ for some integer $$t$$
- $$n$$ is a square converts to $$n = t^2$$ for some integer $$t$$.
- $$n = a \bmod b$$ converts to $$n = bt + a$$ for some integer $$t$$.

    
## Main Types of Proofs

The four typical ways we show $$P \implies Q$$ are the following:

- Direct Proof

- Proof By Contradiction

- Proof By Contrapositive

- Proof By Counterexample

## Direct Proofs

These are the proofs we did last class. 

To show $$P \implies Q$$, you start with $$P$$ and you reason to get to $$Q$$.


## Proof By Contradiction

> - $$P \implies Q \equiv \neg(P \land \neg Q)$$. 

> - This leads to why we do proofs by contradiction. 

> - Instead of proving $$P \implies Q$$, we prove $$P \land \neg Q$$ does not hold. 

> - In other words, we start with $$P \land \neg Q$$ and get to an impossible state $$\bot$$. 

### Example 

- A really famous proof is the proof that $$\sqrt{2}$$ is irrational.

- Since $$P$$ isn't specified, we'll make it "Everything I know about math is true" 

- $$Q: \sqrt{2}$$ is irrational.

- We want to show that $$P \land \neg Q$$ does NOT hold. 

- So we say: Everything I know about math is true and $$\sqrt{2}$$ is *rational*.

## Contradiction Example:

For this proof we are going to use the following statement: 

**Squared Evens Rule:** If $$x^2$$ is even, then $$x$$ is even.

Additionally, recall the definition of a rational number:

A rational number can be written as $$\frac{a}{b}$$ such that $$a, b \in \mathbb{Z}$$ and $$GCD(a,b)=1$$.

## Contradiction Example

\begin{equation*}
\begin{array}{l l l}
   1. &  \sqrt{2} \textrm{ is rational}  &  \textrm{Assumption} \\
   2.  & \sqrt{2} = \frac{a}{b} \land a,b \in \mathbb{Z} \land GCD(a,b) = 1 & \textrm{Definition of Rational Numbers} \\
   3. & \sqrt{2} b = a & \textrm{Took left side of 2. and multiplied both sides by } b \\
   4. & 2 b^2 = a^2 & \textrm{Squared both sides} \\
   5. & a^2 \textrm{ is even} & \textrm{Definition of even number} \\
   6. & a \textrm{ is even} & \textrm{Squared Evens Rule}\\
   7. & a = 2k \land k \in \mathbb{Z}  & \textrm{Definition of even number}\\
   8. & 2b^2 = (2k)^2 & \textrm{Plugged in 7. to 4.}\\
   9. & 2b^2 = 4k^2 & \textrm{Simplified}\\
   10. & b^2 = 2k^2 & \textrm{Divided both sides by } 2 \\
   11. & b^2 \textrm{ is even} & \textrm{Definition of even number} \\
   12. & b \textrm{ is even} & \textrm{Squared Evens Rule}\\
   13. & b= 2m \land m \in \mathbb{Z}  & \textrm{Definition of even number}\\
   14. & 2 \textrm{ is a factor of both } a \textrm{ and } b & \textrm{Lines 7. and 13.} \\
   15. & \bot & \textrm{Lines 2. and 14. contradict each other } \square
\end{array}
\end{equation*}

## Proof by Contrapositive

For a proof of contrapositive, you're going to use the equality we proved last class: 

$$P \implies Q \equiv \neg Q \implies \neg P$$.

In other words, instead of proving $$P \implies Q$$, we are going to assume $$\neg Q$$ and show that it leads to $$\neg P$$.

### Example 
- We want to prove: If $$x^2$$ is odd, $$x$$ is odd.  

- $$P:$$ $$x^2$$ is odd 

- $$Q:$$ $$x$$ is odd.

- Let's write this as a contrapositive:  $$\neg Q \implies \neg P$$.

- If $$x$$ is not odd, then $$x^2$$ is not odd. Or, equivalently, If $$x$$ is even, then $$x^2$$ is even. We've actually already proved this!$$\square$$




## Proof by Counterexample

If you want to disprove something, the easiest way is usually by counter example. 

You don't have to do this in the typical two column format as long as you make your reasoning clear.

### Example

- Say I ask you to prove the following is false: If $$x$$ is even, $$x^2$$ is odd.

- Counterexample: $$x = 2$$.

- $$2$$ is even, and $$2^2= 4$$ is even. $$\square$$

## Other Types of Proofs

You may see some other types of proofs that follow from the types of proofs we've already discussed. We will discuss a few.

- Biconditional
- Forall
    - Exhaustive
    - Proof by Cases
- Existence
    - Constructive
    
    
- For our proofs, we are basically writing a $$\implies$$ to get from line to line.

- Sometimes, instead of proving $$P \implies Q$$, you'll want to prove $$P \iff Q$$. 

- The benefit of this type of proof is that you can start from $$P$$ or $$Q$$ to get to the other side. This is because $$P \iff Q$$  is the same as saying $$Q \iff P$$. 

- The added requirement is that you have to use $$\iff$$ rules to get from line to line. Thankfully, most definitions are actually defined using $$\iff$$.



## Biconditional Proofs


### Example
We want to prove $$x \in \overline{A \cap B} \iff x \in \bar{A} \cup \bar{B}$$

\begin{equation*}
\begin{array}{l l l}
  1. & x \in \overline{A \cap B}   &  \\
  2. \iff & \neg (x \in A \cap B)   & \textrm{Complement Definition} \\ 
  3. \iff & \neg (x \in A \land x \in B) & \textrm{Intersection Definition} \\
  4. \iff & \neg (x \in A) \lor \neg (x \in B) & \textrm{DeMorgan's Logic} \\
  5. \iff & x \in \bar{A} \lor x \in \bar{B} & \textrm{Complement Definition} \\
  6. \iff & x \in \bar{A} \cup \bar{B} & \textrm{Union Definition} 
\end{array}
\end{equation*}


## Logical Equivalence
Proofs of logical equivalence are of the form $$P \iff Q$$. 

Why? Remember that if $$P \equiv Q$$, then $$P \iff Q$$ is always true!


### Example
Say we want to prove $$a \implies b \equiv \neg b \implies \neg a$$.

So we can say $$P: a \implies b$$ and $$Q: \neg b \implies \neg a$$.

First, let's do this proof starting at $$P$$ to get to $$Q$$.
 
\begin{equation*}
\begin{array}{l l l}
    1. & a \implies b & \textrm{Given } (P) \\
    2. & \equiv \neg a \lor b & \textrm{Implication Definition} \\
    3. & \equiv b \lor \neg a & \textrm{Commutativity} \\
    4. & \equiv \neg (\neg b) \lor \neg a & \textrm{Double Negation} \\
    5. & \equiv \neg b \implies \neg a & \textrm{Implication Definition }  \square ~ (Q)~ \\ 
\end{array}
\end{equation*}



## Logical Equivalence Cont.

As previously stated, we can also start at $$Q$$ to get to $$P$$. 

\begin{equation*}
\begin{array}{l l l}
    1. & \equiv \neg b \implies \neg a & \textrm{Given } (Q) \\
    2. & \equiv \neg \neg b \lor \neg a & \textrm{Implication Definition}\\
    3. & \equiv b \lor \neg a & \textrm{Double Negation} \\ 
    4. & \equiv \neg a \lor b & \textrm{Commutativity} \\
    5. & \equiv a \implies b & \textrm{Implication Definition } \square ~ (P)    \\ 
\end{array}
\end{equation*}

Either of these proofs are acceptable because they are saying the same thing! Which side you want to start at is really a personal preference.


## Forall


You may want to prove statements such as "$$\forall x \in S, P(x) \implies Q(x)$$."

As previously discussed, to prove a "for all" statement, you want to look at every element in $$S$$ and show that $$P(x) \implies Q(x)$$ holds. 

You can often do this with a direct proof. All of the things we've directly proved so far are actually "for all" proofs.

- $$\forall x \in \mathbb{Z}$$, If $$x$$ is even, $$x^2$$ is even
- $$\forall x \in \mathbb{Z}, {} x-1 < \left \lfloor{x}\right \rfloor$$
- $$\forall a,b,c \in \{\texttt{True}, \texttt{False}\}, {} \neg a \lor \neg(b \land \neg c) \equiv a \implies (b \implies c)$$
- $$\forall a,b,c \in \mathbb{Z}$$, if $$a \mid b$$ and $$b \mid c$$, then $$a \mid c$$

However, we can also prove "for all" statements by exhaustively looking at every element in $$S$$ and checking if $$P(x)$$ holds.

- $$F = \{$$Erik, Jos&eacute;, Nicoleta, Aksana$$\}$$
- $$V = \{$$Aksana, Erik$$\}$$ is the set of your friends who are vegetarian
- $$N = \{$$Aksana$$\}$$ is the set of your friends who are vegan
- We want to prove: $$\forall x \in F,{} x \in N \implies x \in V$$

## Forall, Exhaustive

However, we can also prove "for all" statements by *exhaustively* looking at every element in $$S$$ and checking if $$P(x)$$ holds. 

Fittingly, this is called a **Proof by Exhaustion**.

A good example is the set problem you've already seen:

>- $$F = \{$$Erik, Jos&eacute;, Nicoleta, Aksana$$\}$$
>- $$V = \{$$Aksana, Erik$$\}$$ is the set of your friends who are vegetarian
>- $$N = \{$$Aksana$$\}$$ is the set of your friends who are vegan
>- We want to prove: $$\forall x \in F,{} x \in N \implies x \in V$$

$$\begin{array}{| l | c | c | c |}
    \hline
       x  &  x \in N & x \in V & x \in N \implies x \in V \\
       \hline
       \textrm{Erik} & \texttt{False} & \texttt{False} & \textrm{True} \\
        \textrm{Jos\'e} & \texttt{False} & \texttt{False} & \textrm{True}  \\
        \textrm{Nicoleta} & \texttt{False} & \texttt{False} & \textrm{True} \\
        \textrm{Aksana} & \texttt{True} & \texttt{True} & \textrm{True}  \\
         \hline
    \end{array}$$

$$sgn(x) = \begin{cases}
    -1 & x<0\\
    0 & x =0\\
    1 & x>0
    \end{cases}$$
    


## Proof by Cases

A **Proof by Cases** is a kind of proof by exhaustion. You are breaking the set you are proving something about into smaller sets.

A good example is when we proved the definition of absolute value.

$$|x| = sgn(x) \cdot x$$

$$sgn(x) = \begin{cases}
    -1 & x<0\\
    0 & x =0\\
    1 & x>0
    \end{cases}$$
    
Case 1: $$x > 0$$

$$\begin{array}{l l l}
      1. & x > 0   & \textrm{Case Assertion} \\
      2. & sgn(x) = 1  & \textrm{Signum Def.} \\
      3. & sgn(x) \cdot x = x & \textrm{Multiply both sides by } x \\
      4. & |x| = x & \textrm{Applied Def. of Absolute Value to Line 1} \\
      5. & sgn(x) = |x| & \textrm{Compared Lines 3 and 5} \\
    \end{array}$$




## Proof by Cases Cont.

Case 2: $$x = 0$$

$$\begin{array}{l l l}
      1. & x = 0   & \textrm{Case Assertion} \\
      2. & sgn(x) = 0  & \textrm{Signum Def.} \\
      3. & sgn(x) \cdot x = 0 & \textrm{Multiply both sides by } x \\
      4. & |x| = 0 & \textrm{Applied Def. of Absolute Value to Line 1} \\
      5. & sgn(x) = |x| & \textrm{Compared Lines 3 and 5} \\
    \end{array}$$

Case 3: $$x < 0$$

$$\begin{array}{l l l}
      1. & x < 0   & \textrm{Case Assertion} \\
      2. & sgn(x) = -1  & \textrm{Signum Def.} \\
      3. & sgn(x) \cdot x = -x & \textrm{Multiply both sides by } x \\
      4. & |x| = -x & \textrm{Applied Def. of Absolute Value to Line 1} \\
      5. & sgn(x) = |x| & \textrm{Compared Lines 3 and 5} \\
    \end{array}$$

- $$F = \{$$Erik, Jos&eacute;, Nicoleta, Aksana$$\}$$
- $$V = \{$$Aksana, Erik$$\}$$ is the set of your friends who are vegetarian
- $$N = \{$$Aksana$$\}$$ is the set of your friends who are vegan
- We want to prove: $$\exists x \in F,{} x \in N \implies x \in V$$

Sometimes you just need to prove the existence of something. 

$$\exists x \in S, {} P(x)$$.

Again, like we discussed in class, you can show the existence of something by looking at every element of the set and finding an $$x$$ such that $$P(x)$$ is true. 

Let's go back to our food example:

>- $$F = \{$$Erik, Jos&eacute;, Nicoleta, Aksana$$\}$$
>- $$V = \{$$Aksana, Erik$$\}$$ is the set of your friends who are vegetarian
>- $$N = \{$$Aksana$$\}$$ is the set of your friends who are vegan
>- We want to prove: $$\exists x \in F,{} x \in N \implies x \in V$$

$$\begin{array}{l l l}
      1. & x = \textrm{Aksana}   & \textrm{Picked an }x \in F \\
      2. & x \in N = \texttt{True}  & \textrm{Given} \\
      3. & x \in V = \texttt{True} & \textrm{Given} \\
      4. & x \in N \implies x \in V = \texttt{True} & \textrm{Applied Def. of Implication to Lines 3 and 4 } \square  \\
    \end{array}$$

