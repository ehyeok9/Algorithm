#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <cmath>
#include <map>
using namespace std;

int main(){
	int n;
	scanf ("%d", &n);
	string type, str;
	int id;
	map<int, string> dic;
	
	for (int i=0; i<n; i++){
		cin >> type >> id >> str;
		if (type == "I"){
			if (dic.find(id) == dic.end()){
				dic[id] = str;
			}
			else{
				continue;
			}
		}
		else if (type == "D"){
			if (dic.find(id) == dic.end()){
				continue;
			}
			else{
				dic.erase(id);
			}
		}
	}
	
	vector<int> list;
	int a;
	for (int i=0; i<5; i++){
		scanf("%d", &a);
		list.push_back(a);
	}
	
	int cnt = 1;
	for (map<int, string>::iterator itr = dic.begin(); itr != dic.end(); ++itr){
		for (int i=0; i< list.size(); i++){
			if (cnt == list[i]){
				cout << itr->first << " " << itr->second << endl;
				continue;
			}
		}
		cnt++;
	}
	
	return 0;
}

