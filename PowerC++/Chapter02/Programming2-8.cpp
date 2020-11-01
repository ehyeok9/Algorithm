#include <iostream>
#include <cmath>
using namespace std;

int main(){
	int time, minute, second, total;
	cout << "시, 분, 초 순서대로 값을 입력하시오: ";
	cin >> time >> minute >> second;
	
	total = second + (minute * 60) + (time*pow(60,2));
	cout << "이 시간 값을 초로 변환하였을 때의 값은 " << total << "초입니다." << endl;
	
	return 0;
}