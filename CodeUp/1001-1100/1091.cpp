#include <iostream>
using namespace std;

int main(){
	int a, m, d, n;
	cin >> a >> m >> d >>n;
	long long int result = a;
	
	for (int i=0; i <n-1; i++){
		result = result*m+d;
	}
	
	cout << result;
	return 0;
}