#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <cmath>
using namespace std;

int main(){
	int a,b,c;
	cin >> a >> b >> c;
	
	if (a ==b && b ==c && c == a){
		cout << "정삼각형";
	}
	else if (((a == b) || (b == c) || (c==a)) && c < a+b){
		cout << "이등변삼각형";
	}
	else if (pow(a,2) + pow(b,2) == pow(c,2)){
		cout << "직각삼각형";
	}
	else if (c < a+b){
		cout << "삼각형";
	}
	else{
		cout << "삼각형아님";
	}
	return 0;
}
