#include <iostream>
using namespace std;

int main(){
	double distance, minute, second, result;
	
	cout << "달린 거리를 입력하시오(kmh): ";
	cin >> distance;
	cout << "달린 시간 중에서 분을 입력하시오: ";
	cin >> minute;
	cout << "달린 시간 중에서 초를 입력하시오: ";
	cin >> second;
	
	double hour = ((minute*60) + second)/ 3600;
	result = distance / hour;
	
	cout << "평균 속도는 " << result << "km/h입니다." << endl;
	return 0;
}