#include <iostream>
#include <cmath>
using namespace std;

int main(){
	
	const double pi = 3.141592;
	int ban, height;
	
	cout << "원기둥 밑면의 반지름을 입력하시오: ";
	cin >> ban;
	cout << "원기둥의 높이를 입력하시오: ";
	cin >> height;
	
	cout << "원기둥의 부피는 " << pi * pow(ban,2) * height << "입니다."<< endl;
	return 0;
}