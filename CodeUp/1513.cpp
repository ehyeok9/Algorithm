#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <cmath>
using namespace std;

int main(){
	int n, a= 1;
	scanf("%d", &n);
	int list[n+1][n+1] = {0};
	int x = n, y= 1; 
	bool flag = true;
	
	for (int i=(2*n-1)/2+1; i >= 1; i--){
		for (int j=1; j <=i; j++){
			list[x][y] = a++; 
			if (flag && j != i){
				x--;
				y++;
			}
			else if (!flag && j != i){
				x++;
				y--;
			}
		}
		flag = !flag;
		if (x == n){
			y++;
		}
		else if (y == n){
			x++;
		}
	}
	
	for (int i=1; i <= n; i++){
		for (int j=1; j <= n; j++){
			printf("%d ", list[i][j]);
		}
		cout << endl;
	}
	return 0;
}

