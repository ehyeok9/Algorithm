#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <cmath>
using namespace std;

int main(){
	int a;
	cin >> a;
	
	if (a > 20){
		cout << "비만";
	}
	else if (a > 10){
		cout << "과체중";
	}
	else{
		cout << "정상";
	}
	return 0;
}
