#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <cmath>
using namespace std;

int main(){
	int num, cnt = 0;
	cin >> num;
	string str = "";
	
	for (int i=num ; i > 0; i--){
		for (int k=0; k < cnt; k++){
			cout << " ";
		}
		for (int j = num - cnt; j >0; j--){
			cout << "*";
		}
		cout << endl;
		cnt ++;
	}
	
	return 0;
}

