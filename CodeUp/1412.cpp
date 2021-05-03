#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <cmath>
using namespace std;

int main(){
	string str;
	getline(cin, str);
	char list[200];
	char a = 'a', z = 'z';
	for (int i = a; i <=z; i++){
		list[i] = 0;
	}
	
	for (int i=0; i < str.length(); i++){
		if (str[i] >= a && str[i] <= z){
			list[str[i]] += 1;
		}
	}
	char q;
	for (int i = a; i <=z; i++){
		char q = i;
		printf("%c:%d\n", q, list[i]);
	}
	return 0;
}

