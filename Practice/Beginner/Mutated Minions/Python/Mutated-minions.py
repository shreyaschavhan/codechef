"""
    AUTHOR  -  Atharva Deshpande
    GITHUB  -  https://github.com/AtharvaD11
"""


#*************************************************
for _ in range(int(input())):
    n,k=map(int,input().split())
    arr = list(map(int,input().split()))
    count = 0
    for i in range(n):
        if (arr[i]+k) %7 == 0:
            count +=1
    print(count)
