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
	int x = 1, y = 1;
	int a =1, x_cnt = 1, y_cnt = 1;
	
	for (int i=1; i <= n+m-1; i++){
		for (int j=1; j <= n; j++){
			int q = i-j;
			if (q >= 0 && q < m){
				list[j][q] = a;
				a++;
			}
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
