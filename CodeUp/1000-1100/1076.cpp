#include <iostream>
using namespace std;

int main(){
	
	char value, start = 'a';
	cin >> value;
	
	while (true){
		if (value == start){
			cout << value;
			break;
		}
		cout << start << " ";
		start += 1;
	}
	return 0;
}
