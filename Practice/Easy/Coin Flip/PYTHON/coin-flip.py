"""
    AUTHOR  -  Atharva Deshpande
    GITHUB  -  https://github.com/AtharvaD11
    QUESTION LINK  -  https://www.codechef.com/LRNDSA01/problems/CONFLIP
"""

""" ALGORITHM  - After n rounds, elements has to count the number of heads or tails. If n is even, half of the coins will show heads and the other half will display tails.
                 If n is odd and the initial position of coins is H, and at the end we need to count H, then the number of H will be n//2 and the number of T will be n//2 + 1.
                 Same applies for n as odd and the initial position as T.
"""


for _ in range(int(input())):
    g = int(input())
    for j in range(g):
        i,n,q = map(int,input().split())
        if n%2==0:
            print(n//2)
        else:
            if i==q:
                print(n//2)
            else:
                print(n//2 + 1)
