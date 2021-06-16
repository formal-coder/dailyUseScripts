// program to calculate the minutes per 1 minute according to the screen on time provided

#include <iostream>
using namespace std;

int main(){
	int batteryCharge, batteryDecrease, batteryRemain;
	double timeRemain, screenOnTime, minutes; //declaring variables

	cout << "Enter screenOnTime, batteryRemain, batteryCharged : ";
	cin >> screenOnTime >> batteryRemain >> batteryCharge;

	batteryDecrease = batteryCharge - batteryRemain;
	minutes = (screenOnTime*60.0)/batteryDecrease;
	timeRemain = minutes*batteryRemain;

	cout << "looking at the provided data, power consumption rate is " << minutes << " minutes per 1 percent" << endl;
	cout << "you will end up using for other " << timeRemain/60 << " hours or "<< timeRemain << " minutes" << endl;
	return 0 ;
}