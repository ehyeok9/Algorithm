#include <iostream>
#include <cmath>
using namespace std;

int main(){
	long long int start, d, n, result;
	cin >> start >> d >> n;
	result = start;
	
	for (int i=1; i < n; i++){
		result *= d;
	}
	
	cout << result;
	return 0;
}