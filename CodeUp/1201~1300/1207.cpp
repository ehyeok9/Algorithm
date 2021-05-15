#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <cmath>
using namespace std;

int main(){
	int a, result = 0;
	
	for (int i = 0; i<4; i++){
		cin >> a;
		if (a == 1){
			result ++;
		}
	}
	
	switch(result){
		case 1:
			cout << "도";
			break;
		case 2:
			cout << "개";
			break;
		case 3:
			cout << "걸";
			break;
		case 4:
			cout << "윷";
			break;
		case 0:
			cout << "모";
			break;
	}
	return 0;
}
