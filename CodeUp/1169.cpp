#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <cmath>
using namespace std;

int main(){
	int age, year;
	cin >> age;
	year = 2012 -age + 1;
	
	if ((year-2000) < 0){
		year -= 1900;
		printf("%d %d", year, 1);
	}
	else{
		year -= 2000;
		printf("%.2d %d", year, 3);
	}
	
	return 0;
}
