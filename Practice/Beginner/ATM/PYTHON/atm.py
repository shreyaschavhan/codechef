"""
    AUTHOR  -  ATHARVA DESHPANDE
    GITHUB  -  https://github.com/AtharvaD11
    QUESTION LINK - https://www.codechef.com/problems/HS08TEST
    
"""

*************************************

x,y = map(float,input().split())
if x%5==0 and y-x-0.5 >=0:
    print("{:.2f}".format(y-x-0.5))
else:
    print("{:.2f}".format(y))
    
**************************************
