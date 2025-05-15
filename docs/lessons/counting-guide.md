---
layout: default
title: Counting Guide
contributors: Alyssa Byrnes
---

## Phrases to Know
For these phrases, assume we're talking about different sets/tuples we can make from the set \{1,2,3\}.

    * ``Order doesn't matter.'': This means that $$\{1,2,3\} = \{3,2,1\}$$. Notice this means we're talking about \emph{sets}. If order doesn't matter, we are counting \emph{combinations}.
    * ``Order matters.'': This means $$(1,2,3) \neq (3,2,1)$$. Notice this means we're talking about \emph{tuples}. If order matters, we are counting \emph{permutations}.
    * ``Repetition allowed.'': This means we can repeat elements in our set/tuples. So, $$\{3,3,3\}$$ would be a possibility we want to count.
    * ``No repetition.'': Every element shows up no more than once. 
    


## Formulas

These are the general formulas for computing sets/tuples of size $$k$$ from a set of size $$n$$.


    * If ``Order matters" and ``Repetition allowed": $$n^k$$
    * If ``Order matters" and ``No Repetition'': $$\frac{n!}{(n-k)!}$$
    * If ``Order doesn't matter'' and ``No Repetition'': $$\binom{n}{k} = \frac{n!}{k!(n-k)!}$$
    * If ``Order doesn't matter'' and ''Repetition allowed": $$\binom{k + n - 1}{k} = \frac{(k+n-1)!}{k!(n-1)!}$$. \\ (Don't worry about knowing this one. I just included it in case you're curious.)




## Other useful things to know

    * If you don't know if the formula you're using is correct, try it with a smaller input. (E.g. if you're looking at the set $$\{1,2,3,4,5\}$$ try it with the set $$\{1,2,3\}$$.) This will help you confirm you are using the right formula.
    * If you see a question that looks like ``Find all combinations/permutations that don't have element $$x$$''. You should just consider your input to be the number of elements in the set without $$x$$. For example, in the homework question, we had $$13$$ beers, and $$3$$ were IPAs. So when I ask for all possible flights without IPAs, you're really just doing all possible flights of the set of beers without IPAs, so you're looking at combinations from a set of size $$10$$ instead of $$13$$.
    * Notice, for permutations and combinations, we are talking about items of the same set. Often, we use the \emph{product rule} and \emph{sum rule} if we are talking about items in \emph{different} sets. So, if I say: there are $$3$$ socks and $$3$$ shoes, how many different sock/shoe pairings are possible. You multiply the size of your set of socks times the size of your set of shoes. $$3 \times 3 = 9$$.
    * If you see a question that looks like ``Find all combinations/permutations that don't contain both $$x$$ and $$y$$.'' You should find all possible combinations/permutations (including those with $$x$$ and $$y$$) and then subtract the number of combinations/permutations that would include $$x$$ and $$y$$.
    For example, if the question is: I have a set of shoes $$S = \{s_1,s_2,s_3\}$$ and socks $$O = \{o_1,o_2,o_3\}$$. However, shoe $$s_1$$ doesn't match with socks $$o_1$$ and $$o_2$$. Find all acceptable shoe/sock combinations. First we find the set of all possible combinations (using product rule): $$3 \times 3 = 9$$. Then we compute the number of not-matching combinations: $$|\{s_1,o_1\},\{s_1,o_2\}| = 2$$. Then we subtract: $$9-2 = 7$$ possible combinations.
    * You can also approach problems like these by summing up all \emph{allowed} sets. So, since $$s_1$$ can't match with $$o_1$$ or $$o_2$$, we consider all combinations of $$\{s_1\}$$ and $$\{o_3\}$$ plus all combinations of $$\{s_2,s_3\}$$ and $$\{o_1,o_2,o_3\}$$, so $$1 + 6 = 7$$.
    
