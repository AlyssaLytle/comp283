---
title: Number Theory
theme: dracula
center: false
transition: 'none'
contributors: Alyssa Byrnes
---


## Useful Operators - Floor and Ceiling
<div id="content">

The **floor** operator, denoted $\left \lfloor{x}\right \rfloor$, tells us the greatest integer $\leq x$.

The **ceiling** operator, denoted $\left \lceil{x}\right \rceil$,  tells us the smallest integer $\geq x$.

(Basically, they're just fancy ways of saying "round down" and "round up")

### Example

- $\left \lfloor{7.5}\right \rfloor = 7$ <br>
- $\left \lceil{7.5}\right \rceil = 8$



</div>


## Property of Floor
<div id="content">
$x-1 < \left \lfloor{x}\right \rfloor \leq x$

- Why?
- By definition, we know $\left \lfloor{x}\right \rfloor \leq x$
- We know $x-1 < \left \lfloor{x}\right \rfloor$ because:
    - We can write $x$ as $x = y + d$ where $y$ is an integer and $d$ is a decimal. (E.g. $7.5 = 7 + .5$)
    - We know $\left \lfloor{x}\right \rfloor = y$ and that $d$ is some real number such that $0 \leq d < 1$.
    - We know $d < 1$, so $d-1$ is negative, therefore $y + d - 1 < y$.
    - So $x - 1 = y + d - 1 < y = \left \lfloor{x}\right \rfloor$ 
</div>


## Property of Ceiling
<div id="content">

$x \leq \left \lceil{x}\right \rceil < x + 1$

- (You can prove this similarly to the way we proved the floor property!)

</div>


## Bases
<div id="content">

We usually represent numbers in base ten

<img src="https://i.imgur.com/8dmbsc7.png" width="600"/>


</div>


## Bases
<div id="content">

- In general, a number in the form of digits $d_k d_{k-1} \ldots d_1 d_0$ can be represented as
$$\sum_{i\in[0,k]}d_i t^i = d_kt^k + d_{k-1}t^{k-1}+ \ldots + d_1t^1 + d_0t^0$$ where $t$ is the base
- All digits $d_i$ are in the range $[0,t-1]$

### Example

- Let's go back to representing the number $10,475$ in base $10$
- So the digits are $d_4 = 1$, $d_3 = 0$, $d_2 = 4$, $d_1 = 7$, $d_0 = 5$ and the base is $t = 10$
- Which gives us what we got before: $10,475 = 1 \cdot 10^4 + 0 \cdot 10^3 + 4 \cdot 10^2 + 7 \cdot 10^1 + 5 \cdot 10^0$
- Also note that all digits are between $0$ and $9$.
</div>


## Base 2
<div id="left">

- Often in computer science, we represent numbers in base $2$. This is also called "binary" representation.
- Since our base $t = 2$, then our digits are in the range $[0,1]$. So basically, we are just looking at strings of $0$s and $1$s. <br> (Often we call $0$s and $1$s "bits". $8$ bits is a byte.)

</div>

<div id="right">

<img src="https://i.imgur.com/brCatgF.png" width="500"/>


</div>


<!-- ## In Class Assignment
<div id="content">

In groups, write (in English) the procedure for converting a number from binary to base 10. 

Then, write the procedure for converting a number from base 10 to binary.

Hint: start by thinking what steps would you take to convert $10110$ to $22$ and $22$ to $10110$, then generalize it to any number.

You can submit this as a group on Gradescope!

(It's okay if you're wrong! We will go over the right answer after you submit. The idea is to just see that you put effort in.)


</div> -->


## Length of Binary Messages 
<div id="content">

If I want to express $x$ in binary, how long will it be? 

(In other words, how many bits will it take?)

-  Think about the procedure we just did for converting a number to binary. We find the highest power of $2$ that is less than or equal to $x$: $k = \left \lfloor{\log_2(x)}\right \rfloor$
-  We know this means that our string of bits will be of length $k$.
-  This can be generalized for any base $b$: The length of any number $x$ in base $b$ is $\left \lfloor{\log_b(x)}\right \rfloor$

</div>


<!-- ## Length of Binary Messages
<div id="content">

- While it makes sense to represent numbers in binary for computers, notice that it takes more digits to represent them. Think about it. Saying "$10110$" instead of "$22$" is longer. 
- So why do we do it? (I'll link to a video...)

</div> -->


## Useful Operator - Divides

For all integers $a,b$ we can say $a$ **divides** $b$, or $a \mid b$, iff there exists some integer $m$ such that $a\cdot m = b$.

### Example

- We can say $2$ divides $6$, or $2 \mid 6$, because $2 \cdot 3 = 6$
- Notice that if $b = 0$ and $m = 0$, then $a$ can be anything. From this we conclude that every number divides $0$. <br>
$\forall a \in \mathbb{Z}, a \mid 0$


## Useful Operator - Mod
<div id="content">

For positive Integers, $x \bmod y$ is the remainder of $x/y$.

More generally, $x \bmod y = x - \left \lfloor{x/y}\right \rfloor \cdot y$.

### Examples

-  $5 \bmod 2 = 1$
-  $4 \bmod 2 = 0$
-  $-1 \bmod 2 = 1$
- *Note that the value of $x \bmod y$ is between $0$ and $y-1$!*

    
    

</div>


## Congruence Modulo y
<div id="content">

Another way we can express mods is via congruency.

$x \equiv z \pmod y$ reads as "$x$ is congruent to $z$ mod $y$".

What this means is that $x \bmod y = z \bmod y$.

### Example

-  $4 \bmod 2 = 0$ and $6 \bmod 2 = 0$, so $4 \equiv 6 \pmod 2$.


</div>

## GCD + Relatively Prime Numbers
<div id="content">
The **greatest common divisor** of two integers $x$ and $y$, denoted $GCD(x,y)$ is the largest positive integer that divides both $x$ and $y$.

### Example
- $GCD(8,12) = 4$
- $GCD(3,6) = 3$
- $GCD(4,7) = 1$

If $GCD(x,y) = 1$, then $x$ and $y$ are **relatively prime** (also called coprime).
</div>