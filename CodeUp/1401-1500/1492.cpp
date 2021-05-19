#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <cmath>
using namespace std;

int main(){
	int n,a;
	scanf("%d", &n);
	
	int list[n+1];
	for (int i=1; i <= n; i++){
		scanf("%d", &a);
		list[i]= a;
	}
	
	int result[n+1];
	
	for (int i=1; i<=n ;i++){
		if (i == 1){
			result[i] = list[i];
			continue;
		}
		result[i] = list[i] + result[i-1];
	}
	
	for (int i=1; i<= n; i++){
		printf("%d ", result[i]);
	}
	
	return 0;
}
