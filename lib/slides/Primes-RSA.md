---
title: PrimesRSA
theme: dracula
center: false
transition: 'none'
contributors: Alyssa Byrnes
---


## Fun With Primes!
<div id="content">

- Primes are a common conversation in both computer science and math. This is because they are incredibly useful!
- One popular application of primes is in cryptography. 
- Why are primes important in this? We will discuss that! But first let's learn a little more about primes.

<iframe src="https://drive.google.com/file/d/1ZUuo50GwpvDpz5Wj5--cC9fkr10uRbJT/preview" width="640" height="450" allow="autoplay"></iframe>


</div>


## Prime vs. Composite

A positive integer $N$ is **composite** if it can be written as the product of two smaller,
positive integers.

$N$ is composite $\iff \exists a,b \in (1,N), N = a \cdot b$

An integer $p$ is **prime** if it's not composite.

In other words, $p$'s only divisors are $1$ and itself.


## GCD + Relatively Prime Numbers

The **greatest common divisor** of two integers $x$ and $y$, denoted $GCD(x,y)$ is the largest positive integer that divides both $x$ and $y$.

### Example
- $GCD(8,12) = 4$
- $GCD(3,6) = 3$
- $GCD(4,7) = 1$

If $GCD(x,y) = 1$, then $x$ and $y$ are **relatively prime** (also called coprime).


## The Fundamental Theorem of Arithmetic
<div id="content">

(It has the word "fundamental" in it so you know it's important!)

Every number can be written as a unique product of prime numbers.

Proof by example (Not a real proof):

-  $100 = 4 \cdot 25 = 2 \cdot 2 \cdot 5 \cdot 5$
-  $2020 = 2 \cdot 2 \cdot 5 \cdot 101$


</div>


<!-- ## In Class Activity
<div id="content">

Come up with step-by-step process to find the prime factorization of a number.

(Do this using "brute force". E.g. no fancy coding techniques yet!)

In other words, if I give you a number $x$, and I tell you to find its prime factors, how would you do it?

Bonus: What is the runtime of this algorithm in "Big-O"?


</div>


## In Class Activity
<div id="content">

- Use your algorithm to find the prime factorization of 2020.

- Use your algorithm to find the prime factorization of 2021.

Is one harder than the other? Why?

- One is harder because it's harder to factor out large prime numbers! (In other words, it takes longer!) Think about what this means for really large primes!

- Why is it useful to have numbers that are hard to factor? We will get back to that...


</div> -->

## Power of Primes

- Try it yourself: come up with step-by-step process to find the prime factorization of a number.
- Use your algorithm to find the prime factorization of both 2020 and 2021.

## Power of Primes

A number that is a product of two large primes can take an extremely long time to factor.

Consider the number

25195908475657893494027183240048398571429282126204032027777137836043662020707595556264018525880784406918290641249515082189298559149176184502808489120072844992687392807287776735971418347270261896375014971824691165077613379859095700097330459748808428401797429100642458691817195118746121515172654632282216869987549182422433637259085141865462043576798423387184774447920739934236584823824281198163815010674810451660377306056201619676256133844143603833904414952634432190114657544454178424020924616515723350778707749817125772467962926386356373289912154831438167899885040445364023527381951378636564391212010397122822120720357

It is 617 digits long, and 2048 bits. It is also the product of two large primes!

It is estimated that it would take a classical computer around 300 trillion years to factor this!

This is the foundation of RSA Cryptography.


## Mod Review
<div id="content">

For positive Integers, $x \bmod y$ is the remainder of $x/y$.

More generally, $x \bmod y = x - \left \lfloor{x/y}\right \rfloor \cdot y$.

### Examples

-  $5 \bmod 2 = 1$
-  $4 \bmod 2 = 0$
-  $-1 \bmod 2 = 1$

</div>


## Mods in the Other direction
<div id="content">

If I say a number is congruent to $b \bmod y$, then that means it is of the form $y \cdot k + b$ where $k$ is an integer. 

### Examples

-  $1 \bmod 2$ (odd numbers) $\equiv 2k + 1$
-  $0 \bmod 2$ (even numbers) $\equiv 2k$
-  $3 \bmod 5 \equiv 5k + 3$

</div>


## Exponent Encryption
<div id="content">

- To encrypt $x$, we want to find an encryption exponent $e$ and a decryption exponent $d$ and an integer $z$ so that:
-  Our original message is: $x$
-  Our encrypted message is: $x^e \bmod z$
-  Our decrypted message is: $(x^e)^d \bmod z = x$
- We want it so that you *have* to know $d$ and $z$ to decrypt the message. 
- We also want it so that someone can know $e$ and $z$ and not figure out $d$ (and more importantly, $x$).
- Lastly, according to how we defined our decrypted message, we have to find an $e$ and $d$ such that $(x^e)^d \bmod z = x$.
</div>

## Asymmetric Encryption using Exponents and Mods
<div id="content">

- We're going to talk about how to encrypt and decrypt numbers. (Remember, numbers can be used to represent words, like in ASCII.)

Say Bob wants to send a message $x$ to Alice.
Say Alice has encryption and decryption keys $e, d$ and integer $z$.


1. Alice sends Bob her *public key*: $(e,z)$  

1. Bob encrypts his message and sends it back to Alice: $x^{e} \bmod z$

1. Alice decrypts this message: $(x^e)^d \bmod z = x$


- Note that Bob doesn't know $d$, this is Alice's *private key*.

- So, we want it that Bob can know $x^{e} \bmod z$ and even $(x^e)^d \bmod z$, but he can't be able to figure out $d$. (It makes sense that $d$ would be hard to figure out since we're working with mods, because a lot of things will be equal...)

- Also we want to pick an $e$ and a $d$ such that $(x^e)^d \bmod z = x$.



</div>


## Useful Math
<div id="content">

There is some math that will help us meet some of these requirements, so let's learn about that first.

**Fermat's Little Theorem** states: 

for all integers $a$ and all primes $p>1$, $a^p \bmod p = a \bmod p$.

Why? Let's watch a video...



</div>


## Useful Math
<div id="content">

There is some math that will help us meet some of these requirements, so let's learn about that first.

**Fermat's Little Theorem** states: 

for all integers $a$ and all primes $p>1$, $a^p \bmod p = a \bmod p$.

Why? Let's watch a video...

You can use this to show:

for all integers $a$, if $a$ is not a multiple of $p$, then $a^{p-1} \bmod p = 1 \bmod p$




</div>


## Things we can derive from FLT
<div id="content">

We can use FLT to prove the following statement:

Let $p$ and $q$ be distinct primes and let $N = p \cdot q$. 

For all integers $k$ and for $m \in [0,N)$,

$m^{(p-1)(q-1)k+1} \bmod N = m \bmod N$.

(Proof in 7.3.4 in book)

- What this means: We want to find some number $y$ that we can express as $y = (p-1)(q-1)k+1$.

- This is the same as saying: We want a $y$ such that $y = 1 \bmod (p-1)(q-1)$.

- Back to cryptography: 

-  Let $z = (p-1)(q-1)$ 
-  Let $e \cdot d = y = 1 \bmod (p-1)(q-1)$.

- Then, $(x^e)^d \bmod z = x$! 


</div>


## RSA Encryption
<div id="content">

- Remember that our decrypted message is $(x^e)^d \bmod N = x$ and we want $d$ to be hard to figure out.

- RSA encryption relies on the use of a number $N$ that is a product of *very* large prime numbers $p$ and $q$. You make $N$ public, but your algorithm relies on $p$ and $q$, so you want them to be hard to figure out! This is why it's useful that primes are hard to factor. (Aka it is difficult to find out $p$ and $q$ from $N$.)

- Let $z = (p-1)(q-1)$. (Since $p$ and $q$ are hard to find out, $z$ is hard for a hacker to find out.)

- Choose encryption exponent $e$ so that $GCD(e, z) = 1$ and then choose decryption exponent $d$ so that $e \cdot d = 1 \bmod (p-1)(q-1)$. (Again, since $z$ is hard to find out, $d$ will be hard to find out, even if the hacker knows $e$.)

- Based on the last slide, since $e \cdot d = 1 \bmod (p-1)(q-1)$, we know that any message $(x^e)^d \bmod N = x$.



</div>


## Biggest RSA Takeways
<div id="content">

- Understand why it's useful to know about primes. Eventually you might need to prove something using facts about primes! (Don't worry about that yet, though.)

- Understand the rules of RSA. (I won't make you generate your own keys, but you might have to work with existing ones!)

- Know the definitions we talked about (prime, coprime, mods, etc.)


</div>