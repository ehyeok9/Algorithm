#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
using namespace std;

int main(){
	string str;
	cin >> str;
	vector<int> list;
	
	for (int i=0; i < str.length(); i++){
		if (str[i] == 't'){
			list.push_back(i);
		}
	}
	
	for (int i=0; i < list.size(); i++){
		cout << list[i] + 1 << ' ';
	}
	
	return 0;
}