Alice is a college student. Her favorite subject is Statistics and probability. For testing her Bob, his friend give her a question. Bob give her a list L of N integers, and an integer T, and ask after that he will choose two numbers L and R randomly such that 0≤L≤R≤N. He asked Alice to find the probability that sum{A[L], .. A[R]} <= T.

Help Alice to find the probability.

## Input:
First line will contains two number N and T, N lines follow, each containing one number from list A.
## Output:
Output one number P to a maximum of 8 decimal places, the probability that sum{D[L],… D[R]} <= T.

## Constraints
1≤N≤100000

1≤A[i]≤1e7
## Sample Input:
5 10

4

5

3

7

1
## Sample Output:
0.6
## EXPLANATION:
[4,5,3,7,1]

[4],[5],[3],[7],[1],[4,5],[5,3],[3,7],[7,1]

out of possible 15.

thus 9/15 = 0.6


```
All submissions for this problem are available.
Author:	3★honesthacker
Tags:	honesthacker
Date Added:	2-02-2021
Time Limit:	1 secs
Source Limit:	50000 Bytes
Languages:	CPP14, C, JAVA, PYTH 3.6, PYTH, CS2, ADA, PYPY, PYP3, TEXT, CPP17, PAS fpc, RUBY, PHP, NODEJS, GO, TCL, HASK, PERL, SCALA, kotlin, BASH, JS, PAS gpc, BF, LISP sbcl, CLOJ, LUA, D, R, CAML, rust, ASM, FORT, FS, LISP clisp, SQL, swift, SCM guile, PERL6, CLPS, WSPC, ERL, ICK, NICE, PRLG, ICON, PIKE, COB, SCM chicken, SCM qobi, ST, NEM, SQLQ
```
