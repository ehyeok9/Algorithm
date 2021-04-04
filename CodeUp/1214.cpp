#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <cmath>
using namespace std;

int main(){
	int year, month, result;
	cin >> year >> month;
	bool co = false;
	
	if ((year%400==0) || (year%4 ==0 && !(year%100 ==0))){
		co = true;
	}
	
	if (co){
		switch (month){
			case 1:
				result = 31;
				break;
			case 2:
				result = 29;
				break;
			case 3:
				result = 31;
				break;
			case 4:
				result = 30;
				break;
			case 5:
				result = 31;
				break;
			case 6:
				result = 30;
				break;
			case 7:
				result = 31;
				break;
			case 8:
				result = 31;
				break;
			case 9:
				result = 30;
				break;
			case 10:
				result = 31;
				break;
			case 11:
				result = 30;
				break;
			case 12:
				result = 31;
				break;
		}
	}
	else{
		switch (month){
			case 1:
				result = 31;
				break;
			case 2:
				result = 28;
				break;
			case 3:
				result = 31;
				break;
			case 4:
				result = 30;
				break;
			case 5:
				result = 31;
				break;
			case 6:
				result = 30;
				break;
			case 7:
				result = 31;
				break;
			case 8:
				result = 31;
				break;
			case 9:
				result = 30;
				break;
			case 10:
				result = 31;
				break;
			case 11:
				result = 30;
				break;
			case 12:
				result = 31;
				break;
		}
	}
	cout << result;
	return 0;
}
