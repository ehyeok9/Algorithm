#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <cmath>
using namespace std;

int main(){
	int n,c, a;
	cin >> n >> c;
	vector<int> list;
	
	for (int i= 0; i < n; i++){
		cin >> a;
		list.push_back(a);
	}
	sort(list.begin(), list.end());
	
	for (int i =0; i < list.size(); i++){
		cout << list[i] << ' ';
		if ((i+1)%c == 0){
			cout << endl;
		}
	}
	return 0;
}
