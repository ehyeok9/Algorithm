#include <iostream>
using namespace std;

int main()
{
	double f_temp;
	double c_temp;
	
	cout << "섭씨온도를 입력하시오: ";
	cin >> c_temp;
	
	
	f_temp = (c_temp*9.0/5.0)+32.0;
	cout << "화씨온도는 " << f_temp << "입니다\n";
	
	
	return 0;
}

/*
1. 올바르게 나오지 않는다. 그 이유는 c_temp의 자료형이 int였기 때문이다.
2. double로 수정하였다.
3. 화씨온도를 사용자로부터 받게 끔 수정하였다.
4. 화씨온도의 자료형을 double로 수정하였다. 그리고 수식의 값들도 실수형태로 수정하였다.
*/