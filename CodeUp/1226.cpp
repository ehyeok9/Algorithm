#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <cmath>
using namespace std;

int main(){
	vector<int> lotto;
	vector<int> mine;
	int a, result=0, bonus = 0;
	
	for (int i=0; i<7; i++){
		cin >> a;
		lotto.push_back(a);
	}
	
	for (int i=0; i<6; i++){
		cin >> a;
		mine.push_back(a);
	}
	
	for (int i=0; i < 6; i++){
		for (int j=0; j <7; j++){
			if (mine[i] == lotto[j] && j !=6){
				result += 1;
				continue;
			}
			else if (mine[i] == lotto[j] && j == 6){
				bonus += 1;
			}
		}
	}
	
	if (result == 6){
		cout << 1;
	}
	else if (result == 5 && bonus == 1){
		cout << 2;
	}
	else if (result == 5 && bonus == 0){
		cout << 3;
	}
	else if (result == 4){
		cout << 4;
	}
	else if (result == 3){
		cout << 5;
	}
	else{
		cout << 0;
	}
	return 0;
}

