#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <cmath>
#include <stack>
using namespace std;

int main(){
	int n;
	scanf("%d", &n);
	string str;
	cin >> str;
	vector<char> list;
	
	for (int i = 0; i < str.length(); i++){
		list.push_back(str[i]);
	}
	
	int cnt = 1;
	string result = "";
	
	for (int i=list.size()-1; i > -1; i--){
		if (cnt == 3 && i != 0){
			result += list[i];
			result += ',';
			cnt = 1;
		}
		else if (cnt == 3 && i == 0){
			result += list[i];
		}
		else{
			result += list[i];
			cnt ++;
		}
	}
	
	for (int i = result.length()-1; i >-1; i--){
		printf("%c", result[i]);
	}
	
	return 0;
}
