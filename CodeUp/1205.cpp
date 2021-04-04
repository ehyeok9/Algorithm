#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <cmath>
using namespace std;

int main(){
	double a,b;
	cin >> a >> b;
	vector<double> list = {a+b, a-b, a*b, a/b, pow(a,b), pow(b,a)};
	printf("%.6lf",*max_element(list.begin(), list.end()));
	return 0;
}
