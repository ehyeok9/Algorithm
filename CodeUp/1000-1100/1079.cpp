#include <iostream>
using namespace std;

int main(){
	
	char vaule;
	
	while (true){
		cin >> vaule;
		if (vaule == 'q'){
			cout << vaule;
			break;
		}
		cout << vaule << endl;
	}
	return 0;
}
