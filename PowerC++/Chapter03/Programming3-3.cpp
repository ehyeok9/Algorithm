#include <iostream>
#include <cmath>
using namespace std;

int main()
{
	int binary, result = 0, count = 0;
	cout << "2진수를 입력하시오: ";
	cin >> binary;
	
	while (binary > 0){
		if ((binary%10) == 1){
			result += pow(2,count);
		}
		count ++;
		binary /= 10;
	}
	cout << "16진수로 변환한 값은 " << result << endl ;
	return 0;
}