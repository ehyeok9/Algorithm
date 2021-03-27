#include <iostream>
using namespace std;

int main(){
	
	int a, b, c;
	
	scanf("%04d.%02d.%02d", &a, &b, &c);
	
	printf("%02d-%02d-%04d", c, b, a);
	
	return 0;
}