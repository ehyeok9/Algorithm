#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <cmath>
using namespace std;

int main(){
	int num;
	cin >> num;
	int value, flag = 0, flag2 =3;
	
	for (int i =2; i < num; i++){
		if (num%i == 0){
			for (int j=2; j < i; j++){
				if (i % j ==0){
					flag = 1;
					break;
				}
			}
			if (flag == 1){
				flag =0;
				continue;
			}
			else{
				flag2 = 4;
				cout << i << ' ' << num/i;
				break;
			}
		}
	}

	if (flag2 == 3){
		cout << "wrong number";
	}
	
	return 0;
}