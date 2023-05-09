---
layout: default
title: ProofsNotes
contributors: Alyssa Byrnes
---

## Proofs
- Proofs are useful because they let you say something about the tools you're using and building! 

- In the real world, this is useful because it helps you explain your work and really convince people of your contribution.

- Proofs are also helpful because they force you to write down your thoughts. In writing down your thoughts, you might find out that your thinking is flawed or you're making assumptions where you shouldn't.  

- Examples of some things that you might prove:

- > This cryptography scheme is secure.
- > This new algorithm is the fastest out there.
- > This network will lose less than $$.001 \%$$ of the messages sent over it.
- > This new robot won't become sentient and kill you.


- A good proof is like good code, clear and easy to follow! 

- When we were proving our logical equivalences, we always stated what equivalence we were using to get from one line to the next. You can think of this as something similar to commenting your code. You want the next person to read it to be able to follow your train of thought.

- We're going to write our proofs in this class in a specific way. As you advance in Computer Science or Math, you will find that you don't need to be this structured when writing proofs. You can think of this method as your "training wheels". The benefit of it is that it helps you practice writing down your reasoning in a linear way, and it helps you remember to justify every statement you make.



## What a proof looks like

The two column format looks like this: 

$$\begin{array}{l l l}
 & \textrm{Column 1} & \textrm{Column 2} \\
 \hline
    1. & \textrm{Your conclusion} & \textrm{How you came to that conclusion}  \\
     2. & \ldots\\
     3. & \ldots\\
     \vdots \\
      \square 
 \end{array}$$
 

 
 
## Types of Proofs - Direct
 
 The first type of proof we will discuss is called a **direct proof**. Basically, we are trying to to prove $$p \implies q$$ by starting at $$p$$ and getting to $$q$$.
 
 For example, say we want to prove the following: "If $$x$$ is even, $$x^2$$ is even". 
 
 Then $$p$$ is "$$x$$ is even" and $$q$$ is "$$x^2$$ is even"
 
    
**Note that at every step you're basically saying, "Therefore..." this is where your implication $$\implies$$ is coming in.**




## Example Proof

We want to show $$x-1 < \left \lfloor{x}\right \rfloor$$

 
 **Note that this is still a direct proof ($$p \implies q$$) but $$p$$ is never directly stated. If $$p$$ is never directly stated, you can just think of $$p$$ as your set of knowledge of the world.**
 


## Example Proof 2
 
  Another example of this is when we do our logical equivalences.
 
 For example, on the midterm you proved $$\neg a \lor \neg(b \land \neg c) \equiv a \implies (b \implies c)$$.
 
 Since you are showing $$p \equiv q$$, you actually are showing $$p \iff q$$ rather than just $$p \implies q$$. 
 
 We could do this two ways. We could prove both $$p \implies q$$ and $$q \implies p$$, or we can consolidate it into one proof by using $$\iff$$ at any step.
 
 We start at $$p$$: $$\neg a \lor \neg(b \land \neg c)$$ and using our equivalences to get to $$q$$: $$a \implies (b \implies c)$$.

 
 



## Types of Proofs - Forall


You may want to prove statements such as "$$\forall x \in S, P(x)$$."

As previously discussed, to prove a "for all" statement, you want to look at every element in $$S$$ and show that $$P(x)$$ holds. 

You can often do this with a direct proof. All of the things we've directly proved so far are actually "for all" proofs.

- $$\forall x \in \mathbb{Z}$$, If $$x$$ is even, $$x^2$$ is even
- $$\forall x \in \mathbb{Z}, {} x-1 < \left \lfloor{x}\right \rfloor$$
- $$\forall a,b,c \in \{\texttt{True}, \texttt{False}\}, {} \neg a \lor \neg(b \land \neg c) \equiv a \implies (b \implies c)$$
- $$\forall p,q,r \in \{\texttt{True}, \texttt{False}\}, {} p \implies q \equiv \neg q \implies \neg p$$
- $$\forall a,b,c \in \mathbb{Z}$$, if $$a \mid b$$ and $$b \mid c$$, then $$a \mid c$$

## Types of Proofs - Forall, Exhaustive

However, we can also prove "for all" statements by exhaustively looking at every element in $$S$$ and checking if $$P(x)$$ holds.

- $$P = \{$$Erik, Jos&eacute;, Nicoleta, Aksana$$\}$$
- $$V = \{$$Aksana, Erik$$\}$$ is the set of your friends who are vegetarian
- $$N = \{$$Aksana$$\}$$ is the set of your friends who are vegan
- We want to prove: $$\forall x, x \in N \implies x \in V$$

## Types of Proofs - Exhaustive

However, we can also prove "for all" statements by *exhaustively* looking at every element in $$S$$ and checking if $$P(x)$$ holds. 

Fittingly, this is called a **Proof by Exhaustion**.

A good example is the set problem you've already seen:

>- $$P = \{$$Erik, Jos&eacute;, Nicoleta, Aksana$$\}$$
>- $$V = \{$$Aksana, Erik$$\}$$ is the set of your friends who are vegetarian
>- $$N = \{$$Aksana$$\}$$ is the set of your friends who are vegan
>- We want to prove: $$\forall x, x \in N \implies x \in V$$

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
    


