#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
using namespace std;

int main(){
	double a, b;
	cin >> a >> b;
	
	for (double i=a; i <=b; i += 0.01){
		printf("%.2lf ", i);
	}
	
	return 0;
}