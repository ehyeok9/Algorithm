#include <iostream>
using namespace std;

int main() {
    int n, price, option;
    scanf("%d", &n);

    for (int i=0; i<n; i++){
        int total = 0;
        scanf("%d\n%d", &price, &option);
        total += price;
        if (option != 0){
            int p,q;
            for (int j=0; j <option; j++){
                scanf("%d %d", &p, &q);
                total += p*q;
            }
        }
        printf("%d\n", total);
    }
    return 0;
}