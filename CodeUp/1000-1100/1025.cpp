#include <iostream>
#include <vector>
#include <string>
using namespace std;

int main(){
	
	vector<int> vec;
	
	string a;
	
	cin >> a;
	
	int q = 1;
	
	for (int i= a.size()-1; i > -1; i--){
		int u = a[i] - '0';
		vec.push_back(u * q);
		q *= 10;		
	}
	
	for (int i = vec.size()-1; i > -1; i--){
		cout << "[" << vec[i] << "]"<< endl;
	}
	return 0;
}