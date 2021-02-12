""" 
    AUTHOR - Atharva Deshpande
    GITHUB - https://github.com/AtharvaD11
    QUESTION LINK  -  https://www.codechef.com/problems/ICL1902
"""

#***********************************************

for _ in range(int(input())):
    n = int(input())
    count = 0
    while(n):
        i = int(n**0.5)
        n -= i**2
        count += 1
    print(count)
