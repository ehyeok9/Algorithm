#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <cmath>
using namespace std;

int main(){
	int a;
	int list[3];
	
	for (int i=0; i<3; i++){
		cin >> a;
		list[i] = a;
	}
	
	sort(list, list+3);
	cout << list[1];
	return 0;
}
