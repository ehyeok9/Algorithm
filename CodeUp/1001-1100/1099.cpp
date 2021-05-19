#include <iostream>
using namespace std;

int main(){
	int matrix[11][11] = {};
	int val;
	
	for (int i=1; i <= 10; i++){
		for (int j=1; j <=10; j++){
			cin >> val;
			matrix[i][j] = val; 
		}
	}

	int x=2,y=2;
	while(true){
		if (x == 9 && y == 9){
			matrix[x][y] = 9;
			break;
		} 
		else if (matrix[x][y] == 2){
			matrix[x][y] = 9;
			break;
		}
		else if (matrix[x][y] == 0 && matrix[x][y+1] == 0){
			matrix[x][y] =9;
			y++;
		}
		else if (matrix[x][y] == 0 && matrix[x][y+1] == 2){
			matrix[x][y] = 9;
			y++;
		}
		else if (matrix[x][y] == 0 && matrix[x][y+1] == 1){
			matrix[x][y] = 9;
			x++;
		}
		else if (matrix[x+1][y] == 1 && matrix[x][y+1] == 1){
			matrix[x][y] = 9;
			break;
		}
		else{
			break;
		}
		
	}
	
	for (int i=1; i <= 10; i++){
		for (int j=1; j <=10; j++){
			cout << matrix[i][j] << ' ';
		}
		cout << endl;
	}
	return 0;
}