#include <iostream>
using namespace std;

int main(){
	int height, width;
	cin >> height >> width;
	
	int pan[101][101];
	for (int i=1; i <= height; i++){
		for(int j=1; j <= width; j++){
			pan[i][j] = 0;
		}
	}
	
	int num, d, l, x, y;
	cin >> num;
	
	for (int i=0; i < num; i++){
		cin >> l >> d >> x >> y;
		
		if (d == 0){
			for(int j=0; j < l; j++){
				pan[x][y+j] = 1;
			}
		}
		else if (d == 1){
			for (int k=0; k < l; k++){
				pan[x+k][y] = 1;
			}
		}
	}
	
	for (int i=1; i <= height; i++){
		for(int j=1; j <= width; j++){
			cout << pan[i][j] << ' ';
		}
		cout << endl;
	}
	return 0;
}