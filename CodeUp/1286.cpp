#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <cmath>
using namespace std;

int main(){
	int num;
	vector<int> list;
	
	for (int i=0; i< 5; i++){
		cin >> num;
		list.push_back(num);
	}
	cout << *max_element(list.begin(), list.end()) << endl << *min_element(list.begin(), list.end());
	return 0;
}
