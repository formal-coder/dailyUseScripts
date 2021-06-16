#include <iostream>
using namespace std;

int main(){
	double radius, area, circumference;
	const double pi=3.141592654;

	cout << "Enter the radius of a circle : ";
	cin >> radius;

	area = pi*radius*radius;
	circumference = 2*pi*radius;

	cout << "area is : " << area << "cm" << endl;
	cout << "circumference is : " << circumference << "cm" << endl;
}