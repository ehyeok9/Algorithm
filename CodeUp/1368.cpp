#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <cmath>
using namespace std;

int main(){
	int h,k;
	char l;
	cin >> h >> k >> l;
	
	vector< vector<char>> list;
	vector<char> floor;
	int space; 
	
	if (l == 'R'){
		for (int i=1; i<=h; i++){
			space = h - i;
			floor.clear();
			for (int j=1; j <=space; j++){
				floor.push_back(' ');
			}
			for (int j=0; j<k; j++){
				floor.push_back('*');
			}
			list.push_back(floor);
		}
	}
	else {
		for (int i=h; i>=1; i--){
			space = h - i;
			floor.clear();
			for (int j=1; j <=space; j++){
				floor.push_back(' ');
			}
			for (int j=0; j<k; j++){
				floor.push_back('*');
			}
			list.push_back(floor);
		}
	}
	
	
	for (int i=0; i <h; i++){
		for (int j=0; j < list[i].size(); j++){
			cout << list[i][j];
		}
		cout << endl;
	}
	return 0;
}

