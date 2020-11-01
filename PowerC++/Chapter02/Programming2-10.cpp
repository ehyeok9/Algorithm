#include <iostream>
using namespace std;

int main(){
	int start, end, use;
	cout << "출발한 지점의 주행 거리계: ";
	cin >> start;
	cout << "도착한 지점의 주행 거리계: ";
	cin >> end;
	cout << "사용한 연료: ";
	cin >> use;
	
	cout << "연비는 " << (double)((end-start)/use) << "km/l입니다." << endl;
	
	return 0;
}