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
	stack<int> round;
	bool result = true;
	
	for (int i=0; i<str.length(); i++){
		if (str[i] == '('){
			round.push('(');
		}
		else if (str[i] == ')' && !round.empty()){
			round.pop();
		}
		else{
			result = false;
			break;
		}
	}
	
	if (result && round.empty()){
		cout << "good";
	}
	else{
		cout << "bad";
	}
	
	return 0;
}

