#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <cmath>
using namespace std;

int main(){
	int n,m,a;
	scanf("%d %d", &n, &m);
	int list[n][n];
	
	for (int i=0; i<n; i++){
		for(int j=0; j<n; j++){
			scanf("%d", &a);
			list[i][j] = a;
		}
	}
	
	int cnt = 0;
	for (int i=0; i<n; i++){
		for(int j=0; j<n; j++){
			if (list[i][j] == -1){
				continue;
			}
			else{
				if ((list[i][j] + m) >= 0 && (list[i][j] + m) <=5){
					cnt++;
				}
			}
		}
	}
	
	printf("%d", cnt);
	return 0;
}
