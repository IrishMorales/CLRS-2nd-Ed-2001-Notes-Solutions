# Chapter 1. Solutions - The Role of Algorithms in Computing

---

### 1.1 Algorithms
**1.1-1**  
sorting - inventory checks

**1.1-2**  
memory usage, simplicity of implementation

**1.1-3**  
array pros:
- can access any element at any time
- can be in more than one dimension  
array cons:
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
**1-1**  
Assuming 1 month = 31 days and 1 year = 365 days  
_See "Problem 1-1.py" for computations_

|         | 1 second            | 1 minute            | 1 hour              | 1 day               | 1 month             | 1 year              | 1 century           |  
|---------|---------------------|---------------------|---------------------|---------------------|---------------------|---------------------|---------------------|  
| lg(n)   | 2^1.00E+06          | 2^6.00E+07          | 2^3.60E+09          | 2^8.64E+10          | 2^2.68E+12          | 2^3.15E+13          | 2^3.15E+15          |  
| sqrt(n) | 1.00E+12            | 3.60E+15            | 1.30E+19            | 7.46E+21            | 7.17E+24            | 9.95E+26            | 9.95E+30            |  
| n       | 1.00E+06            | 6.00E+07            | 3.60E+09            | 8.64E+10            | 2.68E+12            | 3.15E+13            | 3.15E+15            |  
| nlg(n)  | e^W(ln(2^1.00E+06)) | e^W(ln(2^6.00E+07)) | e^W(ln(2^3.60E+09)) | e^W(ln(2^8.64E+10)) | e^W(ln(2^2.68E+12)) | e^W(ln(2^3.15E+13)) | e^W(ln(2^3.15E+15)) |  
| n^2     | 1.00E+03            | 7.75E+03            | 6.00E+04            | 2.94E+05            | 1.64E+06            | 5.62E+06            | 5.62E+07            |  
| n^3     | 1.00E+02            | 3.91E+02            | 1.53E+03            | 4.42E+03            | 1.39E+04            | 3.16E+04            | 1.47E+05            |  
| 2^n     | 19                  | 25                  | 31                  | 36                  | 41                  | 44                  | 51                  |  
| n!      | 9                   | 11                  | 12                  | 13                  | 15                  | 16                  | 17                  |
