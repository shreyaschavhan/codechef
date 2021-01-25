""" 
    AUTHOR  -  Atharva Deshpande
    GITHUB  -  https://github.com/AtharvaD11
    QUESTION LINK  -  https://www.codechef.com/LRNDSA01/problems/ZCO14003
    
"""
    ALGORITHM  -  (i) We store the budgets of potential costumers in customer array.
                  (ii) We iterate through customer array and store the product of number of customers(N) and budget into revenue while successively decrementing N.
                  (iii) Finally, we print the maximum value of revenue list
"""
    


***********************************************************************************************

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

***********************************************************************************************
