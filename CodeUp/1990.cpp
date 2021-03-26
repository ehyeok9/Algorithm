#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
using namespace std;

int main(){
	string str;
	cin >> str;
	int temp, total=0;
	
	for (int i=0; i < str.length(); i++){
		temp = str[i] - '0';
		total += temp;
	}
	
	if (total %3 ==0){
		cout << 1;
	}
	else{
		cout << 0;
	}
	return 0;
}