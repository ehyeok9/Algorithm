#include <iostream>
#include <string>
#include <algorithm>
using namespace std;

int main(){
	string str;
	cin >> str;
	
	int a,b;
	a = count(str.begin(), str.end(), '(');
	b = count(str.begin(), str.end(), ')');
	
	cout << a << ' ' << b;
	return 0;
}