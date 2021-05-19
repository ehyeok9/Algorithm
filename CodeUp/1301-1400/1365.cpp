#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <cmath>
using namespace std;

int main(){
	int value;
	cin >> value;
	char list[value + 1][value + 1];
	
	for (int i=1; i< value+1; i++){
		for (int j=1; j < value+1; j++){
			list[i][j] = ' ';
		}
	}
	
	for (int i=1; i < value+1; i++){
		list[1][i] = '*';
		list[value][i] = '*';
		list[i][1] = '*';
		list[i][value] = '*';
	}
	
	for (int i= 1; i < value +1; i++){
		list[i][i] = '*';
		list[value-i+1][i] = '*';
	}
	
	for (int i = 1; i < value+1; i++){
		for (int j=1; j < value+1; j++){
			cout << list[i][j];
		}
		cout << endl;
	}
	return 0;
}

