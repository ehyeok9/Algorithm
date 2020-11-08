#include <iostream>
using namespace std;

int main()
{
	int x1, x2, y1, y2, z1, z2;
	
	cout << "첫번째 좌표값을 입력하시오: ";
	cin >> x1 >> x2;
	cout << "두번째 좌표값을 입력하시오: ";
	cin >> y1 >> y2;
	cout << "세번째 좌표값을 입력하시오: ";
	cin >> z1 >> z2;
	
	double result_1, result_2;
	result_1 = (y2-x2)/(y1-x1);
	result_2 = (z2-y2)/(z1-y1);
	
	if (result_1 == result_2){
		cout << "삼각형이 성립되지 않습니다." << endl;
	}
	else{
		cout << "삼각형이 성립됩니다." << endl;
	}
	return 0;	
}