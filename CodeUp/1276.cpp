#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <cmath>
using namespace std;

int main(){
	int n, total;
	cin >> n;
	
	total = n;
	for (int i=n-1; i  >0; i--){
		total *= i;
	}
	
	cout << total;
	return 0;
}