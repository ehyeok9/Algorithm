#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
using namespace std;

int main(){
	int a,b,total=0;
	cin >> a >> b;
	
	if (a%2==0){
		total += a*5;
	}
	else{
		total += (a+1)/2;
	}
	
	if (b%2==0){
		total += b*5;
	}
	else{
		total += (b+1)/2;
	}
	
	cout << total;
	return 0;
}