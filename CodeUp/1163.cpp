#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <cmath>
using namespace std;

int main(){
	int a, b, c;
	cin >> a >> b >> c;
	int result = a + b + c;
	result -= (result%100);
	result = (result%1000)/100;
	
	if (result%2 == 0){
		cout << "대박";
	}
	else{
		cout << "그럭저럭";
	}
	
	return 0;
}
