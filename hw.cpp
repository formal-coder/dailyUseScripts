#include <iostream>
using namespace std;

int main(){
    int number, n, count=0;
    
    number =1;
    while (number <= 2010){
        if (number % 4 == 0 && !(number % 100 == 0) || number % 400 == 0){
            count = count + number;
        }
        ++number;
    }
    cout << count << endl;
    return 0;
}