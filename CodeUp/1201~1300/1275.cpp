#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <cmath>
using namespace std;

int main(){
	int n,k;
	cin >> n >> k;
	int total = 1;
	
	for (int i=0; i <k;i++){
		total *= n;
	}
	
	cout << total;
	return 0;
}