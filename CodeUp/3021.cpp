#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <cmath>
#include <stack>
using namespace std;

int main(){
	string a,b;
	cin >> a >> b;
	
	stack<char> first, second;
	for (int i=0; i <a.length(); i++){
		first.push(a[i]);
	}
	for (int i=0; i <b.length(); i++){
		first.push(b[i]);
	}
	
	int x,y,c;
	string result = "";
	bool flag = false;
	
	if (first.size() == second.size()){
		while(!first.empty()){
			x = first.top() - '0';
			y = second.top() - '0';
			
			if(flag){
				c = x+y+1;
			}
			else{
				c = x+y;
			}
			
			if (first.size() == 1){
				if (c > 9){
					result += to_string(c%10);
					result += "1";
				}
				else{
					result += to_string(c);
				}
			}
			else if (c > 9){
				result += to_string(c%10);
				flag = true;
			}
			else{
				result += to_string(c);
				flag = false;
			}			
			first.pop();
			second.pop();
		}
	}
	else{
		if (first.size() > second.size()){
			while(!first.empty()){
				if (second.empty()){
					if (flag){
						x = first.top() - '0' + 1;
						if (x > 9){
							result += to_string(x%10);
							flag = true;
						}
						else{
							result += to_string(x);
							flag = false;
						}
					}
					else{
						x = first.top() - '0';
						result += to_string(x);
					}
					first.pop();
				}
				else{
					x = first.top() - '0';
					y = second.top() - '0';

					if(flag){
						c = x+y+1;
					}
					else{
						c = x+y;
					}

					if (c > 9){
						result += to_string(c%10);
						flag = true;
					}
					else{
						result += to_string(c);
						flag = false;
					}			
					first.pop();
					second.pop();
				}
			}
		}
		else{
			while(!second.empty()){
				if (first.empty()){
					if (flag){
						y = second.top() - '0' + 1;
						if (x > 9){
							result += to_string(x%10);
							flag = true;
						}
						else{
							result += to_string(x);
							flag = false;
						}
					}
					else{
						y = second.top() - '0';
						result += to_string(x);
					}
					second.pop();
				}
				else{
					x = first.top() - '0';
					y = second.top() - '0';

					if(flag){
						c = x+y+1;
					}
					else{
						c = x+y;
					}

					if (c > 9){
						result += to_string(c%10);
						flag = true;
					}
					else{
						result += to_string(c);
						flag = false;
					}			
					first.pop();
					second.pop();
				}
			}
		}
	}
	
	for (int i=result.length()-1; i >-1; i--){
		printf("%c", result[i]);
	}
	return 0;
}
