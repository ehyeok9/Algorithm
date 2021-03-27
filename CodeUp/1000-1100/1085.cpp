#include <iostream>
using namespace std;

int main(){
	double h, b, c, s;
	cin >> h >> b >> c >> s;
	
	double value = (((h*b*c*s)/8)/1024)/1024;
	printf("%.1lf MB", value);
	return 0;
}