"""
    AUTHOR - Atharva Deshpande.
    GITHUB - https://github.com/AtharvaD11
    QUESTION LINK -  https://www.codechef.com/LRNDSA01/problems/LAPIN
    
  """
  
  SOLUTION 1
  **************************************************************************
  
  for _ in range(int(input())):
    s = input()
    l = []
    r = []
    for i in range(len(s)//2):
        l.append(s[i])
        r.append(s[len(s)-1-i])
    for i in l:
        if i not in r or l.count(i)!=r.count(i):
            print("NO")
            break
    else:
        print("YES")
        
*****************************************************************************

SOLUTION 2
*****************************************************************************


def lapindrome(a):
    l = int(len(a)/2)
    return "YES" if sorted(a[:l]) == sorted(a[-l:]) else "NO"

n = int(input())
for i in range(n):
    s = input()
    print(lapindrome(s))
    

*****************************************************************************
