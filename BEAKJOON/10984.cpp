#include <iostream>
using namespace std;

int main(){
    int t;
    scanf("%d", &t);
    
    for (int i=0; i<t; i++){
        int n;
        scanf("%d", &n);
        int aveg = 0;
        double gpa = 0;
        for (int j=0; j< n; j++){
            int temp;
            double d_temp;
            scanf("%d %lf", &temp, &d_temp);
            aveg += temp;
            gpa += temp * d_temp;            
        }
        printf("%d %.1lf\n", aveg, gpa/(double)aveg);        
    }

    return 0;
}