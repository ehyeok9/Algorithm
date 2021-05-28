#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <cmath>
using namespace std;

int main(){
	int n, g, a;
	scanf("%d %d", &n, &g);
	int list[n+1];
	
	for (int i=1; i <=n; i++){
		scanf("%d", &a);
		list[i] = a;
	}
	
	vector<int> result;
	int minimum;
	
	for (int i=1; i <=n; i++){
		if (i ==1){
			minimum = list[i];
		}
		if (g != 1){
			if (i == n){
				if (minimum > list[i]){
					result.push_back(minimum);
				}
				else{
					result.push_back(list[i]);
				}
			}
			else if (i % g == 0){
				if (minimum > list[i]){
					result.push_back(minimum);
				}
				else{
					result.push_back(list[i]);
				}
				if (i < n){
					minimum = list[i+1];
				}
			}
			else{
				if (minimum < list[i]){
					minimum = list[i];
				}
			}
		}
		else {
			result.push_back(list[i]);
		}
	}
	
	for (int i=0; i < result.size(); i++){
		printf("%d ", result[i]);
	}
	
	return 0;
}
