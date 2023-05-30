---
title: Functions
theme: dracula
center: false
transition: 'none'
contributors: Alyssa Byrnes
---


<div id="content">


</div>


## Functions
<div id="content">
A  **function**  $f$ is a relation on $A$ and $B$ that maps
each $a$ from  $A$ 
to exactly one element $b=f(a)$ from $B$. 

Relation $f\subseteq
A\times B$ is a  function  iff  
$$\forall a\in A\  \exists b_1\in B\  \bigl((a,b_1)\in f
\bigr)\land \bigl(\forall b_2\in B\  ({(a,b_2)\in f} \rightarrow {b_2 =
b_1}) \bigr).$$ 

Let's break this down...

- $\forall a\in A\  \exists b_1\in B\  \bigl((a,b_1)\in f \bigr)$ <br> 
This is saying that for all $a$, there exists $b_1$ such that $f(a)=b_1$
- $\bigl(\forall b_2\in B\  ({(a,b_2)\in f} \rightarrow {b_2 =
b_1}) \bigr)$ <br />
This is saying that if we find a $b_2$ such that $f(a)=b_2$, then $b_1 = b_2$ 
(aka $f(a)$ can only have one result)

</div>


## Some Things to Note...
<div id="content">

- A function is a relation $f \subseteq A \times B$, 
which we can write as $f: A \to B$ <br /> This can be said as "$f$ maps $A$ to $B$"
- Using notation we've learned, $\forall a\in A\ b\in B,\ \bigl((a,b)\in f \rightarrow
(b=f(a))\bigr)$
- Writing $y=f(x)$ rather than   $(x,y)\in f$ makes sense if and only if $x$ pairs with only one $y$.
- $A$ is called the **domain** and $B$ is the **range**.


</div>


## Composition
<div id="content">

For, $f: A \to B$ and $g: B \to C$, 

$h = g \circ f$ is the **composition** of $g$ and $f$

which can also be written as $h(a) = g(f(a))$

Note that the output of $f$ has to be in the same set as the input for $g$! 

We will demonstrate this with an example...


</div>


## Composition Example

<div id="content">
$f(x) = x$ and $g(x) = \frac{1}{x}$

Say we define both the *domain* and *range* of $f$ as the integers, $\mathbb{Z}$, so $f: \mathbb{Z} \to \mathbb{Z}$

And we define the *domain* of $g$ to be $\mathbb{Z}^{+}$ (aka the positive integers)

(Note the domain can't be $\mathbb{Z}$ because  $0 \in \mathbb{Z}$, and you can't divide by zero!)

And we can define the *range* of *g* as the rational numbers, $\mathbb{Q}$, because it returns a fraction

so $g: \mathbb{Z}^{+} \to \mathbb{Q}$

Can you make a composition $h = g \circ f$?

- No, because $f$ could return something that can't be input into $g$ <br />
For example, <br />
$f(0) = 0$, and $0 \notin \mathbb{Z}^{+}$, so you can't compute $g(f(0))$
</div>



## Applying Functions to Tuples
<div id="content">

We can apply functions to tuples. 

A common example is the Pythagorean Theorem.

$$ f(x,y) = \sqrt{x^2 + y^2}$$

Note that $f: \mathbb{R} \times \mathbb{R} \to \mathbb{R}$


</div>


## Applying Functions to Sets
<div id="content">

We can also apply functions to sets.

Say that we have $f: X \to Y$

$$f(X) = \{f(x) | x \in X \}$$

This is called the *image* of $X$ under $f$.

We can also say,

$$f^{-1}(Y) = \{ x \in X | f(x) \in Y \}$$

This is called the *pre-image* of $Y$ under $f$.


</div>


## Applying Functions to Sets - Example
<div id="left">
<img src="https://i.imgur.com/c7xFWjN.png" width="400"/>
</div>

<div id="right" class="incremental">
- $f(\{a,b,c,d\}) = \{h, i, j\}$
- $f^{-1}(\{h,i,j\}) = \{a,b,c,d\}$
- $f^{-1}(\{g,k\}) = \{\}$
</div>


## Thinking about square roots...
<div id="content" class="incremental">

Reminder: A  function  $f$ is a relation on $A$ and $B$ that maps
each $a$ from  $A$ 
to exactly one element $b=f(a)$ from $B$. 

* So, is $f(x) = \sqrt{x}$ a function? <br>
  * Answer: It depends! <br>
* When $A = \mathbb{R}$ and $B = \mathbb{R}$? <br>
  * No, because $f(-1)$ gives an answer that's not in the real numbers. <br>($\sqrt{-1} \notin \mathbb{R}$)<br>
* When $A = \mathbb{R}^+$ and $B = \mathbb{R}$?<br>
  * No, because $\sqrt{4} = \pm 2$. A function must map an input to only one answer.<br>
* When $A = \mathbb{R}^+$ and $B = \mathbb{R}^+$? <br>
  * Yes!
</div>





## Common Function: Minimum
<div id="content">

 **Minimum**: The element in a set with the lowest value.

$x = \textrm{min}(A) \iff \forall y \in A, x \leq y$

Note that if we can't explicitly define an $x$, then the minimum is undefined. 

### Example

- What is the minimum of $\mathbb{Z}$? <br>
    - It's undefined, because the lowest element of $\mathbb{Z}$ can't be explicitly stated. <br>
- What is the minimum of $\{x \mid x \in [0,10]\}$? <br>
    - $0$ <br>
- What is the minimum of $\{x \mid x \in (0,10)\}$? <br>
    - It's undefined. <br>

</div>


## Demonstrating Minimum
<div id="content">

Say we want to write code that checks if an element $x$ is the minimum element in set $A$.

First in English, let's write down what we want it to do:

Check each element $y$ in $A$ and see if $x \leq y$. If this is true for all $y$, then return True. If there is one $y$ where this is not true, return False. $\leftarrow$ (On assignments, when I tell you "explain to me in English how you would demonstrate this", this is what I mean!)


</div>


## Demonstrating Minimum
<div id="content">

Say we want to write code that checks if an element $x$ is the minimum element in set $A$.

First in English, let's write down what we want it to do:

Check each element $y$ in $A$ and see if $x \leq y$. If this is true for all $y$, then return True. If there is one $y$ where this is not true, return False. $\leftarrow$ (On assignments, when I tell you "explain to me in English how you would demonstrate this", this is what I mean!)

    1 check_min:
    2    input: integer x, set A
    3    
    4    #check each element in A
    5    for y in A:
    6        if y < x:
    7            return False 
    8    return True 

For line $7$, we only need to find one instance of y such that y<x to disprove that x is minimum, so we can return "False" here which exits the program

If we've made it to line $8$, we've exited the for loop. This means we've checked every element in $A$, and none returned "False", so we can return "True"


</div>


## Common Function: Argmin
<div id="content">

**Argmin**: the index of the minimum element in tuple A. (If the minimum element appears twice, use the index of where it appears first.)

For tuple $A = (a_1,a_2,\ldots,a_n)$,

$\textrm{argmin}(A) = i \iff \forall j \in [1,\ldots,n], (a_i < a_j) \lor (a_i \leq a_j \land i \leq j)$

### Example:

$A = [10,12,7,13]$

$A[0] = 10, A[1] = 12, A[2] = 7, A[3] = 13$

What is $\textrm{argmin}(A)$?

- $2$ because $A[2]$ is the smallest element in $A$.


</div>


## Common Function: Iverson Bracket
<div id="content">

 **Iverson Bracket**: A proposition (usually in the form of a mathematical expression) in brackets, like $[p]$ that evaluates to $1$ if $p$ is True and $0$ if $p$ is False.

### Example:

$[x>2] = \begin{cases} 
      0 & x\leq 2 \\
      1 & x > 2 
   \end{cases}$


</div>


## Common Function: Signum
<div id="content">
**signum**: returns the sign of a number

$sgn(x) = \begin{cases}
    -1 & x<0\\
    0 & x =0\\
    1 & x>0
    \end{cases}$
    

</div>


## Common Function: Absolute Value
<div id="content">

**absolute value**: changes the sign of a value if the value is negative.

$|x| = x$

$|-x| = x$

Can we define this using signum?

- Yes! $|x| = sgn(x) \cdot x$


</div>


## Example: Proof by Cases
<div id="content">

WTS: $|x| = sgn(x) \cdot x$

There are three cases: $x>0$, $x = 0$, $x<0$

- Case 1: $x > 0$<br>
    - $sgn(x) \cdot x = 1 \cdot x = x$ and $|x| = x$, so $|x| = sgn(x) \cdot x$<br>
- Case 2: $x = 0$<br>
    - $sgn(0) \cdot 0 = 0$ and $|0| = 0$, so $|x| = sgn(x) \cdot x$<br>
- Case 3: $x < 0$ <br>
    - $sgn(x) \cdot x  = -1 \cdot x = -x$ and $|x| = -x$, so $|x| = sgn(x) \cdot x$ <br>


</div>


## Types of Functions
<div id="smalltext">
Recall...

A  **function**  $f$ is a relation on $A$ and $B$ that maps each $a$ from  $A$ 
to exactly one element $b=f(a)$ from $B$.

$\forall a\in A\  \exists b_1\in B\  \bigl((a,b_1)\in f
\bigr)\land \bigl(\forall b_2\in B\  ({(a,b_2)\in f} \rightarrow {b_2 =
b_1}) \bigr).$ 

Actually, the full term for this definition is a **total function**.

</div>


## Types of Functions
<div id="smalltext">
Recall...

A  **function**  $f$ is a relation on $A$ and $B$ that maps each $a$ from  $A$ 
to exactly one element $b=f(a)$ from $B$.

$\forall a\in A\  \exists b_1\in B\  \bigl((a,b_1)\in f
\bigr)\land \bigl(\forall b_2\in B\  ({(a,b_2)\in f} \rightarrow {b_2 =
b_1}) \bigr).$ 

Actually, the full term for this definition is a **total function**.

A  **partial function**  $f$ is a relation on $A$ and $B$ that maps each $a$ from  $A$ 
to *at most* one element $b=f(a)$ from $B$.

$\forall a\in A\  \exists b_1\in B  \cancel{\bigl((a,b_1)\in f
\bigr)\land} \bigl(\forall b_2\in B  ({(a,b_2)\in f} \rightarrow {b_2 =
b_1}) \bigr).$ 

In other words, If $x \in A$, $f(x)$ doesn't *necessarily* evaluate.

### Example

>A common example of this is a computer program that only accepts certain inputs, and returns ERROR (or crashes) if it's not an acceptable input.



</div>


## Types of Functions: Injection
<div id="content">

A function $f: A \to B$ is an **injection** iff each element of $B$ is hit by at most one element in $A$.

$\forall x_1,x_2\in A, ~  \bigl(f(x_1)=f(x_2)\bigr) \rightarrow (x_1=x_2).$

Another logically equivalent way to state this is:

$\forall x_1,x_2\in A, ~   (x_1{\neq}x_2)\rightarrow \bigl(f(x_1){\ne}f(x_2)\bigr).$

This logical definition inspires the other term for an injection which is **one-to-one** because one input maps to one output. 

This term doesn't quite capture the full meaning though because, by definition, all functions map one input to one output. 


</div>


## Types of Functions: surjection
<div id="content">

A function $f: A\to B$ is a **surjection**,
or  **onto**, if and only if every element of $B$ is hit by at least one element in $A$.

$\forall y \in B ~ \exists x \in A, ~   f(x)=y$.

In other words, $f(A)=B$. 



</div>


## Types of Functions: bijection
<div id="content">
A function $f: A\to B$ is a **bijection**
if and only if it is an injection and a surjection.

$\forall b\in B, ~  \exists a_1 \in A, ~  \bigl(f(a_1)=b
\bigr)\land \bigl(\forall_{a_2\in A}\  ({f(a_2)= b}) \rightarrow ({a_2 =
a_1}) \bigr).$


</div>


## Showing a Function is a Bijection
<div id="content">

We are going to demonstrate how to prove a function is a bijection. We are also going to demonstrate how we can use what we've learned to prove other things!

- **Lemma**: If $f$ is its own inverse, then it is a bijection <br>
- $f: A \to A$ is its own inverse means $\forall a \in A, f(f(a)) = a$ <br>
- WTS: $f$ is surjective and injective <br>
- Surjective: $\forall y \in A, \exists x \in A f(x)=y$<br>
    - Let $x = f(y), y \in A$ <br>
    - $f(x) = f(f(y)) = y \in A$ <br>
- Injective: $\forall x_1, x_2 \in A, (f(x_1) = f(x_2)) \rightarrow x_1 = x_2$ <br>
    - $\forall x_1, x_2 \in A, (f(x_1) = f(x_2))$ <br>
    - Apply $f$ to both sides: $f(f(x_1)) = f(f(x_2))$ <br>
    - Use the fact that $f(f(a)) = a$ to simplify: $x_1 = x_2$
</div>


## Pigeonhole Principle
<div id="content">
<img src="http://2.bp.blogspot.com/-QEkXJPPdp04/U35B0uOl38I/AAAAAAAACDk/NqGdEWt5T3A/s1600/pigeonhole-principle1.gif" width="400"/>

The pigeonhole principle states: You can not fit $n+1$ pigeons into $n$ holes without having two pigeons share a hole.
</div>


## Pigeonhole Principle
<div id="content">
Bringing it back to functions...

<img src="https://i.imgur.com/GizItRg.png"  width="400"/>

If you are mapping $f: A \to B$ and $|A|>|B|$, then there is no way to map from every element in $A$ without two of them hitting the same element in $B$. 



</div>


## How we can use it...
<div id="content" class="incremental">

An airport with 1,500 landings a day must be able to accommodate
two planes landing in the same minute.

- Why? There are $1440$ minutes in a day so, by the pigeonhole principle, if there are greater than $1440$ planes coming in, some planes will have to land in the same minute.


</div>


## How we can use it...
<div id="content" class="incremental">

In a class of $35$ students, if a majority are women and a majority are
majoring in computer science, then at least one is both.

- Why? (Informal proof by contradiction. Start with false statement, and show that it leads to a contradiction. Aka show the negation is NOT true.)
- Let $S=$ set of all students, $M=$ set of all CS majors, $W=$  set of all women.  $M \subseteq S$ and $W \subseteq S$.
- "Majority are women" means $|W| > \frac{35}{2}$ or $|W| \geq 18$
- "Majority are majoring in computer science" means $|M| > \frac{35}{2}$ or $|M| \geq 18$
- If $M \subseteq S$ and $W \subseteq S$, then $M \cup W \subseteq S$ 
- If $M \cup W \subseteq S$, then $|M \cup W| \leq |S|$
- Negation: Assume no one is both a computer science major and a woman. ($M \cap W = \{\}$)
- Since $M \cap W = \{\}$, $|M \cup W| = |M| + |W| \geq 18 + 18 = 36$.
- $|M \cup W| = 36$ and $|S| = 35$, but $|M \cup W| \leq |S|$. $\rightarrow \leftarrow$
</div>


## Applying Pigeonhole Principle to Functions
<div id="content" class="incremental">

- Recall: If you are mapping $f: A \to B$ and $|A|>|B|$, then there is no way to map from every element in $A$ without two of them hitting the same element in $B$. 
- Injection: each element of $B$ is hit by at most one element in $A$
- So if $|A| > |B|$, by definition $f$ is not an injection. (Aka there are too many arrows coming from $A$.)
- Surjection: each element of $B$ is hit by at least one element in $A$
- So if $|A| < |B|$, by definition $f$ is not a surjection. (Aka there are not enough arrows coming from $A$.)
- From this follows: $f: A \to B$ is a bijection $\iff |A| = |B|$ 
</div>


## Implications of Pigeonhole Principle
<div id="content" class="incremental">

- $f: A \to B$ is a bijection $\iff |A| = |B|$
- Think about what this means if $A$ and $B$ are infinite sets...
- Lets $A = \mathbb{N}$ and $B = \mathbb{Z}$
- If we can show there exists a bijection $f:  \mathbb{N} \to \mathbb{Z}$, then 
$|\mathbb{N}| = |\mathbb{Z}|$!
- (We can! Try it at home!)
- A set is called **countably infinite** (or denumerable) if it can be put in bijective correspondence with the set of natural numbers. 
- A set is called **countable** if it is either finite or countably infinite.
</div>


## Measuring Size of Inputs
<div id="content" class="incremental">

- Computers have size and memory limits, so it's important that we can analyze our algorithms so that we know they are something the computer can handle.
- Commonly, we use **asymptotic notation** to describe runtime. 
- "Big O": $O$ is used to measure the worst case scenario of an input.<br>(In other words, it is an upper bound.)
- $f \in O(g(n)) \iff \exists c \in \mathbb{R}^{+}, \exists N \in \mathbb{N}, \forall n < N, 0 \leq f(n) \leq c \cdot g(n)$ 
- $\Omega$ is used to measure the best case scenario of an input. (In other words, it is an lower bound.)
- $f \in \Omega(g(n)) \iff \exists c \in \mathbb{R}^{+}, \exists N \in \mathbb{N}, \forall n < N, 0 \leq c \cdot g(n) \leq f(n)$ 
- $\Theta$ is used to describe a function that is both in $O$ and $\Omega$.
- $f \in \Theta(g(n))$<br> $\iff \exists c_L, c_H \in \mathbb{R}^{+}, \exists N \in \mathbb{N}, \forall n < N, 0 \leq c_L \cdot g(n) \leq f(n) \leq c_H \cdot g(n)$ 

</div>


