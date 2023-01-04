#include <iostream>
#include <string>
#include <vector>
#include <utility>
#include <algorithm>
using namespace std;

int main() {
    int n;
    scanf("%d", &n);

    for (int i=0; i< n; i++){
        int p;
        scanf("%d", &p);
        vector<pair<int,string>> list;
        for (int j=0; j<p; j++){
            string name;
            int price;
            scanf("%d", &price);
            cin >> name;
            list.push_back(make_pair(price, name));
        }
        sort(list.begin(), list.end());
        cout << list.back().second;
        if (i != n-1){
            cout << endl;   
        }
    }

    return 0;

}