"""
    AUTHOR  -  Atharva Deshpande
    GITHUB  -  https://github.com/AtharvaD11
    QUESTION LINK  -  https://www.codechef.com/problems/FLOW006
"""

*******************************************
# cook your dish here

t = int(input())

for i in range(t):
    inp = input()
    sum = 0
    for j in inp:
        sum += int(j)
    print(sum)
