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
        int activities;
        string origin;
        cin >> activities >> origin;
        int LADDU = 0;
        while(activities--){
            string activity;
            cin >> activity;
            if(!activity.compare("CONTEST_WON")){
                int rank;
                cin >> rank;
                LADDU += 300;
                if(rank < 20){
                    LADDU += (20 - rank);
                }
            }
            if(!activity.compare("TOP_CONTRIBUTOR")){
                LADDU += 300;
            }
            if(!activity.compare("BUG_FOUND")){
                int severity;
                cin >> severity;
                LADDU += severity;
            }
            if(!activity.compare("CONTEST_HOSTED")){
                LADDU += 50;
            }
        }
        if(origin == "INDIAN"){
            cout << LADDU/200 << '\n';
        }
        else{
            cout << LADDU/400 << '\n';
        }
    }
    return 0;
}
