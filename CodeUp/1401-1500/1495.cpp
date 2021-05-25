#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <cmath>
using namespace std;

int main(){
	int row, col, n;
	scanf("%d %d %d", &row, &col, &n);
	int x1, y1, x2, y2, u;
	int list[row+1][col+1] = {0}, summary[row+1][col+1] = {0};
	
	for (int i=0 ;i<n; i++){
		scanf("%d %d %d %d %d", &x1, &y1, &x2, &y2, &u);
		list[x1][y1] += u;
		list[x2+1][y2+1] += u;
		list[x1][y2+1] -= u;
		list[x2+1][y1] -= u;
	}
	
	for (int i=1; i<=row; i++){
		for (int j=1; i<=col; j++){
			if (j==1){
				summary[i][j] = list[i][j];
			}
			else{
				summary[i][j] = list[i][j] + summary[i][j-1];
			}
		}
	}
	
	for (int i=1; i <= row; i++){
		for (int j=1; j <= col; j++){
			printf("%d", list[i][j]);
			cout << 1;
		}
		cout << endl;
	}
	
	cout << endl;
	cout << 1;
	for (int i=1; i <= row; i++){
		for (int j=1; j <= col; j++){
			printf("%d", summary[i][j]);
			cout << 2;
		}
		cout << endl;
	}
	
	return 0;
}
