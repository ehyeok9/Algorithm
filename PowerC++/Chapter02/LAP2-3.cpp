#include <iostream>
using namespace std;

int main()
{
	int first, second;
	cout << "첫번째 피연산자를 입력하시오: ";
	cin >> first;
	cout << "두번째 피연산자를 입력하시오: ";
	cin >> second;
	
	int max, min, apsolute_first, apsolute_second;
	max = (first > second) ? first : second;
	min = (first > second) ? second : first;
	apsolute_first = (first > 0) ? first : -first;
	apsolute_second = (second > 0) ? second : -second;
	
	cout << max << min << apsolute_first << apsolute_second << endl;
	return 0;
}
