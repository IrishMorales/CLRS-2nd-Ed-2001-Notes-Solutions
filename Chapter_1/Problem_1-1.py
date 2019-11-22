import pandas as pd
from decimal import Decimal
import math

#function to return scientific notation
def get_sci_notation(t):
    return '%.2E' % Decimal(str(t))

'''
since we are finding the maximum n such that f(n) = t, given time t,
equate each f(n) to t
'''

'''
for lg(n) = t,
since lg(n) = log2(n)
n = 2^t
'''
def solve_lgn(t):
    return "2^" + get_sci_notation(t)

'''
for sqrt(n) = t where sqrt means square root,
n = t^2
'''
def solve_sqrtn(t):
    return get_sci_notation(int(t)**2)

'''
for n = t, n = t
^this is the hardest part of the entire book so far
'''

'''
for nlg(n) = t,
lg(n^n) = t
n^n = 2^t

Use Lambert-W function here. 
To do this, transform one side of the equation to xe^x
ln(n^n) = ln(2^t)
nln(n) = ln(2^t)
Since e^(ln(n)) = n
e^(ln(n))*ln(n) = ln(2^t)

Rearranging,
ln(n)*e^(ln(n)) = ln(2^t) 
Note that the left side is similar to xe^x
Using W to represent the Lambert W function,
ln(x) = W(ln(2^t))

From ln(x) = k, e^k = x
Thus,
x = e^W(ln(2^t))

At time of writing, there is no known solution to the
Lambert-W function except through iteration, bisection,
and use of complex software.
'''
def solve_nlgn(t):
    '''
    solve through iteration, takes very long time
    tmpn = 2
    while tmpn*math.log2(tmpn) < t:
        tmpn += 1
    #return highest possible n such that nlgn < t
    return tmpn - 1
    '''
    return "e^W(ln(2^" + get_sci_notation(t) + "))"


'''
for n^2 = t,
n = t^(1/2) (read as the square root of t)
'''
def solve_nsqrd(t):
    return get_sci_notation(t**(1/2))

'''
for n^3 = t,
n = t^(1/3) (read as the cube root of t)
'''
def solve_ncbd(t):
    return get_sci_notation(t**(1/3))

'''
for 2^n = t,
n = log2(t)
since lg(n) = log2(n)
n = lg(t)
'''
def solve_2pwrofn(t):
    return int(math.log2(t))

'''
for n! = t
try multiple values of n! in a loop
'''
def solve_nfact(t):
    tmpn = 2
    while math.factorial(tmpn) < t:
        tmpn += 1
    #return highest possible n such that n! < t
    return tmpn - 1

#store answers in a dataframe
functions = ['lg(n)','sqrt(n)','n','nlg(n)','n^2','n^3','2^n','n!']

ans = pd.DataFrame(columns = ["1 second", "1 minute", "1 hour", 
                              "1 day", "1 month", "1 year", "1 century"],
                   index = functions)

#fill all columns with the corresponding number of microseconds
#NOTE: answers must be in microseconds (1 second = 1 x 10^6 microseconds)
ans["1 second"] = ans["1 second"].fillna(1*10**6)
ans["1 minute"] = ans["1 minute"].fillna(60*1*10**6)
ans["1 hour"] = ans["1 hour"].fillna(60*60*1*10**6)
ans["1 day"] = ans["1 day"].fillna(24*60*60*1*10**6)
#assuming 1 month is 31 days
ans["1 month"] = ans["1 month"].fillna(31*24*60*60*1*10**6)
#assuming 1 year is 365 days
ans["1 year"] = ans["1 year"].fillna(365*24*60*60*1*10**6)
ans["1 century"] = ans["1 century"].fillna(100*365*24*60*60*1*10**6)

#apply appropriate function to each row
ans.loc["lg(n)", :] = ans.loc["lg(n)", :].apply(solve_lgn)
ans.loc["sqrt(n)", :] = ans.loc["sqrt(n)", :].apply(solve_sqrtn)
ans.loc["n", :] = ans.loc["n", :].apply(get_sci_notation)
ans.loc["nlg(n)", :] = ans.loc["nlg(n)", :].apply(solve_nlgn)
ans.loc["n^2", :] = ans.loc["n^2", :].apply(solve_nsqrd)
ans.loc["n^3", :] = ans.loc["n^3", :].apply(solve_ncbd)
ans.loc["2^n", :] = ans.loc["2^n", :].apply(solve_2pwrofn)
ans.loc["n!", :] = ans.loc["n!", :].apply(solve_nfact)

print(ans)

ans.to_csv("Problem_1-1_Answers.csv")