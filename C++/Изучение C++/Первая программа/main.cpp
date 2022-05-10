#include <iostream>
#include <cmath> 

using namespace std;

int main() {
    long long m, n, k, l, k1, k2;
    cout << "m, n" <<endl;
    for (m = 1; m <= 1000000000; m++) {
        for (n = 1; n <= 1000; n++) {
            l = (m * m) + (n * n);
            k = (m * n);
            k1 = pow((m + n), l);
            
            k2 = pow((l + 2), k);

            if (k1==k2) {
                cout << m << " " << n << endl; 
                break;
            }
        }
    }
}