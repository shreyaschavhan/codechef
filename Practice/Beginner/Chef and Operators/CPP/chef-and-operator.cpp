// Author - Shreyas Chavhan
// Github - https://www.github.com/shreyaschavhan

#include <bits/stdc++.h>
using namespace std;

int main(){
    ios_base :: sync_with_stdio(false);
    cin.tie(NULL);

    int T;
    cin >> T;
    while(T--){
        int A, B;
        cin >> A>> B;
        if(A < B){
            cout << "<" << '\n';
        }
        else if(A > B){
            cout << ">" << '\n';
        }
        else{
            cout << "=" << '\n';
        }
    }
    return 0;
}
