#include <iostream>
using namespace std;

int main(){
	int input;
	cout << "1-10까지의 숫자를 입력하시오: ";
	cin >> input;
	
	if (input == 2){
		cout << "1등에 당첨되셨습니다." << endl;
	}
	else if (input == 5){
		cout << "2등에 당첨되셨습니다." << endl;
	}
	else if (input == 7){
		cout << "3등에 당첨되셨습니다." << endl;
	}
	else{
		cout << "로또에 당첨되지 못하셨습니다." << endl;
	}
	return 0;
}