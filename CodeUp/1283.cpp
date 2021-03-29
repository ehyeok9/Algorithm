#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <cmath>
using namespace std;

int main(){
	double seed;
	int day;
	double grade,temp;
	cin >> seed >> day;
	grade = seed;
	
	for (int i=0; i < day; i++){
		cin >> temp;
		grade += (grade*(temp/100));
	}
	grade -= seed;
	cout << round(grade) << endl;
	if (round(grade) > 0){
		cout << "good";
	}
	else if (round(grade) < 0){
		cout << "bad";
	}
	else{
		cout << "same";
	}
	
	return 0;
}