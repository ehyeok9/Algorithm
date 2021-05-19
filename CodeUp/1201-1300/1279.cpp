#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <cmath>
using namespace std;

int main(){
	int a, b, value = 0 ;
	cin >> a >> b;
	
	for (int i=a; i <= b; i++){
		if (i%2==0){
			value -= i;
		}
		else{
			value += i;
		}
	}
	
	cout << value;
	return 0;
}