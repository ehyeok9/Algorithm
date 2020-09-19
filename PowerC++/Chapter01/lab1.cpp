#include <iostream> // 
using namespace std;

int main(){
	int x,y,z;
	cout << "첫번째 수를 입력하시오: ";
	cin >> x;
	cout << "두번째 수를 입력하시오: ";
	cin >> y;
	z = x + y;
	cout << "x + y는 " << z << " 입니다." << endl;
	return 0;
}
/*
	5번 질문 : 컴파일 에러가 발생한다. 
	6번 질문 : \n 과 endl의 실행 결과는 달라지지 않는다.
	7번 질문 : 컴파일 오류가 발생한다. 함수 앞에 네이스페이스를 명시해준다. ex) std::cout
*/