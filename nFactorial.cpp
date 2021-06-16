#include <iostream>
using namespace std;
int main(){
    int product = 1, n,number;
    
    cout << "enter number : ";
    cin >> n;

    number = 1;
    while (number <= n){
        product = product * number;
        number = number+1;
    }
    cout << "Factorial of "<< n << " is " << product << endl;
    return 0;
}