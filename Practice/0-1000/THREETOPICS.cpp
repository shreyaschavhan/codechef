#include <bits/stdc++.h>
using namespace std;

int main(){
    ios_base :: sync_with_stdio(false);
    cin.tie(NULL);

    int A, B, C, X;
    cin >> A >> B >> C >> X;

    if (X == A || X == B || X == C){
      cout << "YES";
    }
    else{
      cout << "NO";
    }
    return 0;
}
