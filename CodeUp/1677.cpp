#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <cmath>
using namespace std;

int main(){
	int n,m;
	cin >> n >> m;
	char list[m+1][n+1];
	
	for (int i=1; i<=m; i++){
		for (int j=1; j<=n; j++){
			list[i][j] = ' ';
		}
	}
	list[1][1] = '+';
	list[1][n] = '+';
	list[m][1] = '+';
	list[m][n] = '+';
	
	for (int i=2; i <= n-1; i++){
		list[1][i] = '-';
		list[m][i] = '-';
	}
	
	for (int i=2; i <= m-1; i++){
		list[i][1] = '|';
		list[i][n] = '|';
	}
	
	for (int i=1; i<=m; i++){
		for (int j=1; j<=n; j++){
			cout << list[i][j];
		}
		cout << endl;
	}
	return 0;
}

