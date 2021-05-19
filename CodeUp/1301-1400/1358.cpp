#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <cmath>
using namespace std;

int main(){
	int num, space, constant;
	cin >> num;
	string str;
	constant = num/2+1;
	
	for (int i=1; i <= num/2+1; i++){
		str = "";
		space = constant - i;
		for (int j=0; j < space; j++){
			str += " ";
		}
		if (i == 1){
			str += "*";
		}
		else{
			for (int j = 0 ; j < 1 + (i-1)*2; j++){
				str += "*";
			}
		}
		cout << str << endl;
		
	}
	return 0;
}

