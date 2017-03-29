# Collatz Conjecture

This is a micro-project just for fun to illustrate the Collatz Conjecture. From Wikipedia:

### Statement of the problem
Histogram of total stopping times for the numbers 1 to 100 million. Total stopping time is on the x axis, 
frequency on the y axis. Note that for all positive integers the histogram would be a completely different, 
exponentially-growing sequence (see #In reverse)

Consider the following operation on an arbitrary positive integer:
If the number is even, divide it by two.
If the number is odd, triple it and add one.
In modular arithmetic notation, define the function f as follows:

$$
f(n)={\begin{cases}n/2&{\text{if }}n\equiv 0{\pmod {2}}\\3n+1&{\text{if }}n\equiv 1{\pmod {2}}.\end{cases}}
$$

Now, form a sequence by performing this operation repeatedly, beginning with any positive integer, and taking the result at
each step as the input at the next.
In notation:

$$
 a_{i}={\begin{cases}n&{\text{for }}i=0\\f(a_{i-1})&{\text{for }}i>0\end{cases}}
$$

(that is: 

$a_{i}$ is the value of $ f $ applied to $ n $ recursively $ i $ times; 
$a_{i}=f^{i}(n)$.
The Collatz conjecture is: This process will eventually reach the number 1, regardless of which positive integer is chosen 
initially.
That smallest i such that $a_i = 1$ is called the total stopping time of $n$. The conjecture asserts that every $n$ has a 
well-defined total stopping time. If, for some $n$, such an $i$ doesn't exist, we say that $n$ has infinite total stopping time 
and the conjecture is false.
If the conjecture is false, it can only be because there is some starting number which gives rise to a sequence that does 
not contain 1. Such a sequence might enter a repeating cycle that excludes 1, or increase without bound. 
No such sequence has been found.

---

## How to use it:

Theris only one file (`collatz_conjecture.py`). Execute it on your terminal instance or your IDE. You specify the upper bound of the sampling interval as 
well as the number of integers to sample.
The program then samples this number of integers from the interval [1, upper bound] and for each, runs the collatz algorithm 
until 1 is reached.[1](##notes)
It then plots the sequence of numbers for each starting integer. See if you spot any patterns!

## Notes:
[1] The program does not make any provision to avoid infinite loops, ie. never reaching 1. If you experience something that 
looks like an infinite loop, you may have found a counter-example (or at leasat a candidate) to disprove the conjecture. 
Congratulations! But then again, you would need to have infinite time and memory to be sure it is a counter-example.
