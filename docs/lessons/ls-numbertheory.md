---
layout: default
title: NumberTheory
contributors: Alyssa Byrnes
---

## Introduction to Number Theory

- Chapter 7 in Textbook

- (Called "Math Review" in book, but some of these concepts might be new!)

## Useful Operators - Floor and Ceiling

The **floor** operator, denoted $$\left \lfloor{x}\right \rfloor$$, tells us the greatest integer $$\leq x$$.

The **ceiling** operator, denoted $$\left \lceil{x}\right \rceil$$,  tells us the smallest integer $$\geq x$$.

(Basically, they're just fancy ways of saying "round down" and "round up")

### Example

- > $$\left \lfloor{7.5}\right \rfloor = 7$$

- > $$\left \lceil{7.5}\right \rceil = 8$$


## Property of Floor
> - $$x-1 < \left \lfloor{x}\right \rfloor \leq x$$

> Why?

- > By definition, we know $$\left \lfloor{x}\right \rfloor \leq x$$

- > We know $$x-1 < \left \lfloor{x}\right \rfloor$$ because:
    
    - > We can write $$x$$ as $$x = y + d$$ where $$y$$ is an integer and $$d$$ is a decimal. (E.g. $$7.5 = 7 + .5$$)
    
    - > We know $$\left \lfloor{x}\right \rfloor = y$$ and that $$d$$ is some real number such that $$0 \leq d < 1$$.
    
    - > We know $$d < 1$$, so $$d-1$$ is negative, therefore $$y + d - 1 < y$$.
    
    - > So $$x - 1 = y + d - 1 < y = \left \lfloor{x}\right \rfloor$$ 
    


## Property of Ceiling

> - $$x \leq \left \lceil{x}\right \rceil < x + 1$$

> - (You can prove this similarly to the way we proved the floor property!)

> - We usually represent numbers in base ten

<img src="https://i.imgur.com/8dmbsc7.png" width="600"/>

## Bases

> - In general, a number in the form of digits $$d_k d_{k-1} \ldots d_1 d_0$$ can be represented as
$$$$\sum_{i\in[0,k]}d_i t^i = d_kt^k + d_{k-1}t^{k-1}+ \ldots + d_1t^1 + d_0t^0$$$$ where $$t$$ is the base

> - All digits $$d_i$$ are in the range $$[0,t-1]$$

- >Let's go back to representing the number $$10,475$$ in base $$10$$

- >So the digits are $$d_4 = 1$$, $$d_3 = 0$$, $$d_2 = 4$$, $$d_1 = 7$$, $$d_0 = 5$$ and the base is $$t = 10$$

- >Which gives us what we got before: $$10,475 = 1 \cdot 10^4 + 0 \cdot 10^3 + 4 \cdot 10^2 + 7 \cdot 10^1 + 5 \cdot 10^0$$

- >Also note that all digits are between $$0$$ and $$9$$.

## Base 2

> - Often in computer science, we represent numbers in base $$2$$. This is also called "binary" representation.

> - Since our base $$t = 2$$, then our digits are in the range $$[0,1]$$. So basically, we are just looking at strings of $$0$$s and $$1$$s. (Often we call $$0$$s and $$1$$s "bits". $$8$$ bits is a byte.)

### Example

<img src="https://i.imgur.com/brCatgF.png" width="600"/>

## In Class Assignment

In groups, write (in English) the procedure for converting a number from binary to base 10. 

Then, write the procedure for converting a number from base 10 to binary.

Hint: start by thinking what steps would you take to convert $$10110$$ to $$22$$ and $$22$$ to $$10110$$, then generalize it to any number.

You can submit this as a group on Gradescope!

(It's okay if you're wrong! We will go over the right answer after you submit. The idea is to just see that you put effort in.)

## Length of Binary Messages 

If I want to express $$x$$ in binary, how long will it be? 

(In other words, how many bits will it take?)

- > Think about the procedure we just did for converting a number to binary. We find the highest power of $$2$$ that is less than or equal to $$x$$: $$k = \left \lfloor{\log_2(x)}\right \rfloor$$

- > We know this means that our string of bits will be of length $$k$$.

- > This can be generalized for any base $$b$$: The length of any number $$x$$ in base $$b$$ is $$\left \lfloor{\log_b(x)}\right \rfloor$$

## Length of Binary Messages

- While it makes sense to represent numbers in binary for computers, notice that it takes more digits to represent them. Think about it. Saying "$$10110$$" instead of "$$22$$" is longer. 

- So why do we do it? (Refer to video...)

## Useful Operator - Divides

For all integers $$a,b$$ we can say $$a$$ **divides** $$b$$, or $$a \mid b$$, iff there exists some integer $$m$$ such that $$a\cdot m = b$$.

### Example

> - We can say $$2$$ divides $$6$$, or $$2 \mid 6$$, because $$2 \cdot 3 = 6$$

Why do we define this using multiplication instead of division?

(In other words, why don't we say it as: "There exists an $$m$$ such that $$b/m = a$$?")

The reason is that we want it to be possible for $$m=0$$. 

Notice that if $$b = 0$$ and $$m = 0$$, then $$a$$ can be anything. From this we conclude that every number divides $$0$$.

$$\forall a \in \mathbb{Z}, a \mid 0$$






## Useful Operator - Mod

For positive Integers, $$x \bmod y$$ is the remainder of $$x/y$$.

More generally, $$x \bmod y = x - \left \lfloor{x/y}\right \rfloor \cdot y$$.

### Examples

- > $$5 \bmod 2 = 1$$

- > $$4 \bmod 2 = 0$$

- > $$-1 \bmod 2 = 1$$


- Note that the value of $$x \bmod y$$ is between $$0$$ and $$y-1$$.

    
    
## Congruence Modulo y

Another way we can express mods is via congruency.

$$x \equiv z \pmod y$$ reads as "$$x$$ is congruent to $$z$$ mod $$y$$".

What this means is that $$x \bmod y = z \bmod y$$.

### Example

- > $$4 \bmod 2 = 0$$ and $$6 \bmod 2 = 0$$, so $$4 \equiv 6 \pmod 2$$.

## Fun With Primes!

- Primes are a common conversation in both computer science and math. This is because they are incredibly useful!

- One popular application of primes is in cryptography. 

- Why are primes important in this? We will discuss that! But first let's learn a little more about primes.

<iframe src="https://drive.google.com/file/d/1ZUuo50GwpvDpz5Wj5--cC9fkr10uRbJT/preview" width="640" height="450" allow="autoplay"></iframe>

## Prime vs. Composite

A positive integer $$N$$ is **composite** if it can be written as the product of two smaller,
positive integers.

$$N$$ is composite $$\iff \exists a,b \in (1,N), N = a \cdot b$$

An integer $$p$$ is **prime** if it's not composite.

In other words, $$p$$'s only divisors are $$1$$ and itself.

## GCD + Relatively Prime Numbers

The **greatest common divisor** of two integers $$x$$ and $$y$$, denoted $$GCD(x,y)$$ is the largest positive integer that divides both $$x$$ and $$y$$.

### Example
- $$GCD(8,12) = 4$$
- $$GCD(3,6) = 3$$
- $$GCD(4,7) = 1$$

If $$GCD(x,y) = 1$$, then $$x$$ and $$y$$ are **relatively prime** (also called coprime).

## The Fundamental Theorem of Arithmetic

(It has the word "fundamental" in it so you know it's important!)

Every number can be written as a unique product of prime numbers.

- Proof by example (Not a real proof):

- > $$100 = 4 \cdot 25 = 2 \cdot 2 \cdot 5 \cdot 5$$
- > $$2020 = 2 \cdot 2 \cdot 5 \cdot 101$$

Come up with step-by-step process to find the prime factorization of a number.

(Do this using "brute force". E.g. no fancy coding techniques yet!)

In other words, if I give you a number $$x$$, and I tell you to find its prime factors, how would you do it?

Bonus: What is the runtime of this algorithm in "Big-O"?

## In Class Activity

- Use your algorithm to find the prime factorization of 2020.

- Use your algorithm to find the prime factorization of 2021.

Is one harder than the other? Why?

- One is harder because it's harder to factor out large prime numbers! (In other words, it takes longer!) Think about what this means for really large primes!

- Why is it useful to have numbers that are hard to factor? We will get back to that...

## Mod Review

For positive Integers, $$x \bmod y$$ is the remainder of $$x/y$$.

More generally, $$x \bmod y = x - \left \lfloor{x/y}\right \rfloor \cdot y$$.

- > $$5 \bmod 2 = 1$$

- > $$4 \bmod 2 = 0$$

- > $$-1 \bmod 2 = 1$$


- Note that the value of $$x \bmod y$$ is between $$0$$ and $$y-1$$.

## Mods in the Other direction

If I say a number is congruent to $$b \bmod y$$, then that means it is of the form $$y \cdot k + b$$ where $$k$$ is an integer. 

### Examples

- > $$1 \bmod 2$$ (odd numbers) $$\equiv 2k + 1$$

- > $$0 \bmod 2$$ (even number) $$\equiv 2k$$

- > $$3 \bmod 5 \equiv 5k + 3$$



## Exponent Encryption

- To encrypt $$x$$, we want to find an encryption exponent $$e$$ and a decryption exponent $$d$$ and an integer $$z$$ so that:

- > Our original message is: $$x$$

- > Our encrypted message is: $$x^e \bmod z$$

- > Our decrypted message is: $$(x^e)^d \bmod z = x$$

- We want it so that you *have* to know $$d$$ and $$z$$ to decrypt the message. 

- We also want it so that someone can know $$e$$ and $$z$$ and not figure out $$d$$ (and more importantly, $$x$$).

- Lastly, according to how we defined our decrypted message, we have to find an $$e$$ and $$d$$ such that $$(x^e)^d \bmod z = x$$.

## Asymmetric Encryption using Exponents and Mods

- We're going to talk about how to encrypt and decrypt numbers. (Remember, numbers can be used to represent words, like in ASCII.)

Say Bob wants to send a message $$x$$ to Alice.
Say Alice has encryption and decryption keys $$e, d$$ and integer $$z$$.


1. Alice sends Bob her *public key*: $$(e,z)$$  

1. Bob encrypts his message and sends it back to Alice: $$x^{e} \bmod z$$

1. Alice decrypts this message: $$(x^e)^d \bmod z = x$$


- Note that Bob doesn't know $$d$$, this is Alice's *private key*.

- So, we want it that Bob can know $$x^{e} \bmod z$$ and even $$(x^e)^d \bmod z$$, but he can't be able to figure out $$d$$. (It makes sense that $$d$$ would be hard to figure out since we're working with mods, because a lot of things will be equal...)

- Also we want to pick an $$e$$ and a $$d$$ such that $$(x^e)^d \bmod z = x$$.





## Useful Math

There is some math that will help us meet some of these requirements, so let's learn about that first.

**Fermat's Little Theorem** states: 

for all integers $$a$$ and all primes $$p>1$$, $$a^p \bmod p = a \bmod p$$.

Why? Let's watch a video...

You can use this to show:

for all integers $$a$$, if $$a$$ is not a multiple of $$p$$, then $$a^{p-1} \bmod p = 1 \bmod p$$



## Things we can derive from FLT

We can use FLT to prove the following statement:

Let $$p$$ and $$q$$ be distinct primes and let $$N = p \cdot q$$. 

For all integers $$k$$ and for $$m \in [0,N)$$,

$$m^{(p-1)(q-1)k+1} \bmod N = m \bmod N$$.

(Proof in 7.3.4 in book)

- What this means: We want to find some number $$y$$ that we can express as $$y = (p-1)(q-1)k+1$$.

- This is the same as saying: We want a $$y$$ such that $$y = 1 \bmod (p-1)(q-1)$$.

- Back to cryptography: 

- > Let $$z = (p-1)(q-1)$$ 
- > Let $$e \cdot d = y = 1 \bmod (p-1)(q-1)$$.

- Then, $$(x^e)^d \bmod z = x$$! 

