#include <iostream>
using namespace std;

int main(){
	cout << "키를 입력하시오: ";
	
	int height;
	cin >> height;
	
	const double inch_value = 2.54;
	
	int feet;
	double inch;
	
	feet = height/(12*inch_value);
	feet = (int)feet;
	inch = (height - (feet * 12 * inch_value))/inch_value;	
	
	cout << height << "cm는 " << feet << "피트 " << inch << " 인치입니다." << endl;
	
	return 0;
}