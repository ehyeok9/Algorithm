#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <cmath>
#include <stack>
using namespace std;

int main(){
	string str;
	cin >> str;
	char sex;
	int year;
	
	if (str[7] == '1'){
		sex = 'M';
		year = 1900;
	}
	else if (str[7] == '2'){
		sex = 'F';
		year = 1900;
	}
	else if (str[7] == '3'){
		sex = 'M';
		year = 2000;
	}
	else{
		sex = 'F';
		year == 2000;
	}
	
	year += (str[0] - '0')*10 + (str[1] - '0');
	string result = to_string(year) + "/" +str.substr(2,2) + "/" + str.substr(4,2) + " " + sex;
	cout << result;
	
	return 0;
}
