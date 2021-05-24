#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <cmath>
using namespace std;

int main(){
	int n, m, a=1;
	scanf("%d %d", &n, &m);
	int list[n+1][m+1];
	bool flag = true;
	int sequence_row = m, sequence_colum = n-1, x = 1, y =0;
	int time;
	
	if (n == m){
		time = 2*n+1;
	}
	else{
		time = n+m-2;
	}
	
	for(int i=1; i<= time; i++){
		if (flag && i%2 ==1){
			for (int j = 1; j <= sequence_row; j++){
				y++;
				list[x][y] = a++;
			}
			sequence_row--;
		}
		else if (flag && i%2 ==0){
			for (int j = 1; j <= sequence_colum; j++){
				x++;
				list[x][y] = a++;
			}
			sequence_colum--;
		}
		else if (!flag && i%2 ==1){
			for (int j = 1; j <= sequence_row; j++){
				y--;
				list[x][y] = a++;
			}
			sequence_row--;
		}
		else if (!flag && i%2 ==0){
			for (int j = 1; j <= sequence_colum; j++){
				x--;
				list[x][y] = a++;
			}
			sequence_colum--;
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
		for (int j=1; j <= m; j++){
			printf("%d ", list[i][j]);
		}
		printf("\n");
	}
	return 0;
}

