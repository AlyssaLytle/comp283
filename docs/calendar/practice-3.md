---
layout: default
title: Practice and Review 1
contributors: Alyssa Lytle
---

# Review and Practice 3



## 1. Proof by Induction

Prove the *binomial theorem* by induction on $$n$$: 

$$(x+y)^n = \sum_{m=0}^n {n \choose m}x^m y^{n-m}$$

## 2. Proof by Induction

2.1 Express the following sentence mathematically: 

The sum of the first $$n$$ odd natural numbers equals $$n^2$$

2.2

Prove this expression.

## 3. Induction over Fibonacci

Prove $$F(3n)$$ is even.

# Solutions

## 2

### 2.1 

There are multiple ways you can express this. The indexing can be a little tricky to make sure you're capturing exactly $$n$$ elements.

You might be inclined express it like this: 

$$\forall n \in \mathbb{N}, \sum_{k=1}^n (2k + 1) = n^2$$

But is this capturing the right numbers? Let's try a base case. When $$n = 1$$, $$ \sum_{k=1}^1 2k + 1 = 2(1) + 1 = 3 \neq 1^2$$. We're essentially getting an "off-by-one" error where the left side of our equation is summing the odds starting at $$n=3$$. 

We're used to expressing odds as $$2k+1$$ (an even number plus one), but we can *also* express odds as $$2k-1$$ (an even number minus one)!

Now we get what we want!

$$\forall n \in \mathbb{N}, \sum_{k=1}^n (2k - 1) = n^2$$

## 3 Fibonacci


### Step 1
State the ‘for all’ statement that you want to prove:


$$\forall n \in \mathbb{N}, F(3n)$$ is even \\


### Step 2
State the induction parameter.

We prove this by induction on $$n$$


### Step 3
Prove the base case(s): 


For $$n=0$$:
    * $$F(3(0)) = F(0) = 0$$
    * $$0$$ is even $$\square$$




### Step 4
Write the induction step:


For a given $$n > 0$$



### Step 5
State the Induction Hypothesis:



I can assume, for all $$k$$, with $$0 \leq k < n$$, $$F(3k)$$ is even



### Step 6
State what you want to prove:



I want to prove, for a given $$n>0$$, $$F(3n)$$ is even



### Step 7

Inductively prove what you stated in Step 6 using your Induction Hypothesis stated in Step 5.

$$
\begin{equation*}
    \begin{array}{l l l}
    1. & \forall k, 0 \leq k < n, F(3k) \textrm{ is even} & \textrm{Induction Hypothesis}\\
    2. & F(3(n-1)) \textrm{ is even} & \textrm{Plug } k = n - 1 \textrm{ into Induction Hypothesis}\\
    3. & F(3n-3) \textrm{ is even} & \textrm{Simplify line 2}\\
    4. & \exists x \in \mathbb{Z}, F(3n-3) = 2x & \textrm{Definition of even number}\\
    5. & F(3n) = F(3n-1) + F(3n-2) & \textrm{Definition of Fibonacci Series}\\
    6. & F(3n-1) = F(3n-2) + F(3n-3) & \textrm{Definition of Fibonacci Series}\\
    7. & F(3n) = F(3n-2) + F(3n-3) + F(3n-2) & \textrm{Plugged Line 6 into Line 5}\\
    8. & F(3n) = 2(F(3n-2)) + F(3n-3) & \textrm{Rewrite line 7}\\
    9. &  F(3n) = 2(F(3n-1)) + 2x & \textrm{Plugged line 4 into line 8}\\
    10. & F(3n) = 2(F(3n-1) + x) & \textrm{Simplified line 9}\\
    11. & F(3n-1) + x \in \mathbb{Z} & \textrm{Integer Closure} \\
    12. & F(3n) \textrm{ is even} & \textrm{Definition of odd applied to lines 10 and 11}
    \end{array}
    \end{equation*}
$$


### Step 8
State what you just proved.



Therefore, $$\forall n \in \mathbb{N}, F(3n+1)$$ is odd. 

