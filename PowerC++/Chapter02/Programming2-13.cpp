#include <iostream>
using namespace std;

int main(){
	cout << "섭씨 온도를 입력하시오: ";
	double temp, result;
	cin >> temp;
	result = temp + 273.16;
	cout << "절대온도는 " << result << "입니다." << endl;
	return 0;
}