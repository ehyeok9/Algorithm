#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <cmath>
using namespace std;

int main(){
	int a;
	int square[4][4];
	
	for(int i=0; i < 4; i++){
		for(int j=0; j < 4; j++){
			scanf("%d", &a);
			square[i][j] = a;
		}
	}
	
	int cordinate[101][101] = {0};
	
	for (int i=0; i <4; i++){
		for (int j = 0; j <= square[i][3] - square[i][1]; j++){
			for (int k=0; k <= square[i][2] - square[i][0]; k++){
				cordinate[square[i][0] + k][square[i][1] + j] += 1;
			}
		}
	}
	
	int sum ;
	
	for(int i=0; i < 4; i++){
		sum += (square[i][2] - square[i][0]) * (square[i][3] - square[i][1]);
	}
	
	int sum_2 =0, sum_3 = 0, sum_4=0;
	for (int i=0; i <= 100; i++){
		for (int j=0; j <= 100; j++){
			if (cordinate[i][j] == 2 || cordinate[i-1][j-1] ==2 || cordinate[i-1][j+1] ==2 || cordinate[i+1][j-1] ==2 || cordinate[i+1][j+1] ==2){
				sum_2 += 1;
			}
			else if (cordinate[i][j] == 3 || cordinate[i-1][j-1] ==3 || cordinate[i-1][j+1] ==3 || cordinate[i+1][j-1] ==3 || cordinate[i+1][j+1] ==3){
				sum_3 += 1;				
			}
			else if (cordinate[i][j] == 4 || cordinate[i-1][j-1] ==4 || cordinate[i-1][j+1] ==4 || cordinate[i+1][j-1] ==4 || cordinate[i+1][j+1] ==4){
				sum_4 += 1;
			}
		}
	}
	if (sum_2 != 0){
		sum -= (sqrt(sum_2)-1);
	}
	if (sum_3 != 0){
		sum -= (sqrt(sum_3)-1);
	}
	
	if (sum_4 != 0){
		sum -= (sqrt(sum_4)-1);
	}
	
	cout << sum;
	
	return 0;
}
