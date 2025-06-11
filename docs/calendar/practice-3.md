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

# Solutions

## 2

### 2.1 

There are multiple ways you can express this. The indexing can be a little tricky to make sure you're capturing exactly $$n$$ elements.

You might be inclined express it like this: 

$$\forall n \in \mathbb{N}, \sum_{k=1}^n 2k + 1 = n^2$$

But is this capturing the right numbers? Let's try a base case. When $$n = 1$$, \sum_{k=1}^1 2k + 1 = 2(1) + 1 = 3 \neq 1^2$$. We're essentially getting an "off-by-one" error where the left side of our equation is summing the odds starting at $$n=3$$. 

We're used to expressing odds as $$2k+1$$ (an even number plus one), but we can *also* express odds as $$2k-1$$ (an even number minus one)!

Now we get what we want!

$$\forall n \in \mathbb{N}, \sum_{k=1}^n 2k - 1 = n^2$$