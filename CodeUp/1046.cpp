#include <iostream>
using namespace std;

int main(){
	
	long a, b, c;
	
	scanf("%ld %ld %ld", &a, &b, &c);
	
	printf("%ld\n%.1lf", a+b+c, (a+b+c)/3.0);
	
	return 0;
}