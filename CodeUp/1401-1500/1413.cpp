#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <cmath>
using namespace std;

int main(){
	string str;
	getline(cin, str);
	
	for (int i = str.length()-1; i >= 0; i--){
		printf("%c", str[i]);
	}
	
	return 0;
}
