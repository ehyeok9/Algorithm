#include <iostream>
using namespace std;

int main(){
	int feet, inch ;
	const double inch_value = 2.54;
	
	cout << "키를 입력하시오(피트): ";
	cin >> feet;
	cout << "키를 입력하시오(인치): ";
	cin >> inch;
	
	double total = (feet*12*inch_value) + (inch*inch_value);
	cout << feet << "피트 " << inch << "인치는 " << total << "cm입니다." << endl;
	
	return 0;
}