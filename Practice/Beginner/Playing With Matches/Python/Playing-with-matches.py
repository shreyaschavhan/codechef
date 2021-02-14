"""
    AUTHOR  -  Atharva Deshpande
    GITHUB  -  https://github.com/AtharvaD11
    QUESTION LINK  -  https://www.codechef.com/problems/MATCHES
"""

#*****************************************************

for _ in range(int(input())):
    a,b = map(int,input().split())
    arr = [6, 2, 5, 5, 4, 5, 6, 3, 7, 6]
    c = str(a+b)
    sum = 0
    for i in c:
        sum+= arr[int(i)]
    print(sum)
    
