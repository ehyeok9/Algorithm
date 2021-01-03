#include <iostream>
using namespace std;

int main()
{
	char input;
	cout << "이스케이프 문자 입력하시오: ";
	cin >> input;
	
	switch (input){
		case '\t':
			cout << "탭문자입니다.";
			break;
		case '\n':
			cout << "줄바꿈문자입니다.";
			break;
		case '\b':
			cout << "백스페이스문자입니다.";
			break;
	}
	return 0; 
}