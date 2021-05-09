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
	int a =1;
	
	for (int i=1; i <= n*2; i++){
		if (i > n){
			x = n;
			y = i - n +1;
			for (int j = n*2; j >= i; j--){
				list[x][y] = a;
				a++;
				x--;
				y++;
			}
		}
		else{
			x = i;
			y = 1;
			for (int j = 1; j <= i; j++){
				list[x][y] = a;
				a++;
				x--;
				y++;
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
