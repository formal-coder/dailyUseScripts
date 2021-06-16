#include <iostream>
using namespace std;

int main(){
	double curvedSurfaceArea, totalSurfaceArea, width, height, volume, radius;
	double const pi=3.141592;

	cout << "Enter the radius, then height : ";
	cin >> radius >> height;

	totalSurfaceArea = 2*pi*radius*(height+radius);
	curvedSurfaceArea = 2*pi*radius*height;
	volume = pi*radius*radius*height;

	cout << "curvedSurfaceArea is : " << curvedSurfaceArea << "cm" << endl;
	cout << "totalSurfaceArea is : " << totalSurfaceArea << "cm" << endl;
	cout << "volume is : " << volume << "cm" << endl;
	return 0;
}