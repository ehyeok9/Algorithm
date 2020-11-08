#include <iostream>
using namespace std;

int main()
{
	int a, b, c;
	cout << "정수를 3개 입력하시오: ";
	cin >> a >> b >> c;
	int min;
	
	if (a < b){
		if (a < c){
			min = a;
		}
		else{
			min = c;
		}
	}
	else{
		if (b < c){
			min = b;
		}
		else{
			min = c;
		}
	}
	
	cout << min << endl;
	return 0;
}