#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
using namespace std;

int main(){
	vector<int> list;
	int n;
	cin >>n;
	
	for (int i=1; i <= n; i++){
		if(n%i==0){
			list.push_back(i);
		}
	}
	
	for (int i=0; i < list.size(); i++){
		cout << list[i] << ' ';
	}
	return 0;
}