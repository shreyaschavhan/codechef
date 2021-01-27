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
        cin >> A >> B;
        cout << max(A, B) << " " << A + B << '\n';
    }
    return 0;
}
