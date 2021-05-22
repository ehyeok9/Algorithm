#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <cmath>
using namespace std;

int main(){
	int n;
	scanf("%d", &n);
	int list[n+1][n+1];
	int x = 1, y = n/2 +1;
	
	for (int i=1; i <= pow(n,2); i++){
		list[x][y] = i;
		
		if (i %n == 0){
			x++;
			continue;
		}
		if (x == 1){
			x = n;
		}
		else{
			x -= 1;
		}
		if (y == n){
			y = 1;
		}
		else{
			y++;
		}
	}
	
	for (int i=1; i<=n; i++){
		for(int j=1; j<=n; j++){
			printf("%d ", list[i][j]);
		}
		printf("\n");
	}
	
	return 0;
}
