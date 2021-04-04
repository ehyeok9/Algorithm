#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <cmath>
using namespace std;

int main(){
	int time, minute;
	cin >> time >> minute;
	
	if (minute >= 30){
		cout << time << ' ' << minute -30;
	}
	else{
		if (time ==0){
			cout << 23 << ' ' << minute + 30;
		}
		else{
			cout << time -1 << ' ' << minute + 30;
		}
	}
	return 0;
}
