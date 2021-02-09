"""
    AUTHOR  -  Atharva Deshpande
    GITHUB  -  https://github.com/AtharvaD11
    QUESTION LINK  -  https://www.codechef.com/problems/FCTRL2
"""

# we can easily calculate the factorials of large numbers in python (using recursive or iterative method). However, in c,c++ ; you need to use different approach

******************************************
def fact(n):
    if n==1:
        return 1
    else:
        return n*fact(n-1)

for _ in range(int(input())):
    n = int(input())
    print(fact(n))
    
