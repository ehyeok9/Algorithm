#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
using namespace std;

int main(){
	string str1, str2, str3;
	cin >> str1 >> str2 >> str3;
	
	if ((str1.back() == str2.front()) && (str2.back() == str3.front()) && (str3.back() == str1.front())){
		cout << "good";
	}
	else{
		cout << "bad";
	}
	return 0;
}