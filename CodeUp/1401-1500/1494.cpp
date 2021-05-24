#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <cmath>
using namespace std;

int main(){
	int n,k;
	scanf("%d %d", &n, &k);
	int list[n+1] ={0}, list2[n+1] = {0};
	int q,w,e;
	
	for (int i=1; i<=k; i++){
		scanf("%d %d %d", &q,&w,&e);
		list[q] += e;
		list[w+1] -= e;
	}
	
	for (int i=1; i<=n; i++){
		if (i == 1){
			list2[i] += list[i];
		}
		else{
			list2[i] = list2[i-1] + list[i];
		}
	}
	
	for (int i=1; i<=n;i++){
		printf("%d ", list[i]);
	}
	
	cout << endl;
	
	for (int i=1; i<=n;i++){
		printf("%d ", list2[i]);
	}
	
	return 0;
}
