#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <cmath>
using namespace std;

int main(){
	string str;
	getline(cin, str);
	
	for (int i =0; i < str.length(); i++){
		if (str[i] == ' '){
			continue;
		}
		if (str[i] - 3 < 97){
			str[i] = str[i] -3 + 26;
		}
		else{
			str[i] -=3;
		}
	}
	cout << str;
	return 0;
}
