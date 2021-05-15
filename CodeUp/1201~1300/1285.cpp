#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <cmath>
#include <cctype>
using namespace std;

int main(){
	string str;
	cin >> str;
	
	int value, back = 0;
	vector<int> list;
	
	for (int i=0; i< str.length(); i++){
		if (isdigit(str[i]) == false){
			value = stoi(str.substr(back, i-back));
			list.push_back(value);
			list.push_back(str[i]);
			back = i+1;
		}
	}
	
	int sum = list[0];
	char calc;
	for (int i=1; i <list.size()-1; i++){
		if (i%2==0){
			switch (calc){
				case '+':
					sum += list[i];
					break;
				case '-':
					sum -= list[i];
					break;
				case '*':
					sum *= list[i];
					break;
				case '/':
					sum /= list[i];
					break;
			}
		}
		else {
			calc = list[i];
		}
	}
	
	cout << sum;
	return 0;
}
