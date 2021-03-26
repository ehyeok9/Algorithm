#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
using namespace std;

int main(){
	string a,b;
	cin >> a >> b;
	
	if (a.length() != b.length()){
		if (a.length() > b.length()){
			cout << b << ' '<< a;
		}
		else{
			cout << a << ' '<< b;
		}
	}
	else{
		for (int i =0; i < a.length(); i++){
			if (a[i] != b[i]){
				if (a[i] > b[i]){
					cout << b << ' '<< a;
				}
				else{
					cout << a << ' '<< b;
				}
				break;
			}
			else{
				continue;
			}
		}
	}
	return 0;
}