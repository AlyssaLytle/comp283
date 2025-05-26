---
layout: default
title: Common Functions
contributors: Alyssa Byrnes
---


## Common Functions

These slides are meant to show you some common types of functions you might see in Computer Science. 



## Common Function: Minimum


 **Minimum**: The element in a set with the lowest value.

$$x = \textrm{min}(A) \iff \forall y \in A, x \leq y$$

Note that if we can't explicitly define an $$x$$, then the minimum is undefined. 

### Example

- What is the minimum of $$\mathbb{Z}$$? <br>
    - It's undefined, because the lowest element of $$\mathbb{Z}$$ can't be explicitly stated. <br>
- What is the minimum of $$\{x \vert x \in [0,10]\}$$? <br>
    - $$0$$ <br>
- What is the minimum of $$\{x \vert x \in (0,10)\}$$? <br>
    - It's undefined. <br>



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

### Example:

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
