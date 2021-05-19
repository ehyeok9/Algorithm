#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <cmath>
using namespace std;

int main(){
	int begin, end;
	cin >> begin >> end;
	
	for (int i=begin ; i <=end; i++){
		for (int j=1; j <=9 ;j++){
			printf("%d*%d=%d\n", i, j, i*j);
		}
	}
	
	return 0;
}

