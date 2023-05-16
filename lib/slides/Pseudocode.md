## Pseudocode

## Learning Objectives

- Learn how to write and read Pseudocode


## Basics of Coding

- For this course, you will need to know the fundamental concepts of coding: variables, operators, loops, and functions.
- *If you do not have any experience coding please reach out!*


## What is Pseudocode?

- Pseudocode is a generalized way of writing text that *resembles* code.
- It can be written many different ways, but the main goal is for it to clearly express the **input**, **return value**, and **functionality** of your code.

## Example

- A program that takes an integer as input, and returns that number plus one.


## Example

- A program that takes an integer as input, and returns that number plus one.

```
INPUT x : integer
x = x + 1
RETURN x
```

*(This syntax doesn't have to be copied exactly! It just needs to be clear what your program is doing! If you feel more comfortable using other syntax like Python or Java, that is fine!)*

## Example 2

- A program that inputs a list and returns the *value* of the maximum element.
- E.g. Input: `[1,7,5,3,10,2]` Return: `10`

## Example 2

- A program that inputs a list and returns the *value* of the maximum element.
- E.g. Input: `[1,7,5,3,10,2]` Return: `10`
- Start with English description:
    - Input a list
    - Start by assuming the first element (index 0) is the max
    - Loop through the list...
    - ...and any time I find a number larger than the believed max, make it the new max
    - Return the value of max


## Example 2

- A program that inputs a list and returns the *value* of the maximum element.

```
INPUT my_list: list
max = list[0]
FOR element in my_list:
    IF element > max:
        max = element
RETURN max
```

## Example 2 (By Index)

- A program that inputs a list and returns the *value* of the maximum element.

```
INPUT my_list: list
n = LENGTH(my_list)
max = list[0]
FOR index in [0,n-1]:
    element = my_list[index]
    IF element > max:
        max = element
RETURN max
```
