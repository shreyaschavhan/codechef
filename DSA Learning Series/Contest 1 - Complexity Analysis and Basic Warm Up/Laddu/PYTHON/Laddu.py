"""
    AUTHOR  -  Atharva Deshpande
    GITHUB  -  https://github.com/AtharvaD11
    QUESTION LINK  -  https://www.codechef.com/LRNDSA01/problems/LADDU
"""

*************************************************************

for _ in range(int(input())):
    n_nat = input().split()
    lst = []
    for i in range(int(n_nat[0])):
        lst.append(input().split())
    laddoos = 0
    for i in lst:
        if i[0] == 'CONTEST_WON':
            if int(i[1]) <=20:
                laddoos += (300 + (20-int(i[1])))
            else:
                laddoos += 300
        if i[0] == 'TOP_CONTRIBUTOR':
            laddoos += 300
        if i[0] == 'BUG_FOUND':
            laddoos += (int(i[1]))
        if i[0] == 'CONTEST_HOSTED':
            laddoos += 50
    if n_nat[1] == 'INDIAN':
        print(laddoos//200)
    else:
        print(laddoos//400)

