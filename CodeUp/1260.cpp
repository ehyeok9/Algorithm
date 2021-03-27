#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
using namespace std;

int main(){
	int a,b, total=0;
	cin >> a>>b;
	
	for (int i=a; i <= b; i++){
		if (i%3==0){
			total += i;
		}
	}
	
	cout << total;
	return 0;
}