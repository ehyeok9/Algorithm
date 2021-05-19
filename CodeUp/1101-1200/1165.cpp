#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <cmath>
using namespace std;

int main(){
	int time, goal;
	cin >> time  >> goal;
	time = 90 -time;
	if (time%5==0){
		cout << time/5 + goal;
	}
	else{
		cout << time/5 + goal + 1;
	}
	
	return 0;
}
