#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <cmath>
using namespace std;

int main(){
	int n;
	cin >> n;
	int list[n+1][n+1];
	
	for (int i =1; i <= n; i++){
		for (int j = n; j >= 1; j--){
			cout << (n*i)-(n-j) << ' ';
		}
		cout << endl;
	}
	
	return 0;
}
