#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <cmath>
using namespace std;

int main(){
	int time, ban1,ban2;
	cin >> time  >> ban1 >> ban2;
	time = 90 -time;
	
	if (time%5==0){
		ban1 = time/5 + ban1;
	}
	else{
		ban1 = time/5 + ban1 + 1;
	}
	
	if (ban1 == ban2){
		cout << "same";
	}
	else if (ban1 > ban2){
		cout << "win";
	}
	else{
		cout << "lose";
	}
	
	return 0;
}

