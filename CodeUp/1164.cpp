#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <cmath>
using namespace std;

int main(){
	int a, b, c;
	cin >> a >> b >> c;
	
	if (a <= 170 || b <= 170 || c <= 170){
		cout << "CRASH";
	}
	else{
		cout << "PASS";
	}
	
	return 0;
}
