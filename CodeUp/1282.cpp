#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <cmath>
using namespace std;

int main(){
	int num;
	cin >> num;
	int value;
	double u;
	
	for (int i =1; i <=num; i++){
		value = num - i;
		u = value;
		if (sqrt(u) - (int)(sqrt(u)) == 0){
			cout << i << ' ' << (int)(sqrt(u));
			break;
		}
	}
	return 0;
}