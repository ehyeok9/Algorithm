#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <cmath>
using namespace std;

int main(){
	int list[12][11];
	
	for (int i =1; i<=11; i++){
		for (int j=1; i<=10; i++){
			scanf("%d", &list[i][j]);
		}
	}
	
	for (int i=1; i<=10; i++){
		bool safe = true;		
		if (list[11][i] == 1){
			for (int j=10; j>=1; j--){
				if (list[j][i] < 0){
					safe = false;
					printf("%d fall\n", i);
					break;
				}

				if (list[j][i] > 0){
					safe = false;
					printf("%d crash\n", i);
					break;
				}
			}
			if (safe == true){
				printf("%d safe\n", i);
			}
		}
	}
	return 0;
}
