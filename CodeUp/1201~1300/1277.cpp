#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <cmath>
using namespace std;

int main(){
	int n, temp;
	cin >> n;
	int value[n+1];
	
	for (int i = 1; i <=n; i++){
		cin >> temp;
		value[i] = temp;
	}
	
	printf("%d %d %d", value[1], value[(n+1)/2], value[n]);
	return 0;
}