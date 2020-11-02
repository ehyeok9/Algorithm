#include <iostream>
#include <cmath>
using namespace std;

int main(){
	double const pi = 3.141592;
	
	double r, a, v;
	cout << "반지름을 입력하시오: ";
	cin >> r;
	
	a = 4*pi*pow(r,2);
	v = 4/3*pi*pow(r,3);
	
	cout << "표면적은 " << a << " 체적은 " << v << endl;
	
	return 0;
}