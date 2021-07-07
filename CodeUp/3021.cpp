#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <stack>
using namespace std;

int main(){
	string a,b;
	cin >> a >> b;
	bool flag = false;
	string result = "";
	int fir=0, sec=0;
	int leng;
	if (a.length() > b.length()){
		leng = a.length() - b.length();
		for (int i=0; i< leng; i++){
			b.insert(0, "0");
		}
	}
	else if (a.length() < b.length()){
		leng = b.length() - a.length();
		for (int i=0; i< leng; i++){
			a.insert(0, "0");
		}
	}
	else{
		leng = 0;
	}
	
	for (int i = max(a.length(), b.length())-1; i > -1; i--){
		if (flag){
			fir = a[i] - '0';
			sec = b[i] - '0';
			if ((fir + sec + 1 >= 10) && i != 0){
				result += to_string((fir+sec+1)%10);
				flag = true;
			}
			else if (i == 0){
				if (fir+sec+1 >=10){
					result += to_string((fir+sec+1)%10);
					int re = (fir+sec+1)/10;
					result += to_string(re%10);
				}
				else{
					result += to_string(fir+sec+1);
					flag = false;
				}
			}
			else{
				result += to_string(fir+sec+1);
				flag = false;
			}
		}
		else{
			fir = a[i] - '0';
			sec = b[i] - '0';
			if ((fir + sec >= 10) && i != 0){
				result += to_string((fir+sec)%10);
				flag = true;
			}			
			else if (i == 0){
				if (fir+sec >=10){
					result += to_string((fir+sec)%10);
					int re = (fir+sec)/10;
					result += to_string(re%10);
				}
				else{
					result += to_string(fir+sec);
					flag = false;
				}
			}
			else{
				result += to_string(fir+sec);
				flag = false;
			}
		}
	}
	
	for (int i=result.length()-1; i >-1; i--){
		cout << result[i];
	}
	
	
	return 0;
}
