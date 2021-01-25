/*
      AUTHOR  -  Atharva Deshpande
      GITHUB  -  https://github.com/AtharvaD11
      QUESTION LINK  -  https://www.codechef.com/LRNDSA01/problems/CARVANS
*/

/*
      ALGORITHM - (i) We create an array named cars and store the maximum speeds of all the cars in it.
                  (ii) We iterate through cars and check whether the speed of preceding car is greater than or equal to ith car.
                  (iii) If (ii) is true, we increment count. Else , we reduce the speed of ith car by difference of speeds of current and preceding car.
 */
 
#include <bits/stdc++.h>
using namespace std;
int main() {
    int t;
    cin >>t;
    while(t--){
        int n;
        cin >> n;
        int cars[n];
        for(int i=0;i<n;i++){
            cin >> cars[i];
        }
        int count = 1;
        if(n==1){
            cout << '1'<<endl;
        }
        else{
            for(int i=1;i<n;i++){
                if(cars[i]<=cars[i-1]){
                    count ++;
                }
                else{
                    cars[i] -= (cars[i]-cars[i-1]);
                }
            }
            cout << count << endl;
        }
    }
    return 0;
}
