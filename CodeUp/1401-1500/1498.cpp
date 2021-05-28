#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <cmath>
using namespace std;

int main(){
	int n, a;
	scanf("%d", &n);
	int list[n+1];
	
	for (int i=1; i <=n; i++){
		scanf("%d", &a);
		list[i] = a;
	}
	
	vector<int> result;
	
	for (int i=2; i <= n; i+=2){
		if (list[i] < list[i-1]){
			result.push_back(list[i-1]);
		}
		else{
			result.push_back(list[i]);
		}
	}
	
	for (int i=0; i < result.size(); i++){
		printf("%d ", result[i]);
	}
	
	return 0;
}

