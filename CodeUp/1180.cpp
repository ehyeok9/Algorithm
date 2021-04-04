#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <cmath>
using namespace std;

int main(){
	string str;
	cin >> str;
	reverse(str.begin(), str.end());
		
	int i = stoi(str)*2;
	
	if (i >= 100){
		i -= 100;
	}
	
	cout << i << endl;
	if (i <= 50){
		cout << "GOOD";
	}
	else{
		cout << "OH MY GOD";
	}
	return 0;
}
