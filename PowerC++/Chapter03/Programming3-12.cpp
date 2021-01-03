#include <iostream>
#include <cmath>
using namespace std;

int main()
{
	double user_height, user_weight, user_age;
	cout << "나이, 키, 체중 순으로 입력하시오: ";
	cin >> user_age >> user_height >> user_weight;
	
	double coupe = user_weight / pow(user_height/100,2);
	
	if ((user_age >= 20) && (user_age < 30)){
		if (coupe >= 30.0){
			cout << "비만입니다." << endl;
		}
		else if (coupe >= 24.0){
			cout << "과체중입니다." << endl;
		}
		else if (coupe >= 18.0){
			cout << "표준체중입니다." << endl;
		}
		else if (coupe >= 17.9){
			cout << "저체중입니다." << endl;
		}
	}
	else if ((user_age >= 30) && (user_age < 40)){
		if (coupe >= 30.0){
			cout << "비만입니다." << endl;
		}
		else if (coupe >= 25.0){
			cout << "과체중입니다." << endl;
		}
		else if (coupe >= 18.5){
			cout << "표준체중입니다." << endl;
		}
		else if (coupe >= 18.4){
			cout << "저체중입니다." << endl;
		}
	}
	return 0;
}