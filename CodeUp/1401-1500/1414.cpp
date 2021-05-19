#include <iostream>
#include <string>
#include <algorithm>
using namespace std;

int main(){
	string str;
	cin >> str;
	int c =0, cc =0;
	
	for (int i=0; i < str.length(); i++){
		if (str[i] >= 97 && str[i] <= 122){
			str[i] -= 32;
		}
		if (str[i] == 'C'){
			c += 1;
		}
	}
	
	for (int i=0; i < str.length()-1; i++){
		if (str[i] == 'C' && str[i+1] == 'C'){
			cc += 1;
		}
	}
	cout << c << endl << cc;
	return 0;
}