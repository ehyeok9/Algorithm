#include <iostream>
using namespace std;

int main(){
	int x, y, result;
	cout << "x좌표와 y좌표를 입력하시오: ";
	cin >> x >> y;
	result = (x>0) ? ((y>0) ? 1 : 4) : ((y>0) ? 2 : 3);
	cout << result << "사분면이다." << endl;
	return 0;
}