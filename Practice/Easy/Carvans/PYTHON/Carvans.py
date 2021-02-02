""" 
      AUTHOR  -  Atharva Deshpande
      GITHUB  -  https://github.com/AtharvaD11
      QUESTION LINK  -  https://www.codechef.com/LRNDSA01/problems/CARVANS
"""

""" 
      ALGORITHM - (i) We create an array named cars and store the maximum speeds of all the cars in it.
                  (ii) We iterate through cars and check whether the speed of preceding car is greater than or equal to ith car.
                  (iii) If (ii) is true, we increment count. Else , we reduce the speed of ith car by difference of speeds of current and preceding car.
 """
 
 
 
 for _ in range(int(input())):
    n = int(input())
    cars = list(map(int,input().split()))
    count = 1
    if n==1:
        print(1)
    else:
        for i in range(1,n):
            if cars[i] <= cars[i-1]:
                count +=1
            else:
                cars[i] -= (cars[i] - cars[i-1])
        print(count)
