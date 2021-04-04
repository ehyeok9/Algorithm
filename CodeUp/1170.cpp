#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <cmath>
using namespace std;

int main(){
	string a,b,c;
	cin >> a >> b >> c;
	string str = a+ b + c;
	
	if (str.length() == 3){
		str = a + b + "0" +c;
	}
	
	cout << str;
	return 0;
}
