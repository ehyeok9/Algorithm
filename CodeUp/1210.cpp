#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <cmath>
using namespace std;

int main(){
	int a, result = 0;
	
	for (int i = 0; i<2; i++){
		cin >> a;
		switch(a){
			case 1:
				result += 400;
				break;
			case 2:
				result += 340;
				break;
			case 3:
				result += 170;
				break;
			case 4:
				result += 100;
				break;
			case 5:
				result += 70;
				break;
		}
	}
	
	if (result > 500){
		cout << "angry";
	}
	else{
		cout << "no angry";
	}
	
	return 0;
}
