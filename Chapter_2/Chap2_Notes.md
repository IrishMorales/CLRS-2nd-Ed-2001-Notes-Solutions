# Chapter 2. Notes - Getting Started

---

### 2.1 Insertion Sort
- sorting algorithm similar to arranging cards in a deck  
Ex. Input  = [2, 5, -12, 32, 4] <-- unsorted numbers  
    Output = [-12, 2, 4, 5, 32] <-- sorted numbers
- efficient for small input
- sorted in place

_keys_ - numbers to be sorted

_See implementation/pseudocode in insertion-sort.cpp_

**Loop invariants and the correctness of insertion sort**
_loop invariants_ 
- what **shouldn't** change when a loop is run
- condition that is constant throughout loop  
Ex. for (int i=0; i is less than n; ++i <-- loop variant: i should not exceed n
- can be used to prove correctness of algorithm
- has initialization, maintenance, termination

To prove an algorithm is correct, loop invariant must be true:  
_Initialization_ - before the loop starts  
_Maintenance_ - before and after each iteration  
_Termination_ - after the loop ends

Note: 
_initialization_ is **after** assigning counter variable and  
**before** checking the condition for the first time

Ex. for (int i=0; i is less than n; ++i)
- initialization is after setting i = 0 and before checking i is less than n
- maintenance is before checking i is less than n on other iterations
- termination is when i equals n

**Pseudocode conventions**
- indentation is not enough to indicate structure because indentation is hard to read if printed across multiple pages

---

### 2.2 Analyzing algorithms
- predicting the resources that an algorithm will use
- usually computational time

_Random-access memory (RAM) model_ 
- theoretical model for analyzing algorithms
- one-processor model, instructions happen one after the other w/ no overlap

_input size_
- depends on the problem
- could be number of input elements, number of bits used by input, etc.

_running time_
- number of steps done by algorithm
