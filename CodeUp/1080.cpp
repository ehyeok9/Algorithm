#include <iostream>
using namespace std;

int main(){
	int num, i = 1, sum = 0;
	cin >> num;
	
	for (i; sum +i < num; i++){
		sum += i;
	}
	cout << i ;
	return 0;
}