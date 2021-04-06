#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <cmath>
using namespace std;

int main(){
	int num;
	cin >> num;
	
	for (int i=1; i <=num; i++){
		if (i == 1 || i == num){
			for (int k =0; k < num; k++){
				cout << "*";
			}
		}
		else{
			for (int j =0; j < num; j++){
				if (j ==0 || j == num -1){
					cout << "*";
				}
				else{
					cout << " ";
				}
			}
		}
		cout << endl;
	}
	
	return 0;
}

