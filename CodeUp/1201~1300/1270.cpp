#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
using namespace std;

int main(){
	int n, result = 0;
	cin >> n;
	
	for (int i=1; i<=n;i++){
		if (i%10 == 1){
			result += 1;
		}
	}
	
	cout << result;
	
	return 0;
}