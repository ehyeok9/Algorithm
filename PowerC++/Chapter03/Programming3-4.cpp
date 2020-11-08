#include <iostream>
#include <cmath>
using namespace std;

int add(int num1, int num2);
int minu(int num1, int num2);
int multiple(int num1, int num2);
int divide(int num1, int num2);

int main()
{
	char input;
	int num1, num2;
	
	while (true){
		cout << "연산을 선택하시오: ";
		cin >> input;
		
		if (input == 'Q'){
			break;
		}
		
		cout << "두 수를 공백으로 분리하여 입력하시오: ";
		cin >> num1 >> num2;
		
		switch (input){
			case '+':
				cout << add(num1,num2) << endl;
				break;
			case '-':
				cout << minu(num1,num2) << endl;
				break;
			case '*':
				cout << multiple(num1,num2) << endl;
				break;
			case '/':
				cout << divide(num1,num2) << endl;
				break;
		}
		
	} 
	return 0;
}

int add(int num1, int num2){
	return num1 + num2;
}

int minu(int num1, int num2){
	return num1 - num2;
}

int multiple(int num1, int num2){
	return num1 * num2;
}
int divide(int num1, int num2){
	if (num2 == 0){
		cout << "zero division error 남" << endl;
		return -1;
	}
	else{
		return num1 / num2;
	}
}