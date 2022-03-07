#include <iostream>
#include <vector>
#include <utility>
#include <string>
#include <algorithm>
using namespace std;

int main(){
    int n;

    scanf("%d", &n);
    vector<string> name;
    vector<int> day;
    vector<int> month;
    vector<int> year;

    for (int i=0; i<n; i++){
        string str;
        cin >> str;
        name.push_back(str);

        int a,b,c;
        scanf("%d %d %d", &a, &b, &c);
        day.push_back(a);
        month.push_back(b);
        year.push_back(c);
    }

    int maximum = -1;
    int result_idx = -1;

    for (int i=0; i<n; i++){
        if (year[i] > maximum){
            maximum = year[i];
            result_idx = i;
        }
        else if (year[i] == maximum){
            if (month[result_idx] < month[i]){
                result_idx = i;
            }
            else if (month[result_idx] == month[i]){
                if (day[result_idx] < day[i]){
                    result_idx = i;
                }
            }   
        }
    }
    
    cout << name[result_idx] << endl;
    maximum = 2020;
    result_idx = -1;

    for (int i=0; i<n; i++){
        if (year[i] < maximum){
            maximum = year[i];
            result_idx = i;
        }
        else if (year[i] == maximum){
            if (month[result_idx] > month[i]){
                result_idx = i;
            }
            else if (month[result_idx] == month[i]){
                if (day[result_idx] > day[i]){
                    result_idx = i;
                }
            }   
        }
    }

    cout << name[result_idx];

    return 0;
}