#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <cmath>
using namespace std;

bool sosu(int);

int main(){
	int num;
	cin >> num;
	int a,b, flag = 0;
	
	for (int i=2; i < num; i++){
		if (num%i == 0){
			if (sosu(i) && sosu(num/i)){
				a = i;
				b = num/i;
				break;
			} 
		}
		
		if (i == num-1){
			flag = 1;
		}
	}
	
	if ((flag == 1) || (a == 1 || b == 1) || (num ==2) || ( num == 1)){
		cout << "wrong number";
	}
	else{
		cout << a << ' ' << b;
	}
	return 0;
}

bool sosu(int value){
	
	bool result = true;
	
	for (int i=2; i<value; i++){
		if (value%i == 0){
			result = false;
			break;
		}
	}
	
	return result;
}