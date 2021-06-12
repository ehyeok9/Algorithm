#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <cmath>
#include <stack>
using namespace std;

int main(){
	int n;
	scanf("%d", &n);
	stack<int> stk;
	vector<int> list;
	
	if ( n== 0 ){
		list.push_back(0);
	}
	while (n > 0){
		list.push_back(n%10);
		n /= 10;
	}
	
	for (int i=0; i< list.size(); i++){
		printf("%d", list[i]);
	}	
	return 0;
}
