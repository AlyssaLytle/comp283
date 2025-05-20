---
layout: default
title: Relations
contributors: Alyssa Byrnes
---


## Relations 


A **relation** on two sets, $$A$$ and $$B$$ is a subset of pair $$A \times B$$.


### Example 1
> Let's look at the following relation: <br> <br>
$$R = \{(m,n) \mid m, n \in \mathbb{Z} \land m < n\}$$ <br><br>
In English: "All pairs of integers $$(m,n)$$ such that $$m<n$$." <br><br>
What are our two sets? <br>
> **Answer:** We're looking at the Integers! <br> 
In other words, $$A = \mathbb{Z}$$ and $$B = \mathbb{Z}$$  <br>
so $$R$$ contains elements in $$\mathbb{Z} \times \mathbb{Z} = \mathbb{Z}^2$$




### Example 2

> Let's look at the following relation: <br>
> $$R = \{(m,n) \mid m, n \in \mathbb{Z} \land m < n\}$$ <br>
> In English: "All pairs of integers $$(m,n)$$ such that $$m<n$$." <br>
> Is $$(2,3) \in R$$? <br>
> <p style="color:green;">Yes! Because $$2 \in \mathbb{Z},$$ $$3 \in \mathbb{Z},$$ and $$ 2 < 3 $$.</p>




### Example 3

> Let's look at the following relation:<br>
> $$R = \{(m,n) \mid m, n \in \mathbb{Z} \land m < n\}$$<br>
> In English: "All pairs of integers $$(m,n)$$ such that $$m<n$$." <br>
> Is $$(3,2) \in R$$?
> <p style="color:red;">No! Because  $$3 \cancel{<} 2$$. </p>



## Other Types of Relations


We can use relations to describe many types of relationships!

### Example 4

- Back to our coin purse example... <br>
- Say $$C$$ is a set of coin purses and $$X$$ is a set of coins. <br>
- $$In(x,c) = True \iff$$ coin $$x$$ is in coin purse $$c$$. <br>
- Say we want to see all coins that have a coin purse. We could look at the relation: <br>
- $$R = \{(x,c) \mid x \in X \land c \in C \land In(x,c) \}$$ <br>
- This would give us the pairs $$(x,c)$$ of each coin $$x$$ and its corresponding coin purse $$c$$. <br>



## Some Considerations


### Binary Relations

Most of the relations we will talk about will be **binary relations**. 

This is simply a relation with tuples of size $$2$$ (e.g. $$R \subseteq A \times B$$). However, relations can be over many sets (e.g. $$R \subseteq A \times B \times C$$).

### Notation

Another way we could write about elements of relation $$R \subseteq A \times B$$ is:

$$\forall (x,y) \in R, x R y$$





## Other ways we can write relations - Graphs


You may see relations represented in other ways, too. 

You can represent relation $$R \subseteq A \times B$$ using a **graph** by making each element of $$A$$ and $$B$$ a dot or  *vertex*, and draw an **edge** with an arrow for each $$(a,b) \in R$$. 




### Example - Flow Charts

>Flowcharts are relations of the form:

>$$R = \{(m,n) \mid$$ "do $$m$$ before $$n$$" $$\}$$




<img src="https://i.imgur.com/PiEWWky.png" width="400"/>





## Other ways we can write relations - T/F Matrix



You can represent relation $$R \subseteq A \times B$$ as a $$\mid A \mid \times \mid B \mid$$ matrix $$M$$.

If $$(a,b) \in R$$, then on the matrix $$M[a,b] = T$$, otherwise  $$M[a,b] = F$$.



### Example - Equality

$$R = \{(x,y) \in [1,2,3,4] \mid x = y \}$$



<img src="https://i.imgur.com/Ofg8ewV.png" width="400"/>



## Complement and Inverse


Every relation $$R \subseteq A \times B$$ has a **complement** and an **inverse**.

### Complement Definition
The *complement* of $$R$$, denoted $$\bar{R}$$, consists of all pairs from $$A \times B$$ that are not in R.

$$\bar{R} = \{ (x,y) \mid x \in A \land y \in B \land (x,y) \notin R \}$$

### Inverse Definition
The *inverse* of $$R$$, denoted $$R^{-1}$$, is obtained by simply swapping the order of every pair.

$$R^{-1} = \{ (y,x) \mid (x,y) \in R\}$$





## Complement and Inverse Example


- Let $$P$$ be a group of coworkers: 
- $$P = \{Alice, Bob, Chris \}$$
- Say Alice sends an email to everyone else. Say Chris replies to her email.
- $$R = \{ (a,b) \mid a,b \in P \land a \textrm{ sent an email to } b \}$$
- So, $$R = \{(Alice, Bob), (Alice, Chris), (Chris, Alice) \}$$
- The complement, $$\bar{R}$$, is the set $$(a,b)$$ where $$a$$ did not send an email to $$b$$.
- $$\bar{R} = \{(Bob, Alice), (Bob, Chris), (Chris, Bob) \}$$
- The inverse, $$R^{-1}$$, is the set of $$(b,a)$$ where $$b$$ received an email from $$a$$.
- $$R^{-1} = \{(Bob,Alice), (Chris, Alice), (Alice, Chris)\}$$



## Binary Relations over a Single Set


We are going to discuss some properties of binary relation $$R \subseteq A \times A$$





## Reflexive Relations


$$R \subseteq A \times A$$

$$R$$ is **reflexive** iff $$\forall x \in A, x R x$$.

Another way to say this is $$\forall x \in A, (x R x)$$ holds.

### Example

>$$R_{\textrm{equal}} = \{(x,y) \mid x,y \in \mathbb{Z} \land x = y \}$$ <br>
>Is this reflexive?

><p style="color:green;"> Yes! Because every integer equals itself! ($$x=x$$)</p>

>$$R_{\textrm{nequal}} = \{(x,y) \mid x,y \in \mathbb{Z} \land x \neq y \}$$ 
>Is this reflexive? 
> <p style="color:red;"> No! Because for every integer, $$x\neq x$$ does not hold.</p>



## Irreflexive Relations


$$R$$ is **irreflexive** iff $$\forall x \in A, (x \cancel{R} x)$$

Another way to say this is $$\forall x \in A, (x R x)$$ does not hold.

### Example

>$$R_{\textrm{equal}} = \{(x,y) \mid x,y \in \mathbb{Z} \land x = y \}$$ <br>
>Is this irreflexive?



## Irreflexive Relations


$$R$$ is **irreflexive** iff $$\forall x \in A, (x \cancel{R} x)$$

Another way to say this is $$\forall x \in A, (x R x)$$ does not hold.

### Example

>$$R_{\textrm{equal}} = \{(x,y) \mid x,y \in \mathbb{Z} \land x = y \}$$ <br>
>Is this irreflexive? <br>
>No! Because for all integers, $$x = x$$ holds.



## Irreflexive Relations


$$R$$ is **irreflexive** iff $$\forall x \in A, (x \cancel{R} x)$$

Another way to say this is $$\forall x \in A, (x R x)$$ does not hold.

### Example

>$$R_{\textrm{equal}} = \{(x,y) \mid x,y \in \mathbb{Z} \land x = y \}$$ <br>
>Is this irreflexive? <br>
>No! Because for all integers, $$x = x$$ holds. <br>
>$$R_{\textrm{nequal}} = \{(x,y) \mid x,y \in \mathbb{Z} \land x \neq y \}$$ <br>
>Is this irreflexive?



## Irreflexive Relations


$$R$$ is **irreflexive** iff $$\forall x \in A, (x \cancel{R} x)$$

Another way to say this is $$\forall x \in A, (x R x)$$ does not hold.

### Example

>$$R_{\textrm{equal}} = \{(x,y) \mid x,y \in \mathbb{Z} \land x = y \}$$ <br>
>Is this irreflexive? <br>
>No! Because for all integers, $$x = x$$ holds. <br>
>$$R_{\textrm{nequal}} = \{(x,y) \mid x,y \in \mathbb{Z} \land x \neq y \}$$ <br>
>Is this irreflexive? <br>
>Yes! Because for all integers, $$x \neq x$$ does not hold.



## Symmetric Relations


$$R$$ is **symmetric** iff $$\forall x,y \in A, (x R y \implies y R x)$$

### Example

>$$R_{\textrm{equal}} = \{(x,y) \mid x,y \in \mathbb{Z} \land x = y \}$$ <br>
>Is this symmetric?





## Symmetric Relations


$$R$$ is **symmetric** iff $$\forall x,y \in A, (x R y \implies y R x)$$

### Example

>$$R_{\textrm{equal}} = \{(x,y) \mid x,y \in \mathbb{Z} \land x = y \}$$<br>
>Is this symmetric? <br>
>Yes, because if $$x=y$$, then $$y=x$$





## Symmetric Relations


$$R$$ is **symmetric** iff $$\forall x,y \in A, (x R y \implies y R x)$$

### Example

>$$R_{\textrm{equal}} = \{(x,y) \mid x,y \in \mathbb{Z} \land x = y \}$$<br>
>Is this symmetric? <br>
>Yes, because if $$x=y$$, then $$y=x$$ <br>
>$$R_{\textrm{nequal}} = \{(x,y) \mid x,y \in \mathbb{Z} \land x \neq y \}$$ <br>
>Is this symmetric?




## Symmetric Relations


$$R$$ is **symmetric** iff $$\forall x,y \in A, (x R y \implies y R x)$$

### Example

>$$R_{\textrm{equal}} = \{(x,y) \mid x,y \in \mathbb{Z} \land x = y \}$$<br>
>Is this symmetric? <br>
>Yes, because if $$x=y$$, then $$y=x$$ <br>
>$$R_{\textrm{nequal}} = \{(x,y) \mid x,y \in \mathbb{Z} \land x \neq y \}$$ <br>
>Is this symmetric? <br>
>Yes, because if $$x\neq y$$, then $$y \neq x$$





## Symmetric Relations


$$R$$ is **symmetric** iff $$\forall x,y \in A, (x R y \implies y R x)$$

### Example

>$$R_{\textrm{equal}} = \{(x,y) \mid x,y \in \mathbb{Z} \land x = y \}$$<br>
>Is this symmetric? <br>
>Yes, because if $$x=y$$, then $$y=x$$ <br>
>$$R_{\textrm{nequal}} = \{(x,y) \mid x,y \in \mathbb{Z} \land x \neq y \}$$ <br>
>Is this symmetric? <br>
>Yes, because if $$x\neq y$$, then $$y \neq x$$ <br>
>$$R_{\textrm{lessthan}} = \{(x,y) \mid x,y \in \mathbb{Z} \land x < y \}$$ <br>
>Is this symmetric?



## Symmetric Relations


$$R$$ is **symmetric** iff $$\forall x,y \in A, (x R y \implies y R x)$$

### Example

>$$R_{\textrm{equal}} = \{(x,y) \mid x,y \in \mathbb{Z} \land x = y \}$$<br>
>Is this symmetric? <br>
>Yes, because if $$x=y$$, then $$y=x$$ <br>
>$$R_{\textrm{nequal}} = \{(x,y) \mid x,y \in \mathbb{Z} \land x \neq y \}$$ <br>
>Is this symmetric? <br>
>Yes, because if $$x\neq y$$, then $$y \neq x$$ <br>
>$$R_{\textrm{lessthan}} = \{(x,y) \mid x,y \in \mathbb{Z} \land x < y \}$$ <br>
>Is this symmetric? <br>
>No, because if $$x<y$$, it is not true that $$y<x$$.



## Antisymmetric Relations


$$R$$ is **antisymmetric** iff $$\forall x \neq y \in A, (x R y \implies y \cancel{R} x)$$

You can also say, if $$x R y$$ holds, then $$y R x$$ does not hold.

### Example

>$$R_{\textrm{lessthan}} = \{(x,y) \mid x,y \in \mathbb{Z} \land x < y \}$$ <br>
>Is this antisymmetric?





## Antisymmetric Relations


$$R$$ is **antisymmetric** iff $$\forall x \neq y \in A, (x R y \implies y \cancel{R} x)$$

You can also say, if $$x R y$$ holds, then $$y R x$$ does not hold.

### Example

>$$R_{\textrm{lessthan}} = \{(x,y) \mid x,y \in \mathbb{Z} \land x < y \}$$ <br>
>Is this antisymmetric? <br>
>Yes! Because if $$x<y$$, then $$y \cancel{<} x$$





## Antisymmetric Relations


$$R$$ is **antisymmetric** iff $$\forall x \neq y \in A, (x R y \implies y \cancel{R} x)$$

You can also say, if $$x R y$$ holds, then $$y R x$$ does not hold.

### Example

>$$R_{\textrm{lessthan}} = \{(x,y) \mid x,y \in \mathbb{Z} \land x < y \}$$ <br>
>Is this antisymmetric? <br>
>Yes! Because if $$x<y$$, then $$y \cancel{<} x$$ <br>
>$$R_{\textrm{lessthaneq}} = \{(x,y) \mid x,y \in \mathbb{Z} \land x \leq y \}$$ <br>
>Is this antisymmetric?



## Antisymmetric Relations


$$R$$ is **antisymmetric** iff $$\forall x \neq y \in A, (x R y \implies y \cancel{R} x)$$

You can also say, if $$x R y$$ holds, then $$y R x$$ does not hold.

### Example

>$$R_{\textrm{lessthan}} = \{(x,y) \mid x,y \in \mathbb{Z} \land x < y \}$$ <br>
>Is this antisymmetric? <br>
>Yes! Because if $$x<y$$, then $$y \cancel{<} x$$ <br>
>$$R_{\textrm{lessthaneq}} = \{(x,y) \mid x,y \in \mathbb{Z} \land x \leq y \}$$ <br>
>Is this antisymmetric? <br>
>Yes! Because if $$x \leq y$$, then $$y \cancel{\leq} x$$ <br>
>Wait... but what about if $$x=2$$ and $$y=2$$? $$x \leq y$$ and $$y \leq x$$





## Antisymmetric Relations


$$R$$ is **antisymmetric** iff $$\forall x \neq y \in A, (x R y \implies y \cancel{R} x)$$

You can also say, if $$x R y$$ holds, then $$y R x$$ does not hold.

### Example

>$$R_{\textrm{lessthan}} = \{(x,y) \mid x,y \in \mathbb{Z} \land x < y \}$$ <br>
>Is this antisymmetric? <br>
>Yes! Because if $$x<y$$, then $$y \cancel{<} x$$ <br>
>$$R_{\textrm{lessthaneq}} = \{(x,y) \mid x,y \in \mathbb{Z} \land x \leq y \}$$ <br>
>Is this antisymmetric? <br>
>Yes! Because if $$x \leq y$$, then $$y \cancel{\leq} x$$ <br>
>Wait... but what about if $$x=2$$ and $$y=2$$? $$x \leq y$$ and $$y \leq x$$ <br>
> That's okay, because as we say in the definition, this only has to apply for $$x \neq y$$.





## Transitive Relations


$$R$$ is **transitive** iff $$\forall x,y,z \in A, (x R y \land y R z) \implies x R z$$

### Example

>$$R_{\textrm{equal}} = \{(x,y) \mid x,y \in \mathbb{Z} \land x = y \}$$ <br>
>Is this transitive?





## Transitive Relations


$$R$$ is **transitive** iff $$\forall x,y,z \in A, (x R y \land y R z) \implies x R z$$

### Example

>$$R_{\textrm{equal}} = \{(x,y) \mid x,y \in \mathbb{Z} \land x = y \}$$ <br>
>Is this transitive? <br>
>Yes! Because if $$x=y \land y = z$$, then $$x = z$$





<!-- ## Something to Think About...


Let's look at two relations:

$$R_{\textrm{equal}} = \{(x,y) \mid x,y \in \mathbb{Z} \land x = y \}$$

As we already discussed, $$R_{\textrm{equal}}$$ is reflexive, symmetric, and transitive.

$$R_{\textrm{iff}} = \{(x,y) \mid x,y \in \{T,F\} \land x \iff y \}$$

$$R_{\textrm{iff}}$$ is also

reflexive: $$x \iff x$$ holds

symmetric: If $$x \iff y$$, then $$y \iff x$$

transitive: If $$x \iff y$$ and $$y \iff z$$, then $$x \iff z$$

Is it a coincidence that $$R_{\textrm{equal}}$$ and $$R_{\textrm{iff}}$$ have the same properties? 

No! We've discussed before that $$\iff$$ is measure of equivalence!


 -->


