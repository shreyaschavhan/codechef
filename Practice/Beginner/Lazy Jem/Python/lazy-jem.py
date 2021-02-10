"""
    AUTHOR - Atharva Deshpande
    GITHUB - https://github.com/AtharvaD11
    QUESTION LINK  - https://www.codechef.com/problems/TALAZY
"""

for _ in range(int(input())):
    n,b,m = map(int,input().split())
    total_min = 0
    while(n):
        if n%2!=0:
            quo = (n+1)//2
            rem = n-quo
            total_min += quo*m + b
            n = rem
            m *= 2
        else:
            quo = n//2
            rem = n-quo
            total_min += quo*m + b
            n = rem
            m *= 2
    print(total_min-b)


