#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <cmath>
using namespace std;

int main(){
	int list[3];
	
	for (int i=0; i<3; i++){
		int a,b;
		scanf("%d %d", &a, &b);
		list[i] = a*b;
	}
	int max = -1;
	for (int i=0; i<3; i++){
		if (list[i] > max){
			max = list[i];
		}
	}
	cout << max;
	return 0;
}
