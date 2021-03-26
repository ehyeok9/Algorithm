#include <iostream>
using namespace std;

int main(){
	int limit, sum =0 ,i= 1;
	cin >> limit;
	while (true){
		if (sum >= limit){
			break;
		}
		sum += i;
		i++;
	}
	
	cout << sum;
	return 0;
}