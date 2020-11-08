#include <iostream>
#include <cmath>
using namespace std;

int main()
{
	char input;
	cout << "도형을 선택하시오: ";
	cin >> input;
	
	if (input == 'C'){
		double r;
		cout << "반지름을 입력하시오: ";
		cin >> r;
		cout << 3.14*pow(r,2) << endl;
	}
	else if (input == 'T'){
		double a,b;
		cout << "밑변과 높이를 입력하시오: ";
		cin >> a >> b;
		cout << a*b/2 << endl;
	}
	else if (input == 'R'){
		double e,u;
		cout << "밑변과 높이를 입력하시오: ";
		cin >> e >> u;
		cout << e*u << endl;
	}
	return 0;
}