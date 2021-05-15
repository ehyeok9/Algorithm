#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <cmath>
using namespace std;

int main(){
	int a;
	cin >> a;
	
	if (a%10 == 1){
		if (a == 11){
			cout << "11th";
		}
		else{
			cout << a << "st";
		}
	}
	else if (a%10 ==2){
		if (a == 12){
			cout << "12th";
		}
		else{
			cout << a << "nd";
		}
	}
	else if (a%10 ==3){
		if (a == 13){
			cout << "13th";
		}
		else{
			cout << a << "rd";
		}
	}
	else{
		cout << a << "th";
	}
	return 0;
}

