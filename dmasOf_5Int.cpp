#include <iostream>
using namespace std;

/*takes five integers and, performs sum and difference operations */

int main(){

	//cout << "hello world!" << endl;
	int int1, int2, int3, int4, int5, sum, product, difference, quotient;

	cout << "enter five integers : ";
	cin >> int1 >> int2 >> int3 >> int4 >> int5;

	sum = int1 +int2 +int3 +int4 +int5 ;
	product =  int1*int2*int3*int4*int5 ;

	cout << "sum is " << sum << endl;
	cout << "product is " << product << endl;

	return 0;
}