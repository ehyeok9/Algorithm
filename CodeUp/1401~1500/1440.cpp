#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <cmath>
using namespace std;

int main(){
	int n, a;
	cin >> n;
	vector<int> list;
	
	for (int i=0; i < n; i++){
		scanf("%d", &a);
		list.push_back(a);
	}
	
	string str;
	
	for (int j=0; j < list.size(); j++){
		str = to_string(j+1) + ": ";
		for (int i=0; i < list.size(); i++){
			
			if (i == j){
				continue;
			}
			
			if (list[j] > list[i]){
				str += "> ";
			}
			else if (list[j] < list[i]){
				str += "< ";
			}
			else{
				str += "= ";
			}
		}
		cout << str << endl;
	}
	return 0;
}
