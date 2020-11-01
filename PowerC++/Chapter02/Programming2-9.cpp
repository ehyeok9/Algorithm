#include <iostream>
using namespace std;

int main(){
	int value, cheon, baek, sip, ill;
	cout << "정수를 입력하시오: ";
	cin >> value;
	
	cheon = value/1000;
	value -= (cheon*1000);
	baek = value/100;
	value -= (100*baek);
	sip = value/10;
	value -= (10*sip);
	ill = value;
		
	cout << "천의 자리: " << cheon << endl;
	cout << "백의 자리: " << baek << endl;
	cout << "십의 자리: " << sip << endl;
	cout << "일의 자리: " << ill << endl;
	return 0;
}