#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
using namespace std;

int main(){
	int num;
	cin >> num;
	
	for (int i=1; i <=9; i++){
		printf("%d*%d=%d\n",num,i,num*i);
	}
	return 0;
}