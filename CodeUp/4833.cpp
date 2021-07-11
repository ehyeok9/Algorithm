#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <stack>
using namespace std;

int main(){
	stack<char> box;
	char prev = '.';
	string str;
	cin >> str;
	int result = 0;
	
	for (int i=0; i<str.length(); i++){
		if (str[i] == '('){
			box.push(str[i]);
			prev = '(';
		}
		else if (prev == '(' && str[i] == ')'){
			box.pop();
			result += box.size();
			prev = ')';
		}
		else if (str[i] == ')'){
			box.pop();
			result += 1;
			prev = ')';
		}	
	}
	
	cout << result;
	return 0;
}
