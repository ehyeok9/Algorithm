#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <cmath>
using namespace std;

int main(){
	int num;
	cin >> num;
	
	if (num%7==0){
		cout << "multiple";
	}
	else{
		cout << "not multiple";
	}
	return 0;
}
