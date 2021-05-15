#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <cmath>
using namespace std;

int main(){
	int n;
	cin >> n;
	
	for (int i = 1; i <= pow(n,2);i++){
		cout << i << ' ';
		if (i%n == 0){
			cout << endl;
		}
	}
	return 0;
}
