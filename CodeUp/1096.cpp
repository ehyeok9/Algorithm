#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main(){
	
	int baduk[20][20] = {};
	int n, x, y;
	cin >> n;
	
	for (int i=0; i < n; i++){
		cin >> x >> y;
		baduk[x][y] = 1;
	}
	
	for (int i =1; i < 20 ; i++){
		for (int j =1; j < 20; j++){
			cout << baduk[i][j] << ' ';
		}
		cout << endl;
	}
	return 0;
}