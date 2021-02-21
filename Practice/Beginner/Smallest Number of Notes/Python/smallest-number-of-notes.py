"""
  AUTHOR  -  Atharva Deshpande
  GITHUB  -  https://github.com/AtharvaD11
"""

#**************************************
for _ in range(int(input())):
    n = int(input())
    count =0
    arr = [100,50,10,5,2,1]
    i = 0
    while n:
        count += n//arr[i]
        n = n%arr[i]
        i+=1
    print(count)
