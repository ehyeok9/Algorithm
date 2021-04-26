#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <cmath>
using namespace std;

int main(){
	int value;
	cin >> value;
	
	vector< vector<char>> list;
	vector<char> floor;
	int space; 
	
	for (int i=1; i<=value; i++){
		space = value -i;
		floor.clear();
		for (int j=1; j <=space; j++){
			floor.push_back(' ');
		}
		for (int j=0; j<value; j++){
			floor.push_back('*');
		}
		list.push_back(floor);
	}
	
	for (int i=0; i <value; i++){
		for (int j=0; j < list[i].size(); j++){
			cout << list[i][j];
		}
		cout << endl;
	}
	return 0;
}

