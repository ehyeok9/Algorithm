#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <cmath>
using namespace std;

int main(){
	int n;
	scanf("%d", &n);
	int list[n+1];
	
	for (int i=1; i <= pow(n,2); i++){
		printf("%d ", i);
		if (i % n == 0){
			cout << endl;
		}
	}
	
	return 0;
}
