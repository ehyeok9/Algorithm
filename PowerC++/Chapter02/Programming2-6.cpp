#include <iostream>
using namespace std;

int main(){
	double value, pound, ons;
	
	cout << "무게를 입력하시오: ";
	cin >> value;
	pound = value*2.2;
	ons = pound*16;
	
	cout << value << "킬로그램은 " << pound << " 파운드입니다." << endl;
	cout << value << "킬로그램은 " << ons << " 온스입니다." << endl;
	
	return 0;
}