#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <cmath>
using namespace std;

int main(){
	int a,b;
	cin >> a >> b;
	a /= 10000;
	
	if ( b == 1 || b == 2){
		a = 100-a;
		cout << a + 13;
	}
	else{
		a = 12 - a;
		cout << a +1;
	}
	return 0;
}
