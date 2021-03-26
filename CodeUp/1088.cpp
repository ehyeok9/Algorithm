#include <iostream>
using namespace std;

int main(){
	int num, sum;
	cin >> num;
	
	for (int i=0; i <= num ; i++){
		if (i > num){
			break;
		}
		if (i % 3 ==0){
			continue;
		}
		cout << i << " ";
	}
	return 0;
}