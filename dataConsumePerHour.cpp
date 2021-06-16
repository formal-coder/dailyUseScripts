#include <iostream> //preprocessor directive
using namespace std; //declares we are using namespace function

int main(){
    float Mbps; //declaring variables
    float Mbpm, Mbph, MBph;
    
    cout << "Enter data consumption rate : ";
    cin >> Mbps; //take the user input
    
    Mbpm = Mbps*60;  //per second to per minute
    Mbph = Mbpm*60;  //minute to hour
    MBph = Mbph/8;  //bits to bytes
    
    cout << "Data consumption per hour is " << MBph << "MB per hour " << "at " << Mbps << " Mbps" << " rate." << endl;
    return 0;
}