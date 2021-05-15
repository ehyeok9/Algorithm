#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
using namespace std;

int main(){
	int num, total = 0, value;
	cin >> num;
	
	for(int i=0; i< num; i++){
		cin >> value;
		if (value%2 ==0){
			total += 1;
		}
	}
	
	cout << total;
	return 0;
}