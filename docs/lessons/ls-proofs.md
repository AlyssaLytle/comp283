---
layout: default
title: Proofs
contributors: Alyssa Byrnes
---



## Proofs

- Proofs are useful because they let you say something about the tools you're using and building! 
- In the real world, this is useful because it helps you explain your work and really convince people of your contribution.
- Proofs are also helpful because they force you to write down your thoughts. In writing down your thoughts, you might find out that your thinking is flawed or you're making assumptions where you shouldn't.  
- Examples of some things that you might prove:
   - This cryptography scheme is secure.
   - This new algorithm is the fastest out there.
   - This network will lose less than $$.001 \%$$ of the messages sent over it.
   - This new robot won't become sentient and kill you.



## What a proof looks like


- A good proof is like good code, clear and easy to follow! 
- When we were proving our logical equivalences, we always stated what equivalence we were using to get from one line to the next. You can think of this as something similar to commenting your code. You want the next person to read it to be able to follow your train of thought.
- We're going to write our proofs in this class in a specific way. As you advance in Computer Science or Math, you will find that you don't need to be this structured when writing proofs. You can think of this method as your "training wheels". The benefit of it is that it helps you practice writing down your reasoning in a linear way, and it helps you remember to justify every statement you make.






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
 



## Finding P and Q


### Example

- "If $$x$$ is even, $$x^2$$ is even." 
- $$P:$$ $$x$$ is even 
- $$Q:$$ $$x^2$$ is even
    






### Example


- "There are infinitely many primes." 
- This can be restated as "For all $$a \in \mathbb{Z}$$, if $$a$$ is prime, then there exists a prime $$b \in \mathbb{Z}$$ such that $$b>a$$.''  
- $$P:$$ $$a \in \mathbb{Z}$$ is prime 
- $$Q:$$ There exists $$b \in \mathbb{Z}$$ such that $$b>a$$ 






### Example
   
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




## Types of Proofs - Direct

 
 The first type of proof we will discuss is called a **direct proof**. Basically, we are trying to to prove $$p  \rightarrow q$$ by starting at $$p$$ and getting to $$q$$.
 
 For example, say we want to prove the following: "If $$x$$ is even, $$x^2$$ is even". 
 
 Then $$p$$ is "$$x$$ is even" and $$q$$ is "$$x^2$$ is even"
 
$$\begin{array}{l l l}
      1. & x \textrm{ is even} & \textrm{Given (In other words, this is our } p \textrm{)}\\
      2. & x = 2k, {} k \in \mathbb{Z} & \textrm{Definition of Even Number}\\
      3. & x^2 = (2k)^2 & \textrm{Squared both sides of Line 2} \\
      4. & x^2 = 4k^2 & \textrm{Simplified Line 3} \\
      5. & x^2 = 2(2k^2) & \textrm{Rewrote Line 4} \\
      6. & x^2 \textrm{ is even} & \textrm{Definition of Even Number } \square
    \end{array}$$
    
**Note that at every step you're basically saying, "Therefore..." this is where your implication $$\rightarrow$$ is coming in.**






## Example Proof




We want to show $$x-1 < \left \lfloor{x}\right \rfloor$$

 $$\begin{array}{l l l}
     1. & x = y + d, y \in \mathbb{Z}, d \in [0,1) & \textrm{Rewrite of x}  \\
     2. & d < 1 & \textrm{Defined in Line 1}\\
     3. & d - 1 < 0 & \textrm{Subtracted }1 \textrm{ from both sides of Line 2}\\
     4. & y + d - 1 < y & \textrm{Added } y \textrm{ to both sides}\\
     5. & x - 1 < y & \textrm{Plugged in Line 1 to Line 4.} \\
     6. & y = \left \lfloor{x}\right \rfloor & \textrm{Applied definition of floor to line 1.} \\
     7. & x - 1 < \left \lfloor{x}\right \rfloor & \textrm{Plugged line 6 into line 5. } \square 
 \end{array}$$  
 
 **Note that this is still a direct proof ($$p  \rightarrow q$$) but $$p$$ is never directly stated. If $$p$$ is never directly stated, you can just think of $$p$$ as your set of knowledge of the world.**
 




## Example Proof 2

 
Another example of this is when we do our logical equivalences.
 
 For example, you've previously proved $$\neg a \lor \neg(b \land \neg c) \equiv a  \rightarrow (b  \rightarrow c)$$.
 
 Since you are showing $$p \equiv q$$, you actually are showing $$p  \leftrightarrow q$$ rather than just $$p  \rightarrow q$$. 
 
 We could do this two ways. We could prove both $$p  \rightarrow q$$ and $$q  \rightarrow p$$, or we can consolidate it into one proof by using $$\leftrightarrow$$ at any step.
 
 We start at $$p$$: $$\neg a \lor \neg(b \land \neg c)$$ and use our equivalences to get to $$q$$: $$a  \rightarrow (b  \rightarrow c)$$.

 
 
 
 $$\begin{array}{l l l}
   1. & \neg a \lor \neg(b \land \neg c)  & \textrm{Given} \\
   2. & \equiv a  \rightarrow \neg(b \land \neg c) & \textrm{Implication Definition}\\
   3. & \equiv a  \rightarrow (\neg b \lor c) & \textrm{DeMorgan's}\\
   4. & \equiv a  \rightarrow (b  \rightarrow c) & \textrm{Implication Definition } \square \\
\end{array}$$




