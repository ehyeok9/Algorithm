#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <cmath>
using namespace std;

int main(){
	int n, value = 0 ;
	cin >> n;
	
	while (n > 0){
		n /= 10;
		value += 1;
	}
	
	cout << value;
	return 0;
}