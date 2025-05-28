---
layout: default
title: Practice and Review 1
contributors: Alyssa Lytle
---

# Review and Practice 1

Here are the practice problems to prepare you for the quiz! I will try and cover as many as possible, but please come to the review session with requests! We can also review problems from the lessons, but I encourage you to use office hours for this as well!

## Date and Time: Thurs, May 29 at 12 pm
* [Zoom Link](https://unc.zoom.us/j/91069874856)
* [Recording Link](/)

# Problems

## 1. Functions

For this problem, we will be discussing this figure:
<img src="/comp283/static/figs/fn-fig.png" style="width:100%">

1.1 Is $$f$$ a total function?

1.2. Is $$g$$ a total function?

1.3. Is $$g$$ a bijection?

1.4. Let $$h=g\circ f$$. Is $$h$$ is a total function?

1.5. Is $$h$$ a bijection?



# Solutions

## 1. Functions 

### 1.1 Is $$f$$ a total function?

First, we start with the definition of a total function.

$$A\times B$$ is a  function  iff  
$$\forall a\in A\  \exists b_1\in B\  \bigl((a,b_1)\in f
\bigr)\land \bigl(\forall b_2\in B\  ({(a,b_2)\in f} \rightarrow {b_2 =
b_1}) \bigr).$$

Let's break this into two properties (like we did in the lesson):

- $$\forall a\in A\  \exists b_1\in B\  \bigl((a,b_1)\in f
\bigr)$$

- $$ \forall b_2\in B\  ({(a,b_2)\in f} \rightarrow {b_2 =
b_1}).$$

Now let's plug in the function and set names.

- $$\forall x \in X\  \exists y_1\in Y\  \bigl((x,y_1)\in f
\bigr)$$

This is true. Over $$f$$, every element of $$X$$ maps to an element in $$Y$$.



- $$ \forall y_2\in Y\  ({(x,y_2)\in f} \rightarrow {y_2 =
y_1}).$$

This is not true. Element $$c$$ maps to both $$3$$ and $$4$$. 

In other words, $$(c,3) \in f$$ and $$(c,4) \in f$$. Since $$3 \neq 4$$, our statement is violated.

Therefore, $$f$$ is NOT a total function.


### 1.2 Is $$f$$ a total function?

Similar to the last problem, let's plug our domain $$Y$$, our co-domain $$Z$$, and our function $$g$$ into the definition.

- $$\forall y\in Y\  \exists z_1\in Z\  \bigl((y,z_1)\in g
\bigr)$$

This is true. Over $$g$$, every element of $$Y$$ maps to an element in $$Z$$.

- $$ \forall z_2\in Z\  ({(y,z_2)\in g} \rightarrow {z_2 =
z_1}).$$

This is also true. Over $$g$$, every element in $$Z$$ is mapped to by at most one element in $$Y$$.

Therefore $$g$$ is a total function.

### 1.3 Is $$g$$ a bijection?

### 1.4 Let $$h=g\circ f$$. Is $$h$$ is a total function?

Yes, $$h$$ is a total function. You can verify this by plugging in  domain $$X$$, co-domain $$Z$$, and function $$h$$ into the definition of a function, similar to how we did in 1.1 and 1.2.

### 1.5 Is $$h$$ a bijection?