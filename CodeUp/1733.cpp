#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
using namespace std;

int main(){
	string str;
	cin >> str;
	
	if (str.compare("IOI") == 0){
		cout << "IOI is the International Olympiad in Informatics.";
	}
	else{
		cout << "I don't care.";
	}
	return 0;
}