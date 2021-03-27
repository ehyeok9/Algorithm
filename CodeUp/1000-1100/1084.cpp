#include <iostream>
using namespace std;

int main(){
	
	int red, green, blue;
	scanf("%d %d %d", &red, &green, &blue);
	int sum = 0;
	
	for (int i=0 ; i < red ; i++){
		for (int j=0; j < green; j++){
			for (int k=0; k < blue ; k++){
				printf("%d %d %d\n", i, j, k);
				sum ++;
			}
		}
	}
	
	cout <<  sum;
	return 0;
}