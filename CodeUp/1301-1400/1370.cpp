#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <cmath>
using namespace std;

int main(){
	int n,k;
	cin >> n >> k;
	int space;
	string str;
	
	for (int i=0; i<k; i++){
		space =0;
		for (int j=0; j < n*2-1; j++){
			str = "";
			for (int u=0; u<space; u++){
				str += ' ';
			}
			str += '*';
			if (j+1 < n){
				space++;
			}
			else{
				space--;
			}
			cout << str << endl;
		}
	}
	return 0;
}

