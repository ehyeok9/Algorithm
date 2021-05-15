#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <cmath>
using namespace std;

int main(){
	int n;
	cin >> n;
	string str = "";
	
	while (n >0){
		if (n%2 == 0){
			str += "0";
		}
		else{
			str += "1";
		}
		n /= 2;
	}
	if (str == ""){
		cout << "0";
	}
	for (int i= str.length()-1; i > -1; i--){
		cout << str[i];
	}
	
	return 0;
}

