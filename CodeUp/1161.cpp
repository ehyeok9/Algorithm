#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <cmath>
using namespace std;

int main(){
	int a,b;
	cin >> a >> b;
	string str1 = "홀수";
	string str2 = "짝수";
	string result = "";
	
	if (a%2==0){
		result = result + str2 + "+";
	}
	else{
		result = result + str1 + "+";
	}
	
	if (b%2==0){
		result = result + str2 + "=";
	}
	else{
		result = result + str1 + "=";
	}
	
	if ((a+b)%2==0){
		result = result + str2;
	}
	else{
		result = result + str1;
	}
	
	cout << result;
	
	return 0;
}
