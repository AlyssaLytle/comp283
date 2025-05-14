---
layout: default
title: SetsAndTuples
contributors: Alyssa Byrnes
---

## Learning Objectives

To learn the language of sets and tuples:

-  You will be able to define sets with braces, ($\{\}$), tuples with parentheses, $((\,))$, sets of tuples with Cartesian product, $(\times)$, and sets of strings with concatenation.
-  You will be able to name common sets (including the natural numbers $(\mathbb{N})$, integers $(\mathbb{Z})$, and the empty set $(\emptyset=\{\})$), and use notation for testing element inclusion in a set $( \in )$, and its negation $(\notin)$, and for testing whether a set is a subset of another, $(\subseteq )$.
-  You will be able to count elements in sets using the sum and product rules
-  You will meet several extensions (to lists, sequences, vectors, matrices, strings, and languages) that are common abstractions in computer science. These are just sets and tuples with special operations. (In fact, even tuples can be reduced to sets -Extension 3.14 in the text.)



## Sets - Definitions

A ***set*** is an unordered collection of objects.

The following are sets:

-  $\{1,2,3\}$
-  "all multiples of 7''
-  \{apples, $7$, $\texttt{True}$\}

Sets don't inherently have an order.

## Sets - Terminology

A set is a ***finite set*** if it has a finite number of elements. 

Any set that is not finite is an ***infinite set***.

Let $A$ be a finite set. The number of different elements in $A$ is called its ***cardinality***. 

The cardinality of a finite set  is denoted $|A|$.


>$\{1,2,3\}$ is a finite set. Its cardinality is $3$.

>"all multiples of 7" is an infinite set. Cardinality here is a little more complicated... We will get back to that!



## Sets - Notation
$a \in A$ means $a$ is an element of $A$.

$a \notin A$ means $a$ is *not* an element of $A$.

## Sets - Notation
$a \in A$ means $a$ is an element of $A$.

$a \notin A$ means $a$ is *not* an element of $A$.


### Example

>Let $A = \{$"apples", "bananas", "oranges"$\}$

>"apples" $\in A$

>"blueberries" $\notin A$


## Sets - Notation

$[a,b]$ is the set of whole numbers $\geq a$  and $\leq b$.

$(a,b)$ is the set of whole numbers $> a$  and $< b$.

## Sets - Notation

$[a,b]$ is the set of whole numbers $\geq a$  and $\leq b$.

$(a,b)$ is the set of whole numbers $> a$  and $< b$.

### Examples

>$[1,5] = \{1,2,3,4,5\}$

>$(1,5) = \{2,3,4\}$

>$[1,5) = \{1,2,3,4\}$

## Sets - Notation

Sets are commonly expressed using *set notation*.

Within braces, we can write a rule consisting of a function, a vertical bar, and a set to which the function is applied.

<img src="https://i.imgur.com/AG0hluA.png" width="700"/>

## Sets - Notation

### Example

>We can express the set $\{\
frac{1}{2}, \frac{1}{4}, \frac{1}{8} \}$ as...

><img src="https://i.imgur.com/S8631Np.png" width="700"/>


## Subsets

$A$ is a ***subset*** of $B$ if and only if every element of $A$ is an element of $B$. 

Can also be written: $A \subseteq B$ 

### Examples

>Let $A = \{1,3,5\}$ and $B = \{1,2,3,4,5\}$.

>>$A \subseteq B$.


>Let $A = \{1,2,3\}$ and $B = \{3,2,1\}$.

>>$A \subseteq B$ and $B \subseteq A$.

## Equality 

$A = B$ if and only if every element of $A$ is an element of $B$ and conversely every element of $B$ is an element of $A$. 
That is, $A \subseteq B$ and $B \subseteq A$.

### Example
>Let $A = \{1,2,3\}$ and $B = \{3,2,1\}$. <br><br>
$A \subseteq B$ and $B \subseteq A$, so $A=B$

## Intersection


$A \cap B$ is the set of elements that are both in $A$ **and** in $B$.

### Example
> $A = \{$Apples, Bananas$\}$ <br> 
$B= \{$Bananas, Oranges$\}$ <br>
$A \cap B =$ {Bananas}


- Note how this ties into logic...
$x \in A \cap B$ iff $x \in A \land x \in B$


## Union

$A \cup B$ is the set of elements that are in either $A$ **or** $B$.

### Example
> $A = \{$Apples, Bananas$\}$ <br>
$B= \{$Bananas, Oranges$\}$ <br>
$A \cup B =$ {Apples, Bananas, Oranges}
 
- Note how this ties into logic...
 $x \in A \cup B$ iff $x \in A \lor x \in B$


## Common Sets

- There are some standard symbols that represent specific sets you will see:
- The set of **Natural Numbers** $\mathbb{N}$ is the set of all whole numbers $\geq 0$, $\{0,1,2,3,4,\ldots\}$.*
- The set of **Integers** $\mathbb{Z}$ is the set of all whole numbers, $\{\ldots, -3, -2, -1, 0, 1, 2, 3, \ldots\}$.
- The set of **Rational Numbers** $\mathbb{Q}$ are numbers that can be represented as a quotient of whole numbers, $\{\frac{p}{q} \mid p,q \in \mathbb{Z}\}$
- The set of **Real Numbers** $\mathbb{R}$ is all *real* numbers. 


## Tuples

A $k$-***tuple*** is an ordered sequence of $k$ elements, which we write down in parentheses, $(a_1,a_2,\ldots,a_k)$.

> The most common tuple seen in math is the coordinate pair $(x,y)$ on a graph. 

> A 2-tuple is commonly called an *ordered pair*.

Two tuples are equal if and only if all of their corresponding elements are equal.
$(a_1,a_2,\ldots,a_k)$ iff for all $i\in[1,\ldots,k]$ we have $a_i=b_i$.


## Tuples - Cartesian Product

The basic operation to create tuples is the Cartesian Product of two sets.

The \textbf{cartesian product} of $A$ and $B$, $A \times B = \{(a,b)|$ for all $a \in A$ and for all $b \in B\}$

### Example
>Let $L=\{a,b,c\}$ and let $D = \{0,1\}$
$L \times D = \{(a,0),(a,1),(b,0),(b,1),(c,0),(c,1)\}$
$D \times L = \{(0,a),(0,b),(0,c),(1,a),(1, b),(1,c)\}$
$L \times L = L^2 = \{(a,a),(a,b),(a,c),(b,a),(b, b),(b,c),(c,a),(c, b),(c,c)\}$

The cartesian product is associative: $D \times(L \times D) = (D \times L) \times D$.

The cartesian product is not necessarily commutative: $D\times L \neq L \times D$.
</dov>

## Sequences, Strings, and Series

Some other structures we may use:

-  **list**: tuples that may have arbitrary finite length, 
-  **sequence**: lists that may be infinite 
-  **vectors**: tuples with additional operations (e.g. addition, scalar multiplication, rotation, and calculating lengths)
-  **matrices, arrays, and tables**: tuples, displayed with a two-dimensional layout, and perhaps given extra operations.


## Concatenation

***Concatenation*** is used to join two strings or lists by putting all elements of the second string behind all elements of the first.

### Example
>The concatenation of "hello" and "world" is "helloworld".

## Series

A ***series*** is a sum of a sequence of numbers, replacing commas by plus signs. 

Any finite sequence, such as ($x_1, x_2,\ldots, x_n$), has a series $x_1 + x_2 +\ldots+ x_n$ with a well-defined value. 

This can also be written with summation notation: $\sum_{i\in[1,n]}x_i$.


## Counting Elements in Sets

The ***Sum rule*** states: Suppose that each element of a set has an assigned type. Then the total number of elements is the sum of the numbers of elements of each type.

The ***Product rule*** states: Suppose that elements of a set have features that can be chosen independently. Then the number of elements is the product of the numbers of choices.

The best way to demonstrate what this means is by example...

## Counting Example 1

- You have a set of six different math books, five different philosophy books, and three different religion books. How many books do you have? 
- The sum rule says, "Add them up. $6 + 5 + 3 = 14$." 


## Counting Example 2


- Now you want a set of three books, one of each type; how many sets of three are possible? 
- You want to count all tuples of the form $(m,p,r)$, where $m$ is a math book, $p$ is a philosophy book, and $r$ is a religion book. You choose one of six math books, one of five philosophy books, and one of three religion books, so the product rule says, 
- "$6 \cdot 5 \cdot 3 = 90$ sets of three are possible."
- If $M$ is the set of math books, $P$ is the set of philosophy books, and $R$ is the set of religion books. You can get all possible sets of three using the **cartesian product**, and the **cardinality** of that is the number of possible sets, $|M \times P \times R|$.
- We can see that $|M|\cdot |P| \cdot |R| = |M \times P \times R|$. 
- *This exactly what the product rule is saying!*

## Permutations

The **permutations** of $n$ distinct items are the set of all $n$-tuples that *never repeat* any item.

### Example
>Let $A = \{Bob, Alice, Chris\}$ <br>
All permutations of $A$: <br>
$\big\{\{Bob, Alice, Chris\}, \{Bob, Chris, Alice\},$ <br>
$\{Alice, Chris, Bob\}, \{Alice, Bob, Chris\},$ <br>
$\{Chris, Bob, Alice\}, \{Chris, Alice, Bob\}\big\}$

## Counting Permutations

The number of permutations of $n$ items is $n!$ ($n$ factorial).

As a reminder, $n! = n \cdot (n-1) \cdot (n-2) \cdot \ldots \cdot 1$.

### Example
>Let $A = \{Bob, Alice, Chris\}$ <br>
The number of possible permutations of $A$ is $3! = 3 \cdot 2 \cdot 1 = 6$. 

## Permutations Examples

Let's go back to our previous example. 

You have a set of six different math books, five different philosophy books, and three different religion books.  

We want to know the number of ways to arrange three of the 14 books on the shelf and get one of each type. 

Let's break this down...





## Permutations Examples


- You have a set of 6 different math books, 5 different philosophy books, and 3 different religion books. We want to know the number of ways to arrange three of the 14 books on the shelf and get one of each type. 
- Let's break this down...
- Let's say you just want three books, one of each type, from the shelf. How many possible combinations are there?
- Our product rule tells us there are $6 \cdot 5 \cdot 3$ possible combinations.
- Let's say you just want to know how many times you can arrange a set of $3$ books, regardless of type. This is the same as counting how many permutations there are of a set of size $3$, so the answer is $3!$.
- Now we can combine these two answers: $3! \cdot 6 \cdot 5 \cdot 3$


## Permutations Examples Continued

- Now let's say you want to know how many different ways you can arrange your $14$ books. That's pretty straightforward. You have $14!$ possible permutations of your set of books. 
- Say you just wanted to know how many ways you can order any three of those fourteen books. We just stop our factorial early. $14 \cdot 13 \cdot 12$.
- There's actually a way we can mathematically express this. It can be written as $\frac{14!}{(14-3)!}$.

Let's draw out why this works...


## Permutations Examples Continued


- Now let's say you want to know how many different ways you can arrange your $14$ books. That's pretty straightforward. You have $14!$ possible permutations of your set of books. 
- Say you just wanted to know how many ways you can order any three of those fourteen books. We just stop our factorial early. $14 \cdot 13 \cdot 12$.
- There's actually a way we can mathematically express this. It can be written as $\frac{14!}{(14-3)!}$.
- If you want to stop $n$ factorial after $k$ terms (you can call this a $k$-permutation), you can express this as $\frac{n!}{(n-k)!}$. 


## Combinations

A $k$-***combination*** is a set with $k$ elements chosen from a set of $n$ possible items with no repeats. 

(Since these are sets, order does not matter!)

### Example

>Compute all $2$-combinations of $\{a,b,c\}$. <br>
$\{a,b\},\{a,c\}, \{b,c\}$

### Permutations vs. Combinations
> The $2$-permutations of $\{a,b,c\}$ would be $(a,b), (b,a), (a,c), (c,a), (b,c), (c,b)$.


## Number of Combinations

The number of $k$-combinations of a set of size $n$ is ${n \choose k}$, read as "$n$ choose $k$".

Other ways you may see "$n$ choose $k$" written:

-  $C(n,k)$
-  $_nC_k$
-  $COMB(n,k)$

### How to Compute n choose k

${n \choose k} = \frac{n!}{k!(n-k)!}$

Why does this formula work? Some reasoning behind this by example...


## Example

- Compute the number of $2$-permutations of $\{a,b,c\}$.
- We're going to do this the long way. Let's consider all possible sets of size 2 we can make from $\{a,b,c\}$.
- All sets of size 2 of $\{a,b,c\}$: $\{a,b\},\{a,c\}, \{b,c\}$.
- Now for permutations, order matters, so we have to consider all orderings of these new sets.
- All permutations of $\{a,b\}$: $(a,b), (b,a)$.
- All permutations of $\{a,c\}$: $(a,c), (c,a)$.
- All permutations of $\{b,c\}$: $(b,c), (c,b)$.


## Example Continued... 

- So, the number of $k$-permutations is the number of all sets of size $k$ times the number of possible permutations for one of those sets of size $k.$
- Notice the number of all sets of size $k$ is the same thing as the number of $k$-combinations.
- And we know that the number of possible permutations for one of those sets of size $k$ is $k!$.
- So, the number of $k$-permutations is equal to the number of $k$-combinations times $k!$.
- Equivalently, we can say that the number of $k$-combinations is equal to the number of $k$-permutations divided by $k!$.
- The number of $k$ permutations $= \tfrac{n!}{(n-k)!}$
- The number of $k$ permutations $= \frac{n!}{(n-k)!} \cdot \frac{1}{k!} = \frac{n!}{k!(n-k)!} = {n \choose k}$



