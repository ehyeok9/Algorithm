#include <iostream>
using namespace std;

int main(){
	double a,b,c,d;
	cout << "ac, ae, bc 순으로 입력하시오: ";
	cin >> a >> b >> c;
	
	d = (b*c)/a;
	cout << "de는 " << d << endl ;
	return 0;
}