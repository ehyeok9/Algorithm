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
	int list[row][col] = {}, summary[row][col] = {};
	
	for (int i=1 ;i<=n; i++){
		scanf("%d %d %d %d %d", &x1, &y1, &x2, &y2, &u);
		list[x1][y1] = list[x1][y1] + u;
		list[x2+1][y2+1] = list[x2+1][y2+1] + u;
		
		list[x1][y2+1] = list[x1][y2+1] - u;
		list[x2+1][y1] = list[x2+1][y1] - u;
	}
	
	for (int i=0; i<row; i++){
		for (int j=0; j<col; j++){
			if (j==0){
				summary[i][j] = list[i][j];
				for (int k=0; k< i; k++){
					summary[i][j] += list[k][j];
				}
			}
			else{
				summary[i][j] = list[i][j] + summary[i][j-1];
				for (int k=0; k< i; k++){
					summary[i][j] += list[k][j];
				}
			}
		}
	}
	
	for (int i=0; i < row; i++){
		for (int j=0; j < col; j++){
			printf("%d ", list[i][j]);
		}
		cout << endl;
	}
	
	cout << endl;
	
	for (int i=0; i < row; i++){
		for (int j=0; j < col; j++){
			printf("%d ", summary[i][j]);
		}
		cout << endl;
	}
	
	return 0;
}
