# Chapter 1. Solutions - The Role of Algorithms in Computing

---

### 1.1 Algorithms
**1.1-1**
sorting - inventory checks

**1.1-2**
memory usage, simplicity of implementation

**1.1-3**
array
pros:
- can access any element at any time
- can be in more than one dimension
cons:
- fixed size
- relatively high memory usage

**1.1-4**
similarity: both find shortest path
difference: 
- shortest path problem ends at destination
- travelling salesman problem has multiple destinations & ends at origin

**1.1-5**
best - finding dimensions in architecture
approximate - solutions to differential equations

---

### 1.2 Algorithms as a technology
**1.2-1**
search engines - require algorithms to fetch and rank search results

**1.2-2**
8 _n_^2 < 64 _n_lg _n_
_n_ < 8lg _n_

From graphing,
1.1 <= _n_ <= 43.59
Therefore, insertion sort beats merge sort at
1 < _n_ < 43

**1.2-3**
100 _n_^2 < 2^_n_

By trying different values for _n_,
When n = 13, 100 _n_^2 > 2^_n_
When n = 14, 100 _n_^2 > 2^_n_
When n = 15, 100 _n_^2 < 2^_n_

Therefore, 100 _n_^2 < 2^_n_ at n = 15

---

### Problems
| 	   | 1 second      | 
| ---------|--------|
| lg _n_   | 19.9315|
| sqrt(_n_)| 1,000|
| _n_	   | 1,000,000|
| _n_lg _n_| 1.99 x 10^7|
| _n_^2	   | 1 x 10^12|
| _n_^3	   | 1 x 10^18 |
| 2^_n_    |        |
| _n_!	   |        |
