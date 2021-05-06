#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <cmath>
using namespace std;

int main(){
	int n, m;
	cin >> n >> m;
	int list[n+1][m+1];
	int a = 1;
	
	for (int i =n; i >= 1; i--){
		for (int j = m; j >= 1; j--){
			list[i][j] = a;
			a ++;
		}
	}
	
	for (int i=1; i <= n;i++){
		for (int j=1; j <=m; j++){
			cout << list[i][j] << ' ';
		}
		cout << endl;
	}
	
	return 0;
}
