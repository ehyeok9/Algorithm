#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <cmath>
using namespace std;

int main(){
	int n, a= 1;
	scanf("%d", &n);
	int list[n+1][n+1];
	
	for (int i=1; i <= n; i++){
		if (i%2 == 0){
			for (int j=n; j >= 1; j--){
				list[i][j] = a;
				a++;
			}
		}
		else{
			for (int j=1; j <= n; j++){
				list[i][j] = a;
				a++;
			}
		}
	}
	
	for (int i=1; i <= n; i++){
		for (int j=1; j <= n; j++){
			printf("%d ", list[i][j]);
		}
		cout << endl;
	}
	return 0;
}
