#include <iostream>
using namespace std;

int main(){
	
	int a;
	
	cin >> a;
	
	if ((a>=80) && (a<=100)){
		printf("A");
	}
	else if (a >= 70){
		printf("B");
	}
	else if (a >= 40){
		printf("C");
	}
	else if (a >= 0){
		printf("D");
	}
	
	return 0;
}

