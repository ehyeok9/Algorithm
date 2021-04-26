#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <cmath>
using namespace std;

int main(){
	int num;
	cin >> num;
	string str;
	for (int i=1; i <= num; i++){
		str = "";
		for (int j=0; j < i-1; j++){
			str += " ";
		}
		str += "**";
		cout << str << endl;
	}
	return 0;
}

