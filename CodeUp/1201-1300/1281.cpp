#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <cmath>
using namespace std;

int main(){
	int a, b, value = 0 ;
	cin >> a >> b;
	string sentence = "";
	
	for (int i=a; i <= b; i++){
		if (i%2==0){
			value -= i;
			sentence.push_back('-');
			sentence += to_string(i);
		}
		else{
			value += i;
			if (i != a){
				sentence.push_back('+');
			}
			sentence += to_string(i);
		}
	}
	
	sentence += ("=" + to_string(value));
	cout << sentence;
	return 0;
}