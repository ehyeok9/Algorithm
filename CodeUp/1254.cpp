#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
using namespace std;

int main(){
	char a,b;
	cin >> a >> b;
	
	for (int i = a; i <= b; i++){
		char u = i;
		cout << u << ' ';
	}
	return 0;
}