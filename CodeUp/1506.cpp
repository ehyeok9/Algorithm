#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <cmath>
using namespace std;

int main(){
	int n, a=1;
	scanf("%d", &n);
	int list[n+1][n+1];
	bool flag = true;
	int sequence = n, x = 0, y =1;
	
	for (int i=1; i<=2*n+1; i++){
		if (flag && i%2 ==1){
			for (int j = 1; j <= sequence; j++){
				x++;
				list[x][y] = a++;
			}
			sequence--;
		}
		else if (flag && i%2 ==0){
			for (int j = 1; j <= sequence; j++){
				y++;
				list[x][y] = a++;
			}
		}
		else if (!flag && i%2 ==1){
			for (int j = 1; j <= sequence; j++){
				x--;
				list[x][y] = a++;
			}
			sequence--;
		}
		else if (!flag && i%2 ==0){
			for (int j = 1; j <= sequence; j++){
				y--;
				list[x][y] = a++;
			}
		}
		
		if (i%2 ==0){
			if (flag){
				flag = false;
			}
			else{
				flag = true;
			}
		}
	}
	
	for (int i=1; i <= n; i++){
		for (int j=1; j <= n; j++){
			printf("%d ", list[i][j]);
		}
		printf("\n");
	}
	return 0;
}
