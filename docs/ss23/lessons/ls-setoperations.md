---
layout: default
title: SetOperations
contributors: Alyssa Byrnes
---

## Back to Sets!
### We are going to apply some of the stuff we learned about prepositional logic to learn a little more about sets!
### (This is also a good opportunity for us to practice our prepositional logic!)
### Textbook Chapter 5

## From Last Time, Some Other Useful Notation to Know
 $$\emptyset = \{\}$$ is the empty set.
 
 A **multiset**, also called a bag, tracks repeats, but not order. 
 
### Example 

>$$\{a,a,a,b,b,b,b,c,c,d,d,d,d,d\}$$ is a multiset. 

>It can also be written as $$\{a:3, b:4, c:2, d:5\}$$.


## Set Operations (Some old, some new) 

<img src="https://i.imgur.com/0c94JPz.png" width="250"/>
<img src="https://i.imgur.com/UwPfgSt.png" width="300"/>

-$$a \in B$$ means $$a$$ is an element of $$B$$.

-$$a \notin B$$ means $$a$$ is *not* an element of $$B$$.

>Note that technically, $$a \in B$$ and $$a \notin B$$ are predicates! They take an element and a set as input and give True or False as an output.

>Really, $$a \in B$$ is the same as the function $$in(a,B)$$ from the coins assignment we did last class!

## Subset
<img src="https://i.imgur.com/ZLuhg2i.png" width="300"/>

Let $$A$$ and $$B$$ be sets. We say that $$A$$ is a **subset** of $$B$$ if and only if every element of $$A$$ is an element of $$B$$. 

We write $$A \subseteq B$$ to denote the fact that $$A$$ is a subset of $$B$$.

## Subsets Cont.

### Using Prepositional Logic 

>$$\forall A,B, ~ A \subseteq B \iff \forall x \in A, ~ x \in A \implies x \in B$$

>Technically, we didn't define the domains for $$A$$ and $$B$$, but given the context, we know they are sets, so we'll let it slide... 

>We *could* say that all sets exist in some universe of sets $$S$$. 

>Then our quantifier would say $$\forall A,B \in S \ldots$$ 

>However, for the rest of these slides, we will just do it the lazy/easier to read way... 

## Equality
<img src="https://i.imgur.com/sHL4goN.png" width="150"/>

### Using Prepositional Logic

>Remember this?

>For all sets $$A$$ and $$B$$, $$A = B$$  if and only if every element of $$A$$ is an element of $$B$$ and every element of $$B$$ is an element of $$A$$

> $$\forall A,B, ~ A = B \iff (A \subseteq B$$ and $$B \subseteq A)$$

> $$\forall A,B, ~ A = B \iff (\forall x \in A, (x \in A \implies x \in B) \land (x \in B \implies x \in A))$$

> $$\forall A,B, ~ A = B \iff (\forall x, ~ (x \in A \iff x \in B))$$

## Complement
<img src="https://i.imgur.com/R9uDave.png" width="200"/>

The complement of a set $$A$$, denoted $$\bar{A}$$ is the set of all elements in the universe $$U$$ that are *not* in $$A$$.

### Using Set Notation

>$$\bar{A} = \{x ~ | ~ x \notin A\}$$

### Using Prepositional Logic

>$$\forall a, ~ a \in \bar{A} \iff a \notin A$$

>or, equivalently, $$\forall a \in U, ~ a \notin \bar{A} \iff a \in A$$


## Intersection
<img src="https://i.imgur.com/HpI6xVu.png" width="300"/>

$$A \cap B$$ are the elements that are both in $$A$$ and $$B$$.

### Using Set Notation

>$$A \cap B = \{ x ~ | ~ x \in A \land x \in B \}$$

### Using Prepositional Logic

>$$\forall A, B, x, ~ x \in A \cap B \iff (x \in A \land x \in B)$$


## Union
<img src="https://i.imgur.com/thTdr8m.png" width="300"/>

$$A \cup B$$ are the elements that are either in $$A$$ or $$B$$.

### Using Set Notation

>$$A \cup B = \{ x ~ | ~ x \in A \lor x \in B \}$$

### Using Prepositional Logic

>$$\forall A, B, x, ~ x \in A \cup B \iff (x \in A \lor x \in B)$$


## Difference

<img src="https://i.imgur.com/FOqpwIS.png" width="300"/>

The **difference** of sets $$A$$ and $$B$$ is the set that contains all elements in $$A$$ that are not in $$B$$.

### Using Set Notation

>$$A - B = A\backslash B =\{\, x ~ | ~ x \in A \land x \notin B \}$$

### Using Prepositional Logic

>$$\forall A, B, x, ~ x \in A \backslash B \iff x \in A \land x \notin B$$
 


## Difference Cont.
### Example 

>Let $$A=\{1,3,5,7\}$$ and $$B=\{4,5,6,7,8\}$$.

>$$A-B = \{1,3\}$$.


### Example 

>Let $$C=\{\bigcirc,\diamondsuit,\Box,\heartsuit\}$$ and $$e = \heartsuit$$. 

>$$C-\{e\} = \{\bigcirc, \diamondsuit, \Box\}$$.

## Xor
<img src="https://i.imgur.com/lF0EPYP.png" width="300"/>

### Using Set Notation

>$$A \oplus B = \{x ~ | ~ x \in A \oplus x \in B\}$$

### Using Prepositional Logic

> $$\forall A,B,x, ~ x \in A \oplus B \iff x \in A \oplus x \in B$$

## Disjoint Sets

Two sets are **disjoint** if they share no elements.

>$$\forall A,B,$$ $$A$$ and $$B$$ are disjoint $$\iff A \cap B = \emptyset$$ 

>$$\forall A,B,$$ $$A$$ and $$B$$ are disjoint $$\iff \forall x,~ (x \in B \implies x \notin A) \land (x \in A \implies x \notin B)$$

## Disjoint Union
<img src="https://i.imgur.com/e1baS8x.png" width="300"/>

$$A \uplus B$$ is the union of two **disjoint** sets.



If $$A$$ and $$B$$ are disjoint (share no elements), then $$A \uplus B = A \cup B$$

If $$A$$ and $$B$$ share elements, then $$A \uplus B = ERROR$$

### Using Prepositional Logic

>$$\forall A,B,~ A \uplus B = A \cup B \iff A \cap B = \emptyset$$

## Cartesian Product

<img src="https://i.imgur.com/SgxWVdP.png" width="300"/>
The **cartesian product** of $$A$$ and $$B$$, 

### Using Set Notation

> $$A \times B = \{(a,b)| \forall a \in A$$,  $$\forall b \in B\}$$

### Using Prepositional Logic

> $$\forall A,B, a,b, ~ ((a,b) \in A \times B) \iff (a \in A \land b \in B)$$  


## Powerset
<img src="https://i.imgur.com/THuABsa.png" width="300"/>

The powerset of a set $$A$$, denoted $$\mathscr{P}(A)$$ is the set of all subsets of $$A$$

### Using Set Notation

>$$\mathscr{P}(A) = \{ S ~ | ~ S \subseteq A\}$$

## Powerset Size
The size of $$\mathscr{P}(A)$$:

$$|\mathscr{P}(A)| = 2^{|A|}$$

>Why? Let's do it on the board...

