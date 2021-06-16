#include <iostream>
using namespace std;

int main() {
    // program to convert degree fahrenheit to degree celsius
    double celsius, fahrenheit;
    
    cout << "Enter temperature in fahrenheit : ";
    cin >> fahrenheit;
    
    celsius = (fahrenheit-32)*(5.0/9.0);
    
    cout << fahrenheit << " degree fahrenheit" << " converted into " << celsius << " degree celsius" << endl;
    
    cout << "Enter temperature in celsius : ";
    cin >> celsius;
    
    fahrenheit = (celsius*9.0/5.0)+32;
    
    cout << celsius << " degree celsius" << " converted into " << fahrenheit << " degree fahrenheit" << endl;
    return 0;
}