#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <cmath>
using namespace std;

int main(){
	double hegiht, weight;
	cin >> hegiht >> weight;
	double standard, ratio;
	standard = (hegiht - 100.0)*0.9;
	ratio = (weight -standard)*100.0/standard;
	
	if (ratio>20){
		cout << "비만";
	}
	else if (ratio >10){
		cout << "과체중";
	}
	else{
		cout << "정상";
	}
	return 0;
}

