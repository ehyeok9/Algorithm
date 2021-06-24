#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <cmath>
#include <map>
using namespace std;

int main(){
	int n,m, a;
	scanf("%d %d", &n, &m);
	map<string, int> dic;
	string str;
	
	for (int i=0; i<n; i++){
		cin >> str;
		scanf("%d", &a);
		if (dic.find(str) == dic.end()){
			dic[str] = a;
		}
		else{
			int temp = dic[str];
			dic.erase(str);
			dic.insert(make_pair(str, a+temp));
		}
	}
	
	for (int i=0; i<m; i++){
		cin >> str;
		if (dic.find(str) == dic.end()){
			printf("%d\n", 0);
		}
		else{
			printf("%d\n", dic[str]);
		}
	}
	return 0;
}

