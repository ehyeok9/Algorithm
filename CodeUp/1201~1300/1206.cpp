#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <cmath>
using namespace std;

int main(){
	int a,b;
	cin >> a >> b;
	
	if (b%a ==0){
		cout << a << "*" << b/a << "=" << b;
	}
	else if (a%b == 0){
		cout << b << "*" << a/b << "=" << a;
	}
	else{
		cout << "none";
	}
	return 0;
}
