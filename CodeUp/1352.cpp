#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <cmath>
using namespace std;

int main(){
	int num;
	cin >> num;
	
	for (int i=0; i < num ; i++){
		for (int j=0; j < num; j++){
			cout << "*";
		}
		cout << endl;
	}
	
	return 0;
}

