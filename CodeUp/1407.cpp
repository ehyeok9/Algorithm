#include <iostream>
#include <string>
#include <algorithm>
using namespace std;

int main(){
	string c;
	getline(cin, c);
	
	int blank = count(c.begin(), c.end(), ' ');
	remove(c.begin(), c.end(), ' ');
	c = c.substr(0, c.length() - blank);
	cout << c;
	return 0;
}