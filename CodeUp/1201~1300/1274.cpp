#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
using namespace std;

int main(){
	int n, flag = 1;
	cin >>n;
	
	for (int i=2; i < n; i++){
		if(n%i==0){
			flag = 0;
		}
	}
	
	if (flag == 0){
		cout << "not prime";
	}
	else{
		cout << "prime";
	}
	return 0;
}