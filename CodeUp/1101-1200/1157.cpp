#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <cmath>
using namespace std;

int main(){
	double num;
	cin >> num;
	
	if (num >= 50.0 && num <= 60.0){
		cout << "win";
	}
	else{
		cout << "lose";
	}
	return 0;
}
