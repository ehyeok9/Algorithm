#include <iostream>
using namespace std;

int main()
{
	int first, second;
	cout << "첫번째 피연산자를 입력하시오: ";
	cin >> first;
	cout << "두번째 피연산자를 입력하시오: ";
	cin >> second;
	
	cout << first << " + " << second << " 은 " << first+second << endl;
	cout << first << " - " << second << " 은 " << first-second << endl;
	cout << first << " * " << second << " 은 " << first*second << endl;
	cout << first << " / " << second << " 은 " << first/second << endl;
	cout << first << " % " << second << " 은 " << first%second << endl;
	
	
	return 0;
}
