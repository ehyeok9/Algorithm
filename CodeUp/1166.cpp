#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <cmath>
using namespace std;

int main(){
	int year;
	cin >> year;
	
	if (((year%4 ==0) && !(year%100 == 0)) || (year%400 == 0)){
		cout << "yes";
	}
	else {
		cout << "no";
	}
	return 0;
}
