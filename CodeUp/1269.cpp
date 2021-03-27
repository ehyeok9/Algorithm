#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
using namespace std;

int main(){
	int a,b,c,n,value, total=0;
	cin >> a >> b >> c >> n;
	value = a;
	
	for (int i =1; i <n;i++){
		value = value*b+c;
	}
	
	cout << value;
	return 0;
}