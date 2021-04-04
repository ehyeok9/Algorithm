#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <cmath>
using namespace std;

int main(){
	int a,b,c;
	cin >> a >> b >> c;
	int list[3] = {a,b,c};
	sort(list, list+3);
	
	if (list[2] < list[1] + list[0]){
		cout << "yes";
	}
	else{
		cout << "no";
	}
	
	return 0;
}
