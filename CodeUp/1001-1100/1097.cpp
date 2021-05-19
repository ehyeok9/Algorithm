#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main(){
	
	int baduk[20][20] = {};
	int cir;
	
	for (int i = 1; i < 20; i++){
		for (int j=1; j < 20; j++){
			cin >> cir;
			baduk[i][j] = cir;
		}
	}
	
	int num, x, y;
	cin >> num;
	int gip[num][2];
	
	for (int i=0; i < num; i++){
		cin >> x >> y;
		gip[i][0] = x;
		gip[i][1] = y;
	}
	
	for (int i=0; i < num; i++){
		
		for (int j=1; j < 20; j++){
			if (j == gip[i][1]){
				continue;
			}
			if (baduk[gip[i][0]][j] ==1){
				baduk[gip[i][0]][j] = 0;
			}
			else{
				baduk[gip[i][0]][j]= 1;
			}
		}
		
		for (int k=1; k<20; k++){
			if (k == gip[i][0]){
				continue;
			}
			if (baduk[k][gip[i][1]] == 1){
				baduk[k][gip[i][1]] = 0;
			}
			else{
				baduk[k][gip[i][1]] = 1;
			}
		}
	}
	
	for (int i=1; i <20; i++){
		for (int j=1; j< 20; j++){
			cout << baduk[i][j] << ' ';
		}
		cout << endl;
	}
	return 0;
}