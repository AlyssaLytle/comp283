---
layout: default
title: Proving Invariants
contributors: Alyssa Byrnes
---


## Invariant

- An **invariant** is a statement that is true during all steps of a procedure.
- In other words, your invariant should be true at Step 0, Step 1, and Step 1000 of your algorithm.
- If the invariant holds for an arbitrary step of your algorithm, this means it'll always hold! (What does that sound like?)
- If the invariant always holds, this means that it'll hold at the last step, which tells us something about our output!



<!-- ## Example


Let's look at our pseudocode for finding the index of the max value in a list.

    1. INPUT: list A
    2. max_idx = 0
    3. max_elem = A[0]
    4. n = length(A)
    5. FOR i in [1,n-1]:
    6.    IF A[i] > max_elem:
    7.        max_elem = A[i]
    8.        max_idx = i
    9. RETURN max_idx
    
- An example invariant could be:

- $$$$ \textrm{For input list } A, \forall i \in [0, \verb|length(A)|), \exists \verb| max_idx| \in [0,i-1], \textrm{ and } \forall j \in [0,i-1], \verb|A[max_idx]| \geq \verb|A[j]|$$$$

- Note that invariants are often called "loop invariants" because they are really describing what is happening inside of our loop!

- Now, let's apply it for $$i = n-1$$ (aka, the end of our for loop)

- $$$$\exists \verb| max_idx| \in [0,n-1), \textrm{ and } \forall j \in [0,n-1), \verb|A[max_idx]| \geq \verb|A[j]|$$$$

- That looks a lot like what we wrote for our generalized output!


 -->


## Proving our Invariant


- We've discussed that if we can prove our invariant, we can prove something about our output! So how do we prove our invariant?
- We can prove our invariant by induction!
- We are going to induct on our loop variable $$i$$ and show that for every trip through the loop our invariant holds!

<img src="https://i.imgur.com/JXtLDMR.png" width="500"/>




<!-- ## Proving our Invariant -->

<!-- 
### Step 1 
We want to prove: 
$$\textrm{For input list } A,$$  <br>
$$\forall i \in [0, \verb|length(A)|],$$ <br>
$$\exists ~ \verb| max_idx| \in [0,i-1],$$ <br>
$$\forall j \in [0,i-1], \verb|A[max_idx]| \geq \verb|A[j]|$$



## Proving our Invariant -->


### Step 1 
We want to prove: 
$$\textrm{For input list } A,$$  <br>
$$\forall i \in [0, \verb|length(A)|],$$ <br>
$$\exists ~ \verb| max_idx| \in [0,i-1],$$ <br>
$$\forall j \in [0,i-1], \verb|A[max_idx]| \geq \verb|A[j]|$$

### Step 2
We prove this by induction on $$i$$.





<!-- ## Proving our Invariant -->


    1. INPUT: list A
    2. max_idx = 0
    3. max_elem = A[0]
    4. n = length(A)
    5. FOR i in [1,n-1]:
    6.    IF A[i] > max_elem:
    7.        max_elem = A[i]
    8.        max_idx = i
    9. RETURN max_idx



<img src="https://i.imgur.com/t5jrK7A.png" width="500"/>



<br><br><br><br><br><Br>

### Step 3 (Base case) 
- *Before* we enter the loop. ($$i=1$$)
- $$\exists \verb| max_idx| \in [0,0], \textrm{ and } \forall j \in [0,0], \verb|A[max_idx]| \geq \verb|A[j]|$$
- Possible values for $$\verb|max_idx|$$: $$0$$
- Possible values for $$j$$: $$0$$
- $$\verb|A[0]| \geq \verb|A[0]| \square$$


<!-- ## Proving our Invariant -->


### Step 4
For a given $$i > 1$$, 

### Step 5 
Induction Hypothesis: I can assume, for all $$k$$, with $$1 \leq k < i$$, that $$\exists \verb| max_idx| \in [0,k-1],$$ 
and 
$$\forall j \in [0,k-1],$$ 
$$\verb|A[max_idx]| \geq \verb|A[j]|$$

### Step 6
I want to prove that $$\exists \verb| max_idx| \in [0,i-1],$$
and 
$$\forall j \in [0,i-1], \verb|A[max_idx]| \geq \verb|A[j]|$$



<img src="https://i.imgur.com/a5HS6Lw.png" width="600"/>






<!-- ## Proving our Invariant (Step 7) -->


    1. INPUT: list A
    2. max_idx = 0
    3. max_elem = A[0]
    4. n = length(A)
    5. FOR i in [1,n-1]:
    6.    IF A[i] > max_elem:
    7.        max_elem = A[i]
    8.        max_idx = i
    9. RETURN max_idx

- Line 6, we have an IF statement, so let's do a proof by cases!
- Case 1: $$\verb|A[i]| > \verb|max_elem|$$
- Case 2: $$\verb|A[i]| \leq \verb|max_elem|$$



<!-- ## Proving our Invariant (Step 7) -->


    1. INPUT: list A
    2. max_idx = 0
    3. max_elem = A[0]
    4. n = length(A)
    5. FOR i in [1,n-1]:
    6.    IF A[i] > max_elem:
    7.        max_elem = A[i]
    8.        max_idx = i
    9. RETURN max_idx




Case 1: $$\verb|A[i]| > \verb|max_elem|$$

$$
\begin{equation}
\begin{array}{l l l}
    1. & \forall k, 1 \leq k < i, \exists \verb| max_idx| \in [0,k-1], \textrm{ and } \forall j \in [0,k-1], \verb|A[max_idx]| \geq \verb|A[j]| 
     & \textrm{Ind. Hypothesis}\\
     2. & \exists \verb| max_idx| \in [0,i-2], \textrm{ and } \forall j \in [0,i-2], \verb|A[max_idx]| \geq \verb|A[j]| & \textrm{Ind. Hypothesis with } k = i-1 \\
     3. & \verb|A[i] > max_elem| & \textrm{Case 1}\\
     4. & \verb|max_elem = A[i]| \land \verb|max_idx = i| & \textrm{Defined in code lines 4-6}\\
     5. & \forall j \in [0,i-1], \verb|A[max_idx]| \geq \verb|A[j]| & \textrm{Combined 2, 3, and 4}
\end{array}
\end{equation}
$$






Case 2: $$\verb"A[i]"  \leq \verb"max_elem"$$

$$
\begin{equation}
\begin{array}{l l l}
    1. & \forall k, 1 \leq k < i, \exists \verb| max_idx| \in [0,k-1], \textrm{ and } \forall j \in [0,k-1], \verb|A[max_idx]| \geq \verb|A[j]| 
     & \textrm{Ind. Hypothesis}\\
     2. & \exists \verb| max_idx| \in [0,i-2], \textrm{ and } \forall j \in [0,i-2], \verb|A[max_idx]| \geq \verb|A[j]| & \textrm{Ind. Hypothesis with } k = i-1 \\
     3. & \verb|A[i]| \leq \verb|max_elem| & \textrm{Case 2}\\
     4. & \forall j \in [0,i-1], \verb|A[max_idx]| \geq \verb|A[j]| & \textrm{Combined 2 and 3} \square
\end{array}
\end{equation}
$$

<!-- ## Proving Our Invariant -->


### Step 8

Therefore, we have proved <br> 
$$\textrm{For input list } A,$$ <br>
$$\forall i \in [0, \verb|length(A)|],$$ <br>
$$\exists \verb| max_idx| \in [0,i-1],$$ 
$$\forall j \in [0,i-1], \verb|A[max_idx]| \geq \verb|A[j]|$$ by induction.







