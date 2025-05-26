---
layout: default
title: Functions
contributors: Alyssa Byrnes
---




## Functions

A  **function**  $$f$$ is a relation on $$A$$ and $$B$$ that maps
each $$a$$ from  $$A$$ 
to exactly one element $$b=f(a)$$ from $$B$$. 

Relation $$f\subseteq
A\times B$$ is a  function  iff  
$$\forall a\in A\  \exists b_1\in B\  \bigl((a,b_1)\in f
\bigr)\land \bigl(\forall b_2\in B\  ({(a,b_2)\in f} \rightarrow {b_2 =
b_1}) \bigr).$$

Let's break this down...

- $$\forall a\in A\  \exists b_1\in B\  \bigl((a,b_1)\in f \bigr)$$ <br> 
This is saying that for all $$a$$, there exists $$b_1$$ such that $$f(a)=b_1$$
- $$\bigl(\forall b_2\in B\  ({(a,b_2)\in f} \rightarrow {b_2 =
b_1}) \bigr)$$ <br />
This is saying that if we find a $$b_2$$ such that $$f(a)=b_2$$, then $$b_1 = b_2$$ 
(aka $$f(a)$$ can only have one result)




## Some Things to Note...


- A function is a relation $$f \subseteq A \times B$$, 
which we can write as $$f: A \to B$$ <br /> This can be said as "$$f$$ maps $$A$$ to $$B$$"
- Using notation we've learned, $$\forall a\in A\ b\in B,\ \bigl((a,b)\in f \rightarrow
(b=f(a))\bigr)$$
- Writing $$y=f(x)$$ rather than   $$(x,y)\in f$$ makes sense if and only if $$x$$ pairs with only one $$y$$.
- $$A$$ is called the **domain** and $$B$$ is the **range**.





## Composition


For, $$f: A \to B$$ and $$g: B \to C$$, 

$$h = g \circ f$$ is the **composition** of $$g$$ and $$f$$

which can also be written as $$h(a) = g(f(a))$$

Note that the output of $$f$$ has to be in the same set as the input for $$g$$! 

We will demonstrate this with an example...





### Example


$$f(x) = x$$ and $$g(x) = \frac{1}{x}$$

Say we define both the *domain* and *range* of $$f$$ as the integers, $$\mathbb{Z}$$, so $$f: \mathbb{Z} \to \mathbb{Z}$$

And we define the *domain* of $$g$$ to be $$\mathbb{Z}^{+}$$ (aka the positive integers)

(Note the domain can't be $$\mathbb{Z}$$ because  $$0 \in \mathbb{Z}$$, and you can't divide by zero!)

And we can define the *range* of *g* as the rational numbers, $$\mathbb{Q}$$, because it returns a fraction

so $$g: \mathbb{Z}^{+} \to \mathbb{Q}$$

Can you make a composition $$h = g \circ f$$?

- No, because $$f$$ could return something that can't be input into $$g$$ <br />
For example, <br />
$$f(0) = 0$$, and $$0 \notin \mathbb{Z}^{+}$$, so you can't compute $$g(f(0))$$




## Applying Functions to Tuples


We can apply functions to tuples. 

A common example is the Pythagorean Theorem.

$$$$ f(x,y) = \sqrt{x^2 + y^2}$$$$

Note that $$f: \mathbb{R} \times \mathbb{R} \to \mathbb{R}$$





## Applying Functions to Sets


We can also apply functions to sets.

Say that we have $$f: X \to Y$$

$$f(X) = \{f(x) \vert x \in X \}$$

This is called the *image* of $$X$$ under $$f$$.

We can also say,

$$f^{-1}(Y) = \{ x \in X \vert f(x) \in Y \}$$

This is called the *pre-image* of $$Y$$ under $$f$$.





## Applying Functions to Sets - Example

<img src="https://i.imgur.com/c7xFWjN.png" width="400"/>



> $$f(\{a,b,c,d\}) = \{h, i, j\}$$

> $$f^{-1}(\{h,i,j\}) = \{a,b,c,d\}$$

> $$f^{-1}(\{g,k\}) = \{\}$$



## Thinking about square roots...


Reminder: A  function  $$f$$ is a relation on $$A$$ and $$B$$ that maps
each $$a$$ from  $$A$$ 
to exactly one element $$b=f(a)$$ from $$B$$. 

* So, is $$f(x) = \sqrt{x}$$ a function? <br>
  * Answer: It depends! <br>
* When $$A = \mathbb{R}$$ and $$B = \mathbb{R}$$? <br>
  * No, because $$f(-1)$$ gives an answer that's not in the real numbers. <br>($$\sqrt{-1} \notin \mathbb{R}$$)<br>
* When $$A = \mathbb{R}^+$$ and $$B = \mathbb{R}$$?<br>
  * No, because $$\sqrt{4} = \pm 2$$. A function must map an input to only one answer.<br>
* When $$A = \mathbb{R}^+$$ and $$B = \mathbb{R}^+$$? <br>
  * Yes!





## Types of Functions

Recall...

A  **function**  $$f$$ is a relation on $$A$$ and $$B$$ that maps each $$a$$ from  $$A$$ 
to exactly one element $$b=f(a)$$ from $$B$$.

$$\forall a\in A\  \exists b_1\in B\  \bigl((a,b_1)\in f
\bigr)\land \bigl(\forall b_2\in B\  ({(a,b_2)\in f} \rightarrow {b_2 =
b_1}) \bigr).$$ 

Actually, the full term for this definition is a **total function**.

A  **partial function**  $$f$$ is a relation on $$A$$ and $$B$$ that maps each $$a$$ from  $$A$$ 
to *at most* one element $$b=f(a)$$ from $$B$$.

$$\forall a\in A\  \exists b_1\in B  \cancel{\bigl((a,b_1)\in f
\bigr)\land} \bigl(\forall b_2\in B  ({(a,b_2)\in f} \rightarrow {b_2 =
b_1}) \bigr).$$ 

In other words, If $$x \in A$$, $$f(x)$$ doesn't *necessarily* evaluate.

### Example

>A common example of this is a computer program that only accepts certain inputs, and returns ERROR (or crashes) if it's not an acceptable input.






## Types of Functions: Injection


A function $$f: A \to B$$ is an **injection** iff each element of $$B$$ is hit by at most one element in $$A$$.

$$\forall x_1,x_2\in A, ~  \bigl(f(x_1)=f(x_2)\bigr) \rightarrow (x_1=x_2).$$

Another logically equivalent way to state this is:

$$\forall x_1,x_2\in A, ~   (x_1{\neq}x_2)\rightarrow \bigl(f(x_1){\ne}f(x_2)\bigr).$$

This logical definition inspires the other term for an injection which is **one-to-one** because one input maps to one output. 

This term doesn't quite capture the full meaning though because, by definition, all functions map one input to one output. 





## Types of Functions: surjection


A function $$f: A\to B$$ is a **surjection**,
or  **onto**, if and only if every element of $$B$$ is hit by at least one element in $$A$$.

$$\forall y \in B ~ \exists x \in A, ~   f(x)=y$$.

In other words, $$f(A)=B$$. 






## Types of Functions: bijection

A function $$f: A\to B$$ is a **bijection**
if and only if it is an injection and a surjection.

$$\forall b\in B, ~  \exists a_1 \in A, ~  \bigl(f(a_1)=b
\bigr)\land \bigl(\forall_{a_2\in A}\  ({f(a_2)= b}) \rightarrow ({a_2 =
a_1}) \bigr).$$





## Showing a Function is a Bijection


We are going to demonstrate how to prove a function is a bijection. We are also going to demonstrate how we can use what we've learned to prove other things!

- **Lemma**: If $$f$$ is its own inverse, then it is a bijection <br>
- $$f: A \to A$$ is its own inverse means $$\forall a \in A, f(f(a)) = a$$ <br>
- WTS: $$f$$ is surjective and injective <br>
- Surjective: $$\forall y \in A, \exists x \in A f(x)=y$$<br>
    - Let $$x = f(y), y \in A$$ <br>
    - $$f(x) = f(f(y)) = y \in A$$ <br>
- Injective: $$\forall x_1, x_2 \in A, (f(x_1) = f(x_2)) \rightarrow x_1 = x_2$$ <br>
    - $$\forall x_1, x_2 \in A, (f(x_1) = f(x_2))$$ <br>
    - Apply $$f$$ to both sides: $$f(f(x_1)) = f(f(x_2))$$ <br>
    - Use the fact that $$f(f(a)) = a$$ to simplify: $$x_1 = x_2$$



## Pigeonhole Principle

<img src="http://2.bp.blogspot.com/-QEkXJPPdp04/U35B0uOl38I/AAAAAAAACDk/NqGdEWt5T3A/s1600/pigeonhole-principle1.gif" width="400"/>

The pigeonhole principle states: You can not fit $$n+1$$ pigeons into $$n$$ holes without having two pigeons share a hole.


Bringing it back to functions...

<img src="https://i.imgur.com/GizItRg.png"  width="400"/>

If you are mapping $$f: A \to B$$ and $$\vert A\vert >\vert B\vert $$, then there is no way to map from every element in $$A$$ without two of them hitting the same element in $$B$$. 




### How we can use it...

### Example 1

An airport with 1,500 landings a day must be able to accommodate
two planes landing in the same minute.

- Why? There are $$1440$$ minutes in a day so, by the pigeonhole principle, if there are greater than $$1440$$ planes coming in, some planes will have to land in the same minute.


### Example 2

In a class of $$35$$ students, if a majority are women and a majority are
majoring in computer science, then at least one is both.

- Why? (Informal proof by contradiction. Start with false statement, and show that it leads to a contradiction. Aka show the negation is NOT true.)
- Let $$S=$$ set of all students, $$M=$$ set of all CS majors, $$W=$$  set of all women.  $$M \subseteq S$$ and $$W \subseteq S$$.
- "Majority are women" means $$\vert W\vert > \frac{35}{2}$$ or $$\vert W\vert \geq 18$$
- "Majority are majoring in computer science" means $$\vert M\vert > \frac{35}{2}$$ or $$\vert M\vert \geq 18$$
- If $$M \subseteq S$$ and $$W \subseteq S$$, then $$M \cup W \subseteq S$$ 
- If $$M \cup W \subseteq S$$, then $$\vert M \cup W\vert \leq \vert S\vert $$
- Negation: Assume no one is both a computer science major and a woman. ($$M \cap W = \{\}$$)
- Since $$M \cap W = \{\}$$, $$\vert M \cup W\vert = \vert M\vert + \vert W\vert \geq 18 + 18 = 36$$.
- $$\vert M \cup W\vert = 36$$ and $$\vert S\vert = 35$$, but $$\vert M \cup W\vert \leq \vert S\vert $$. $$\rightarrow \leftarrow$$



## Applying Pigeonhole Principle to Functions


- Recall: If you are mapping $$f: A \to B$$ and $$\vert A\vert >\vert B\vert $$, then there is no way to map from every element in $$A$$ without two of them hitting the same element in $$B$$. 
- Injection: each element of $$B$$ is hit by at most one element in $$A$$
- So if $$\vert A\vert > \vert B\vert $$, by definition $$f$$ is not an injection. (Aka there are too many arrows coming from $$A$$.)
- Surjection: each element of $$B$$ is hit by at least one element in $$A$$
- So if $$\vert A\vert < \vert B\vert $$, by definition $$f$$ is not a surjection. (Aka there are not enough arrows coming from $$A$$.)
- From this follows: $$f: A \to B$$ is a bijection $$\iff \vert A\vert = \vert B\vert $$ 



## Implications of Pigeonhole Principle


- $$f: A \to B$$ is a bijection $$\iff \vert A\vert = \vert B\vert $$
- Think about what this means if $$A$$ and $$B$$ are infinite sets...
- Let $$A = \mathbb{N}$$ and $$B = \mathbb{Z}$$
- If we can show there exists a bijection $$f:  \mathbb{N} \to \mathbb{Z}$$, then 
$$\vert \mathbb{N}\vert = \vert \mathbb{Z}\vert $$!
- (We can! Try it at home!)
- A set is called **countably infinite** (or denumerable) if it can be put in bijective correspondence with the set of natural numbers. 
- A set is called **countable** if it is either finite or countably infinite.



## Measuring Size of Inputs


- Computers have size and memory limits, so it's important that we can analyze our algorithms so that we know they are something the computer can handle.
- Commonly, we use **asymptotic notation** to describe runtime. 
- "Big O": $$O$$ is used to measure the worst case scenario of an input.<br>(In other words, it is an upper bound.)
- $$f \in O(g(n)) \iff \exists c \in \mathbb{R}^{+}, \exists N \in \mathbb{N}, \forall n < N, 0 \leq f(n) \leq c \cdot g(n)$$ 
- $$\Omega$$ is used to measure the best case scenario of an input. (In other words, it is an lower bound.)
- $$f \in \Omega(g(n)) \iff \exists c \in \mathbb{R}^{+}, \exists N \in \mathbb{N}, \forall n < N, 0 \leq c \cdot g(n) \leq f(n)$$ 
- $$\Theta$$ is used to describe a function that is both in $$O$$ and $$\Omega$$.
- $$f \in \Theta(g(n))$$<br> $$\iff \exists c_L, c_H \in \mathbb{R}^{+}, \exists N \in \mathbb{N}, \forall n < N, 0 \leq c_L \cdot g(n) \leq f(n) \leq c_H \cdot g(n)$$ 




