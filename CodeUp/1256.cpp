#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
using namespace std;

int main(){
	int n;
	cin >> n;
	string s = "";
	
	for (int i=0; i<n; i++){
		s.push_back('*');
	}
	cout << s;
	return 0;
}