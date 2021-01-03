#include <iostream>
using namespace std;

int main(){
	
	long a, b;
	
	scanf("%ld %ld", &a, &b);
	
	printf("%ld\n%ld\n%ld\n%ld\n%ld\n%.2lf\n", a+b, a-b, a*b, a/b, a%b, a/(double)b);
	
	return 0;
}