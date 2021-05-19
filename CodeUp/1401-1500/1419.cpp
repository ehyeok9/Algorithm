#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
using namespace std;

int main(){
	string str;
	getline(cin, str);
	int total=0, idx = 0, word;
	
	
	while (idx != -1){
		word = str.find("love", idx);
		if (word != -1){
			total += 1;
			idx = word + 4;
		}
		else{
			idx = -1;
		}
	}
	
	cout << total;
	return 0;
}