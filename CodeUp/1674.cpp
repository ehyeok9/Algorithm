#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <cmath>
using namespace std;

int main(){
	string str;
	cin >> str;
	
	int sum = 0, a;
	
	for (int i=0; i < str.length(); i++){
		a = str[i] - '0';
		sum += a;
	}
	
	if (sum%7 == 4){
		cout << "Bad";
	}
	else{
		cout << "Good";
	}
	return 0;
}
