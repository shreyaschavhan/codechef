"""   
    AUTHOR -  Atharva Deshpande
    GITHUB -  https://github.com/AtharvaD11
    QUESTION LINK  -  https://www.codechef.com/LRNDSA01/problems/ZCO14003
"""

*************************************************************************

n = int(input())
customers = []
for _ in range(n):
    ele = int(input())
    customers.append(ele)
customers.sort()
revenue = []
N = n
for i in range(n):
    revenue.append(customers[i]*N)
    N-=1
print(max(revenue))

*************************************************************************
