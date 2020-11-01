#include <iostream>
#include <cmath>
using namespace std;

int main(){
	double x;
	
	cout << "다항식을 계산하기 위한 x의 값을 입력하시오 : " ;
	cin >> x;
	
	cout << (3*pow(x,3)) - (7*pow(x,2)) + 9 << endl;
	return 0;
}