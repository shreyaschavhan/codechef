"""
    AUTHOR  -  Atharva Deshpande
    GITHUB  -  https://github.com/AtharvaD11
    QUESTION LINK -  https://www.codechef.com/LRNDSA01/problems/FCTRL
"""

"""
  ALGRITHM  -  Factorials of all n>= 5 contains trailing zeroes. So, we keep on dividing n till n becomes < 5 and simultaneously keep on summing the quotient.  The total sum of all
                the quotients is our number of zeroes.
"""

*****************************************

t = int(input())
for _ in range(t):
    n = int(input())
    zeroes = 0
    quo = n
    while True:
        quo = quo//5
        zeroes += quo
        if quo < 5:
            break
    print(zeroes)

*******************************************
