#include <iostream>
#include <cmath>
using namespace std;

int main(){
	int a,b,c;
	double result1, result2;
	
	cout << "a,b,c의 값을 입력하시오.";
	cin >> a >> b >> c;
	
	result1 = (-b+ sqrt(pow(b,2)-(4*a*c)))/(2*a);
	result2 = (-b - sqrt(pow(b,2)-(4*a*c)))/(2*a);
	
	cout << "2차 방정식의 값은 " << result1 << "과 " << result2 << "이다." << endl;
	return 0;
}