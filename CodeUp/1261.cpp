#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
using namespace std;

int main(){
	vector<int> num;
	int n;
	
	for (int i=0; i< 10; i++){
		cin >> n;
		if (n%5 ==0){
			num.push_back(n);
		}
	}
	
	if (num.size() == 0){
		cout << 0;
	}
	else{
		cout << num[0];
	}
	return 0;
}