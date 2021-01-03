#include <iostream>
using namespace std;

int main(){
	double height, input_weight;
	cout << "키와 몸무게를 입력하시오: ";
	cin >> height >> input_weight;
	
	double weight = (height -100)*0.9;
	
	if (weight < input_weight){
		cout << "과체중입니다." << endl;
	}
	else if (input_weight < weight){
		cout << "저체중입니다." << endl;
	}
	else{
		cout << "표준체중입니다." << endl;
	}
	
	return 0;
}