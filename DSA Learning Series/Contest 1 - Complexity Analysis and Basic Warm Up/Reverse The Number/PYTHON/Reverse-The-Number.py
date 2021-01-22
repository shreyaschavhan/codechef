"""

    AUTHOR - Atharva Deshpande.
    GITHUB - https://github.com/AtharvaD11
    QUESTION LINK - https://www.codechef.com/LRNDSA01/problems/FLOW007

"""
"""
    ALGORITHM - 
            The constraints denotes that the value of n range from 1<=n<=10^6. 
            (i) Convert the input integer(n) into string
            (ii) Print the reversed string by using slicing technique.

"""


n = int(input())
for _ in range(n):
    number = int(input())
    num = str(number)
    print(int(num[::-1]))
