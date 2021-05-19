#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <cmath>
using namespace std;

int main(){
	int a,b,c, result = 1;
	cin >> a >> b >> c;
	int ternal[3] = {a,b,c};
	
	for (int i=0; i <3; i++){
		if (ternal[i] <= 170){
			cout << "CRASH " << ternal[i];
			result =0;
			break;
		}
	}
	
	if (result == 1){
		cout << "PASS";
	}
	
	return 0;
}

