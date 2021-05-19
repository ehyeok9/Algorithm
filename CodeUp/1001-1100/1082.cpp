#include <iostream>
using namespace std;

int main(){
	
	int a;
	
	cin >> hex >> a;
	
	for (int i = 1; i < 16 ; i++){
		cout << hex;
		cout << uppercase;
		cout << a << "*" << hex << i << "=" << hex << i*a << endl;
	}
	return 0;
}
