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
	
	vector<string> word;
	word.clear();
	int previous =0, current=0;
	current = str.find(' ');
	
	while (current != string::npos){
		string sub = str.substr(previous, current-previous);
		word.push_back(sub);
		previous = current+1;
		current = str.find(' ', previous);
	}
	word.push_back(str.substr(previous, current-previous));

	stack<string> equation;
	int a,b;
	for (int i=0; i < word.size()-1; i++){
		if (word[i] == "*"){
			a = stoi(equation.top());
			equation.pop();
			b = stoi(equation.top());
			equation.pop();
			equation.push(to_string(b*a));
		}
		else if (word[i] == "-"){
			a = stoi(equation.top());
			equation.pop();
			b = stoi(equation.top());
			equation.pop();
			equation.push(to_string(b-a));
		}
		else if (word[i] == "+"){
			a = stoi(equation.top());
			equation.pop();
			b = stoi(equation.top());
			equation.pop();
			equation.push(to_string(b+a));
		}
		else{
			equation.push(word[i]);
		}
	}
	
	int answer = stoi(equation.top());
	
	cout << answer;
	return 0;
}
