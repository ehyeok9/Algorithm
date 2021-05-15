#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <cmath>
using namespace std;

int main(){
	int n, m;
	scanf("%d %d", &n, &m);
	int a = 1;
	int list[n+1][m+1];
	
	for (int i = n+m; i >= 2; i--){
		for (int j=m; j >=1; j--){
			for (int k=1; k <= n; k++){
				if (j+k == i){
					list[k][j] = a++;
					break;
				}
			}
		}
	}
	
	for (int i=1; i <=n; i++){
		for (int j=1; j <=m; j++){
			printf("%d ", list[i][j]);
		}
		cout << endl;
	}
	return 0;
}
