#include <iostream>
using namespace std;

int main(){
	char input;
	cout << "알파벳을 하나 입력해주세요: ";
	cin >> input;
	bool determine = false;
	
	switch (input){
		case 'a':
			determine = true;
			break;
		case 'e':
			determine = true;
			break;
		case 'i':
			determine = true;
			break;
		case 'o':
			determine = true;
			break;
		case 'u':
			determine = true;
			break;
	}
	
	if (determine){
		cout << "모음입니다." << endl;
	}
	else{
		cout << "비모음입니다." << endl;
	}
	
	return 0;
}