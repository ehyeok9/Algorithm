#include <iostream>
using namespace std;

int main(){
	int a, b, c, day = 1;
	cin >> a >> b >> c;
	
	while(true){
		if ((day%a == 0) && (day%b==0) && (day%c==0)){
			break;
		}
		day++;
	}
	
	cout << day;
	return 0;
}