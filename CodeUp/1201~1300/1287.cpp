#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <cmath>
using namespace std;

int main(){
	int num;
	cin >> num;
	string a = "*";
	for (int i=1; i <=9;i++){
		a.resize(num*i, '*');
		cout << a << endl;
	}
	return 0;
}
