#include <iostream>
#include <cmath>
using namespace std;

int main(){
	int start, d, n, result;
	cin >> start >> d >> n;
	result = start;
	
	for (int i=0; i < n-1; i++){
		result += d;
	}
	
	cout << result;
	return 0;
}