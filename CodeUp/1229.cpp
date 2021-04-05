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
	
	if (hegiht >= 160){
		standard = (hegiht - 100.0)*0.9;
	}
	else if (hegiht >= 150){
		standard = (hegiht -150)/2 +50;
	}
	else{
		standard = (hegiht -100);
	}
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

