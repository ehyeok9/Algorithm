#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <cmath>
using namespace std;

int main(){
	int num, cnt =0;
	cin >> num;
	
	for (int i=1; i <= num*2 -1; i++){
		if (i > num){
			--cnt;
		}
		else{
			++cnt;
		}
		
		for (int j=1; j<=cnt; j++){
			cout << "*";
		}
		cout << endl;
	}
	return 0;
}

