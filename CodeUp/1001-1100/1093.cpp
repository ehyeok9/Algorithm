#include <iostream>
using namespace std;

int main(){
	int fri[24] = {};
	int n, j;
	cin >> n;
	
	for (int i=0; i <n; i++){
		cin >> j;
		fri[j] += 1;
	}
	
	for (int i=1; i < 24; i++){
		cout << fri[i] << ' ';
	}
	
	return 0;
}