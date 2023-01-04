#include <iostream>
#include <vector>
#include <cmath>

using namespace std;

int main() {
    int m,n;
    int minimum, total = 0;
    vector<int> list;

    scanf("%d %d", &m, &n);

    for (int i=m ; i <= n ; i++){
        if (sqrt(i) - (int)sqrt(i) == 0 ){
            list.push_back(i);
        }
    }

    if (list.empty()){
        printf("%d", -1);
    }
    else{
        
        minimum = list[0];

        for (int i=0; i < list.size(); i++){
            total += list[i];        
        }

        printf("%d\n%d", total, minimum);
    }
    
    return 0;

}


