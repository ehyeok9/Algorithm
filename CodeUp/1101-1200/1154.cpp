#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <cmath>
using namespace std;

int main(){
	int a,b;
	cin >> a >> b;
	
	if (a > b){
		cout << a-b;
	}
	else{
		cout << b-a;
	}
	return 0;
}
