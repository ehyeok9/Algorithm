#include <iostream>
using namespace std;

int main(){
	short height, landspace, portrait;
	
	cout << "가로, 세로, 높이 순으로 입력하되 200은 넘기면 안 되용 ! : ";
	cin >> landspace >> portrait >> height;
	
	cout << landspace * portrait * height << endl;
	
	return 0;
}