#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <cmath>
#include <stack>
using namespace std;

int main(){
	string str;
	getline(cin, str);
	stack<char> equation;
	int result, a,b;
	
	for (int i = 0; i <= str.length() -2; i += 2){
		if (str[i] == '*'){
			a = equation.top();
			equation.pop();
			b = equation.top();
			equation.pop();
			equation.push(b*a);
		}
		else if (str[i] == '/'){
				a = equation.top();
				equation.pop();
				b = equation.top();
				equation.pop();
				equation.push(b/a);
		}
		else if (str[i] == '-'){
			a = equation.top();
			equation.pop();
			b = equation.top();
			equation.pop();
			equation.push(b-a);
		}
		else if (str[i] == '+'){
			a = equation.top();
			equation.pop();
			b = equation.top();
			equation.pop();
			equation.push(b+a);
		}	
		else{
			result = str[i] - '0';
			equation.push(result);
		}
	}
	
	cout << equation.top();
	return 0;
}
