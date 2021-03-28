#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
using namespace std;

int main(){
	int n, result = -1;
	cin >> n;
	int j;
		
	for (int i=0 ; i<n ; i++){
		cin >> j;
		if (j > result){
			result = j;
		}
	}
	
	cout << result;
	return 0;
}