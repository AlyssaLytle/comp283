## Algorithms and Invariants

- An **algorithm** is just a set of instructions to solve a problem.

### Example

   > In class, you wrote an algorithm to find the prime factors of a number.

## What you will learn

- How to come up with an algorithm to solve a given problem
- (Monday) How to express that algorithm in pseudocode
- (Monday) What you can *say* about the algorithm (e.g. what kind of guarantees you can make about the outcome, how long it takes, etc.)

## An example

A classic problem is: "Given an array of integers, what is the index of the *maximum* number in the array?"

1. Write what would be your *input* to your algorithm.
   
   > - I will be inputting some array, $A$, for which I want to know the maximum element. 

2. Write an example (or examples) of the kind of output you want. (This will help with your planning process.)
    
   > - So, if $A = [1,7,5,3,10,2]$, we want an algorithm that will return $4$, because $A[4] = 10$ is the maximum element in the array.
   
3. Write what your general *output* will be.

   > - My algorithm will output an integer $max\_idx$ so that $A[max\_idx]$ is the maximum element in the array.
   

4. In English, let's think about how we will solve this.

   > - Look at every element in $A$ from left to right and remember the max element $max\_elem$ and its index $max\_idx$. If a bigger number comes along, make that bigger number your new $max\_elem$ and make its index your new $max\_idx$. 

5. Write what your *variables* will be. (In other words, what do you have to keep track of.)

   > - In my algorithm, my variables are $max\_elem$, which is the current maximum element, $max\_idx$ which is the index of the current maximum element. I also need some way to track what elements I've already looked at, so I'm going to have a variable $i$ which tells me the index of the current element I'm checking.
   
## In Class Activity

Today, we will practice completing these 5 steps for some problems. You do not have to turn this in, but you will need your answers to this to complete Monday's activity!

