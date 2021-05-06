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
	int a = 1;
	
	for (int i =1; i <= n; i++){
		if (i%2 == 1){
			for (int j=1; j <=n; j++){
				list[i][j] = a;
				a++;
			}
		}
		else{
			for (int j=n; j >=1; j--){
				list[i][j] = a;
				a++;
			}
		}
	}
	
	for (int i=1; i <= n;i++){
		for (int j=1; j <=n; j++){
			cout << list[i][j] << ' ';
		}
		cout << endl;
	}
	
	return 0;
}
