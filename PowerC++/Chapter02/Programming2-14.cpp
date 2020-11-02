#include <iostream>
using namespace std;

int main(){
	double money, plus;
	
	cout << "예금액을 입력하시오: ";
	cin >> money;
	cout << "연이율을 입력하시오(단위 퍼센트): ";
	cin >> plus;
	
	for (int i=0; i < 2; i++){
		money += ((money/100)*plus);
	}
	
	cout << "2년 후의 예금액은 " << money << "입니다." << endl;
	
	return 0;
}