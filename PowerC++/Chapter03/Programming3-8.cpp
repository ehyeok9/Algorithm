#include <iostream>
using namespace std;

int main()
{
	char input;
	char a = 'a', z = 'z', A = 'A', Z = 'Z';
	cin >> input;
	
	if ((input >= A) && (input <= Z)){
		input += 32;
		cout << input << endl;
	}
	else if ((input >= a) && (input <= z)){
		cout << "대문자로 입력하시오." << endl;
	}
	return 0; 
}