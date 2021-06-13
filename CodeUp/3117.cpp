#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <cmath>
#include <stack>
using namespace std;

int main(){
	int n, a;
	scanf("%d", &n);
	stack<int> stk;
	
	for (int i=0; i<n; i++){
		scanf("%d", &a);
		if (a == 0 && stk.empty()){
			continue;
		}
		else if (a==0){
			stk.pop();
		}
		else{
			stk.push(a);
		}
	}
	
	int sum = 0;
	while (!stk.empty()){
		sum += stk.top();
		stk.pop();
	}
	
	printf("%d", sum);
	return 0;
}
