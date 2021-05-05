#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <cmath>
using namespace std;

int main(){
	int n,m;
	vector<int> n_num;
	vector<int> m_num;
	int a;
	
	cin >> n;
	for (int i=0; i < n; i++){
		scanf("%d", &a);
		n_num.push_back(a);
	}
	cin >> m;
	for (int i=0; i < m; i++){
		scanf("%d", &a);
		m_num.push_back(a);
	}
	
	sort(n_num.begin(), n_num.end());

	for (int i = 0; i< m_num.size(); i++){
		int c = 0;
		int left = 0, right = n_num.size()-1;
		
		while(left <= right){
			int mid = (left+right)/2;
			if (n_num[mid] > m_num[i]){
				right = mid -1;
			}
			else if (n_num[mid] < m_num[i]){
				left = mid + 1;
			}
			else{
				c = 1;
				break;
			}
		}
		
		cout << c << ' ';
	}
	
	return 0;
}
