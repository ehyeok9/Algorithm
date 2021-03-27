#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
using namespace std;

int main(){
	int num, total =0;
	cin >> num;
	
	for (int i=1; i <= num; i++){
		total += i;
	}
	
	cout << total;
	return 0;
}