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
	
	for (int i = 2; i <= n+m; i++){
		for (int j=1; j <=n; j++){
			for (int k=1; k <= m; k++){
				if (j+k == i){
					list[j][k] = a++;
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
