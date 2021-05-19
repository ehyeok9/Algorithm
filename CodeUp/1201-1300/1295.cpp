#include <iostream>
#include <string>
using namespace std;

int main(){
	string c;
	cin >> c;
	
	for (int i=0; i < c.length(); i++){
		if (c[i] >= 65 && c[i] <= 90){
			c[i] += 32;
		}
		else if (c[i] >= 97 && c[i] <= 122){
			c[i] -= 32;
		}
		else{
			continue;
		}
	}
	
	cout << c;
	return 0;
}