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
$$$$\forall a\in A\  \exists b_1\in B\  \bigl((a,b_1)\in f
\bigr)\land \bigl(\forall b_2\in B\  ({(a,b_2)\in f} \implies {b_2 =
b_1}) \bigr).$$$$ 

Let's break this down...

- $$\forall a\in A\  \exists b_1\in B\  \bigl((a,b_1)\in f \bigr)$$ <br /> 
This is saying that for all $$a$$, there exists $$b_1$$ such that $$f(a)=b_1$$

- $$\bigl(\forall b_2\in B\  ({(a,b_2)\in f} \implies {b_2 =
b_1}) \bigr)$$ <br />
This is saying that if we find a $$b_2$$ such that $$f(a)=b_2$$, then $$b_1 = b_2$$ 
(aka $$f(a)$$ can only have one result)

## Some Things to Note...

- A function is a relation $$f \subseteq A \times B$$, 
which we can write as $$f: A \to B$$ <br /> This can be said as "$$f$$ maps $$A$$ to $$B$$"

- Using notation we've learned, $$\forall a\in A\ b\in B,\ \bigl((a,b)\in f \implies
(b=f(a))\bigr)$$

- Writing $$y=f(x)$$ rather than   $$(x,y)\in f$$ makes sense if and only if $$x$$ pairs with only one $$y$$.

- $$A$$ is called the **domain** and $$B$$ is the **range**.

## Composition

For, $$f: A \to B$$ and $$g: B \to C$$, 

$$h = g \circ f$$ is the **composition** of $$g$$ and $$f$$

which can also be written as $$h(a) = g(f(a))$$

Note that the output of $$f$$ has to be in the same set as the input for $$g$$! 

We will demonstrate this with an example...

## Composition Example

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

$$$$f(X) = \{f(x) | x \in X \}$$$$

This is called the *image* of $$X$$ under $$f$$.

We can also say,

$$$$f^{-1}(Y) = \{ x \in X | f(x) \in Y \}$$$$

This is called the *pre-image* of $$Y$$ under $$f$$.

## Applying Functions to Sets - Example

<img src="https://i.imgur.com/c7xFWjN.png" width="450"/>

- $$f(\{a,b,c,d\}) = \{h, i, j\}$$

- $$f^{-1}(\{h,i,j\}) = \{a,b,c,d\}$$

- $$f^{-1}(\{g,k\}) = \{\}$$

## Thinking about square roots...

Reminder: A  function  $$f$$ is a relation on $$A$$ and $$B$$ that maps
each $$a$$ from  $$A$$ 
to exactly one element $$b=f(a)$$ from $$B$$. 

So, is $$f(x) = \sqrt{x}$$ a function?

   - Answer: It depends!

- When $$A = \mathbb{R}$$ and $$B = \mathbb{R}$$?

    - No, because $$f(-1)$$ gives an answer that's not in the real numbers. ($$\sqrt{-1} \notin \mathbb{R}$$)

- When $$A = \mathbb{R}^+$$ and $$B = \mathbb{R}$$?

    - No, because $$\sqrt{4} = \pm 2$$. A function must map an input to only one answer.

- When $$A = \mathbb{R}^+$$ and $$B = \mathbb{R}^+$$?

    - Yes!

## Conditions to be a function
Say if $$f$$ is a relation on $$A$$ and $$B$$,

$$f(x)$$ is a function iff

1. For every $$x \in A$$, $$f(x) \in B$$

1. For every $$x \in A$$, there exists $$f(x) \in B$$

1.  For every $$x \in A$$, there exists *only one* $$f(x) \in B$$




## Common Function: Minimum

 **Minimum**: The element in a set with the lowest value.

$$x = \textrm{min}(A) \iff \forall y \in A, x \leq y$$

Note that if we can't explicitly define an $$x$$, then the minimum is undefined. 

### Example

- What is the minimum of $$\mathbb{Z}$$?

    - It's undefined, because the lowest element of $$\mathbb{Z}$$ can't be explicitly stated.

- What is the minimum of $$\{x \mid x \in [0,10]\}$$?

    - $$0$$

- What is the minimum of $$\{x \mid x \in (0,10)\}$$?

    - It's undefined.
    
## Demonstrating Minimum

Say we want to write code that checks if an element $$x$$ is the minimum element in set $$A$$.

First in English, let's write down what we want it to do:

Check each element $$y$$ in $$A$$ and see if $$x \leq y$$. If this is true for all $$y$$, then return True. If there is one $$y$$ where this is not true, return False. $$\leftarrow$$ (On assignments, when I tell you "explain to me in English how you would demonstrate this", this is what I mean!)

    1 check_min:
    2    input: integer x, set A
    3    
    4    #check each element in A
    5    for y in A:
    6        if y < x:
    7            return False 
    8    return True 

For line $$7$$, we only need to find one instance of y such that y<x to disprove that x is minimum, so we can return "False" here which exits the program

If we've made it to line $$8$$, we've exited the for loop. This means we've checked every element in $$A$$, and none returned "False", so we can return "True"

## Common Function: Argmin

**Argmin**: the index of the minimum element in tuple A. (If the minimum element appears twice, use the index of where it appears first.)

For tuple $$A = (a_1,a_2,\ldots,a_n)$$,

$$\textrm{argmin}(A) = i \iff \forall j \in [1,\ldots,n], (a_i < a_j) \lor (a_i \leq a_j \land i \leq j)$$

$$A = [10,12,7,13]$$

$$A[0] = 10, A[1] = 12, A[2] = 7, A[3] = 13$$

What is $$\textrm{argmin}(A)$$?

- $$2$$ because $$A[2]$$ is the smallest element in $$A$$.

## Common Function: Iverson Bracket

 **Iverson Bracket**: A proposition (usually in the form of a mathematical expression) in brackets, like $$[p]$$ that evaluates to $$1$$ if $$p$$ is True and $$0$$ if $$p$$ is False.

### Example:

$$[x>2] = \begin{cases} 
      0 & x\leq 2 \\
      1 & x > 2 
   \end{cases}$$



## Common Function: Signum
**signum**: returns the sign of a number

$$sgn(x) = \begin{cases}
    -1 & x<0\\
    0 & x =0\\
    1 & x>0
    \end{cases}$$
    


## Common Function: Absolute Value

**absolute value**: changes the sign of a value if the value is negative.

$$|x| = x$$

$$|-x| = x$$

Can we define this using signum?

- Yes! $$|x| = sgn(x) \cdot x$$

## Example: Proof by Cases

WTS: $$|x| = sgn(x) \cdot x$$

There are three cases: $$x>0$$, $$x = 0$$, $$x<0$$

- Case 1: $$x > 0$$

    - $$sgn(x) \cdot x = 1 \cdot x = x$$ and $$|x| = x$$, so $$|x| = sgn(x) \cdot x$$

- Case 2: $$x = 0$$

    - $$sgn(0) \cdot 0 = 0$$ and $$|0| = 0$$, so $$|x| = sgn(x) \cdot x$$

- Case 3: $$x < 0$$

    - $$sgn(x) \cdot x  = -1 \cdot x = -x$$ and $$|x| = -x$$, so $$|x| = sgn(x) \cdot x$$



## Types of Functions
Recall...

A  **function**  $$f$$ is a relation on $$A$$ and $$B$$ that maps each $$a$$ from  $$A$$ 
to exactly one element $$b=f(a)$$ from $$B$$.

$$\forall a\in A\  \exists b_1\in B\  \bigl((a,b_1)\in f
\bigr)\land \bigl(\forall b_2\in B\  ({(a,b_2)\in f} \implies {b_2 =
b_1}) \bigr).$$ 

Actually, the full term for this definition is a **total function**.

A  **partial function**  $$f$$ is a relation on $$A$$ and $$B$$ that maps each $$a$$ from  $$A$$ 
to *at most* one element $$b=f(a)$$ from $$B$$.

$$\forall a\in A\  \exists b_1\in B  \cancel{\bigl((a,b_1)\in f
\bigr)\land} \bigl(\forall b_2\in B  ({(a,b_2)\in f} \implies {b_2 =
b_1}) \bigr).$$ 

In other words, If $$x \in A$$, $$f(x)$$ doesn't *necessarily* evaluate.

### Example

>A common example of this is a computer program that only accepts certain inputs, and returns ERROR (or crashes) if it's not an acceptable input.




## Types of Functions: Injection

A function $$f: A \to B$$ is an **injection** iff each element of $$B$$ is hit by at most one element in $$A$$.

$$\forall x_1,x_2\in A, ~  \bigl(f(x_1)=f(x_2)\bigr) \implies (x_1=x_2).$$

Another logically equivalent way to state this is:

$$\forall x_1,x_2\in A, ~   (x_1{\neq}x_2)\implies \bigl(f(x_1){\ne}f(x_2)\bigr).$$

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
\bigr)\land \bigl(\forall_{a_2\in A}\  ({f(a_2)= b}) \implies ({a_2 =
a_1}) \bigr).$$

## Showing a Function is a Bijection

We are going to demonstrate how to prove a function is a bijection. We are also going to demonstrate how we can use what we've learned to prove other things!

- **Lemma**: If $$f$$ is its own inverse, then it is a bijection 

- $$f: A \to A$$ is its own inverse means $$\forall a \in A, f(f(a)) = a$$

- WTS: $$f$$ is surjective and injective

- Surjective: $$\forall y \in A, \exists x \in A f(x)=y$$

- > Let $$x = f(y), y \in A$$ 

- >$$f(x) = f(f(y)) = y \in A$$

- Injective: $$\forall x_1, x_2 \in A, (f(x_1) = f(x_2)) \implies x_1 = x_2$$

- > $$\forall x_1, x_2 \in A, (f(x_1) = f(x_2))$$

- > Apply $$f$$ to both sides: $$f(f(x_1)) = f(f(x_2))$$

- > Use the fact that $$f(f(a)) = a$$ to simplify: $$x_1 = x_2$$

## Pigeonhole Principle
<img src="http://2.bp.blogspot.com/-QEkXJPPdp04/U35B0uOl38I/AAAAAAAACDk/NqGdEWt5T3A/s1600/pigeonhole-principle1.gif" width="400"/>

The pigeonhole principle states: You can not fit $$n+1$$ pigeons into $$n$$ holes without having two pigeons share a hole.



## Pigeonhole Principle
Bringing it back to functions...

<img src="https://i.imgur.com/GizItRg.png"  width="400"/>

If you are mapping $$f: A \to B$$ and $$|A|>|B|$$, then there is no way to map from every element in $$A$$ without two of them hitting the same element in $$B$$. 


An airport with 1,500 landings a day must be able to accommodate
two planes landing in the same minute.

>- Why? There are $$1440$$ minutes in a day so, by the pigeonhole principle, if there are greater than $$1440$$ planes coming in, some planes will have to land in the same minute.



## How we can use it...

In a class of $$35$$ students, if a majority are women and a majority are
majoring in computer science, then at least one is both.

- Why? (Informal proof by contradiction. Start with false statement, and show that it leads to a contradiction. Aka show the negation is NOT true.)

- Let $$S=$$ set of all students, $$M=$$ set of all CS majors, $$W=$$  set of all women.  $$M \subseteq S$$ and $$W \subseteq S$$.

- "Majority are women" means $$|W| > \frac{35}{2}$$ or $$|W| \geq 18$$

- "Majority are majoring in computer science" means $$|M| > \frac{35}{2}$$ or $$|M| \geq 18$$


- If $$M \subseteq S$$ and $$W \subseteq S$$, then $$M \cup W \subseteq S$$ 

- If $$M \cup W \subseteq S$$, then $$|M \cup W| \leq |S|$$


- Negation: Assume no one is both a computer science major and a woman. ($$M \cap W = \{\}$$)

- Since $$M \cap W = \{\}$$, $$|M \cup W| = |M| + |W| \geq 18 + 18 = 36$$.

- $$|M \cup W| = 36$$ and $$|S| = 35$$, but $$|M \cup W| \leq |S|$$. $$\rightarrow \leftarrow$$


## Applying Pigeonhole Principle to Functions

- Recall: If you are mapping $$f: A \to B$$ and $$|A|>|B|$$, then there is no way to map from every element in $$A$$ without two of them hitting the same element in $$B$$. 

- Injection: each element of $$B$$ is hit by at most one element in $$A$$

- >So if $$|A| > |B|$$, by definition $$f$$ is not an injection. (Aka there are too many arrows coming from $$A$$.)

- Surjection: each element of $$B$$ is hit by at least one element in $$A$$

- >So if $$|A| < |B|$$, by definition $$f$$ is not a surjection. (Aka there are not enough arrows coming from $$A$$.)

- From this follows: $$f: A \to B$$ is a bijection $$\iff |A| = |B|$$ 

