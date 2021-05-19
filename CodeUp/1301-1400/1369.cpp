#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <cmath>
using namespace std;

int main(){
	int n,k;
	cin >> n >> k;
	
	char list[n*2+1][n*2+1];
	
	for (int i=1; i< n*2+1; i++){
		for (int j=1; j < n*2+1; j++){
			list[i][j] = ' ';
		}
	}
	
	for (int i=1; i < n+1; i++){
		list[1][i] = '*';
		list[n][i] = '*';
		list[i][1] = '*';
		list[i][n] = '*';
	}
	
	vector<int> num;
	int pp =k;
	while(true){
		if (pp > n*2){
			break;
		}
		num.push_back(pp);
		pp += k;
	}
	
	for (int i=1; i <= num.size(); i++){
		int u = n; 
		for (int j=1; j <= num[i-1]; j++){
			list[j][num[i-1]-j+1] = '*';
		}
	}
	
	
	for (int i = 1; i < n+1; i++){
		for (int j=1; j < n+1; j++){
			cout << list[i][j];
		}
		cout << endl;
	}
	return 0;
}

