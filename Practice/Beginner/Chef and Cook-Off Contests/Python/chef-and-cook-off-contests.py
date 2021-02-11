"""
    AUTHOR  -  Atharva Deshpande
    GITHUB  -  https://github.com/AtharvaD11
    QUESTION LINK  -  https://www.codechef.com/problems/C00K0FF
"""

#**************************************************************
from collections import Counter
for _ in range(int(input())):
    n = int(input())
    arr = []
    for i in range(n):
        arr.append(input())
    arr = Counter(arr)
    if arr['cakewalk'] >= 1 and arr['simple'] >= 1 and arr['easy'] >= 1 and (arr['easy-medium'] >= 1 or arr['medium'] >=1) and (arr['medium-hard']>=1 or arr['hard']>=1):
        print('Yes')
    else:
        print('No')
