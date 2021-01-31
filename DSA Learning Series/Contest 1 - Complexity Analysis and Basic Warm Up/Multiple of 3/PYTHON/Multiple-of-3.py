"""
    AUTHOR  -  Atharva Deshpande
    GITHUB  -  https://github.com/AtharvaD11
    QUESTION LINK  -  https://www.codechef.com/LRNDSA01/problems/MULTHREE

"""
HINT -  Please learn Modulo Arithmetic first.


***********************************************
for _ in range(int(input())):
    k,d0,d1 = map(int,input().split())
    s = d0+d1
    total = 0
    if k== 2:
        total = s
    else:
        c = (2*s)%10 + (4*s)%10 +(6*s)%10 + (8*s)%10
        num_cycles = (k-3)//4
        total = s +(s%10) + (c*num_cycles)
        left_over = (k-3) - (num_cycles*4)
        p = 2
        for i in range(1,left_over+1):
            total += (p*s)%10
            p = (p*2)%10
    if total%3==0:
        print("YES")
    else:
        print("NO")
