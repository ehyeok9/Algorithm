#include <iostream>
#include <string>
#include <algorithm>
using namespace std;

int main(){
	string password;
	cin >> password;
	
	string protect1 = "", protect2 = "";
	
	for (int i=0; i < password.length(); i++){
		protect1.push_back(password[i] +2);
		protect2.push_back((password[i] * 7)%80 +48);
	}
	
	cout << protect1 << endl << protect2;
	return 0;
}