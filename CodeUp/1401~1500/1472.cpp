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
	int a = 1, t = 0;
	
	for (int i =n; i >= 1; i--){
		if (t%2 == 0){
			for (int j=m; j >= 1; j--){
				list[i][j] = a;
				a++;
			}
		}
		else{
			for (int j=1; j <= m; j++){
				list[i][j] = a;
				a++;
			}
		}
		t++;
	}
	
	for (int i=1; i <= n;i++){
		for (int j=1; j <=m; j++){
			cout << list[i][j] << ' ';
		}
		cout << endl;
	}
	
	return 0;
}
