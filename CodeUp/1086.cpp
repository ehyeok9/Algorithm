#include <iostream>
using namespace std;

int main(){
	double w, h, b;
	cin >> w >> h >> b;
	
	double value = (((w*h*b)/8)/1024)/1024;
	printf("%.2lf MB", value);
	return 0;
}