#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <cmath>
using namespace std;

int main(){
	int num;
	cin >> num;
	string str = "*";
	for (int i=num; i >= 1 ; i--){
		str.resize(i, '*');
		cout << str << endl;
	}
	
	return 0;
}

