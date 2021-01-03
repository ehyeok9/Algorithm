#include <iostream>
using namespace std;

int main()
{
	int input;
	cout << "물건의 개수를 입력하시오: ";
	cin >> input;
	int result;
	
	if (input >= 10){
		result = (input*100)*0.9;	
	}
	else{
		result = input*100;
	}
	
	cout << result << endl;
	return 0; 
}