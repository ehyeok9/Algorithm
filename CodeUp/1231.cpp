#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <cmath>
using namespace std;

int main(){
	string str;
	getline(cin, str);
	char c;
	int a,b;
	
	for (int i=0; i < str.length(); i++){
		if (str[i] < 48){
			c = str[i];
			a = stoi(str.substr(0,i));
			b = stoi(str.substr(i+1, str.length()));
			break;
		}
	}
	
	if (c == '+'){
		cout << a+b;
	}
	else if (c == '-'){
		cout << a-b;
	}
	else if (c == '*'){
		cout << a*b;
	}
	else{
		printf("%.2lf", a/(double)b);
	}
	
	return 0;
}

