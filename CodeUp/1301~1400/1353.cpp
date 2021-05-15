#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <cmath>
using namespace std;

int main(){
	int num;
	cin >> num;
	
	for (int i=1; i <= num ; i++){
		for (int j=1; j <= i; j++){
			cout << "*";
		}
		cout << endl;
	}
	
	return 0;
}

