#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <cmath>
using namespace std;

int main(){
	int n, x, y;
	scanf("%d", &n);
	scanf("%d %d", &x, &y);
	int list[101][101];
	list[x][y] = 1;
	
	for (int i=2; i <= 200; i++){
		
		int x_1 = -i+1, y_1 =0, x_2 = -i+1, y_2 =0, x_3 = i-1, y_3=0, x_4= i-1, y_4 =0;
		
		for(int j=i; j>=1; j--){
			if (x+x_1 < 1 || y+y_1 < 1 || x+x_1 > 100 || y+y_1 > 100){
				x_1++;
				y_1--;
			}
			else{
				list[x+x_1][y+y_1] = i;
				x_1++;
				y_1--;
			}
			if (x+x_2 < 1 || y+y_2 < 1 || x+x_2 > 100 || y+y_2 > 100){
				x_2++;
				y_2++;
			}
			else{	
				list[x+x_2][y+y_2] = i;
				x_2++;
				y_2++;
			}
			if (x+x_3 < 1 || y+y_3 < 1 || x+x_3 > 100 || y+y_3 > 100){
				x_3--;
				y_3--;
			}
			else{	
				list[x+x_3][y+y_3] = i;
				x_3--;
				y_3--;
			}
			if (x+x_4 < 1 || y+y_4 < 1 || x+x_4 > 100 || y+y_4 > 100){
				x_4--;
				y_4++;
			}
			else{	
				list[x+x_4][y+y_4] = i;
				x_4--;
				y_4++;
			}
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
