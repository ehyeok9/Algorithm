#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <cmath>
using namespace std;

int main(){
	int n, space, middle = 0;
	cin >> n;
	space = n-1;
	string str;
	
	for (int i=0; i < n;i++){
		str = "";
		for (int j=0; j< space; j++){
			str += " ";
		}
		str += "*";
		for (int j=0; j < middle; j++){
			str += " ";
		}
		str += "*";
		cout << str << endl;
		space--;
		middle += 2;
	}
	space ++;
	middle -= 2;
	for (int i=0; i < n;i++){
		str = "";
		for (int j=0; j< space; j++){
			str += " ";
		}
		str += "*";
		for (int j=0; j < middle; j++){
			str += " ";
		}
		str += "*";
		cout << str << endl;
		space++;
		middle -= 2;
	}
	
	return 0;
}

