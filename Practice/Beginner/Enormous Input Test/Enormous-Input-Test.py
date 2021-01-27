""" 
    AUTHOR  -  Atharva Deshpande
    GITHUB PROFILE -  https://github.com/AtharvaD11
    QUESTION LINK  -  https://www.codechef.com/problems/INTEST
"""


(n, k) = map(int, input().split(' '))

ans = 0

for i in range(n):
	x = int(input())
	if x % k == 0:
		ans += 1

print(ans)	
