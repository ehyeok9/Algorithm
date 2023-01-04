#include <iostream>
using namespace std;

int main(){
    int current_hour, current_minute, current_second;
    int finish_hour, finish_minute, finish_second;

    scanf("%d:%d:%d", &current_hour, &current_minute, & current_second);
    scanf("%d:%d:%d", &finish_hour, &finish_minute, &finish_second);

    int result_hour, result_minute, result_second;
    
    if (current_hour < finish_hour){
        result_hour = finish_hour - current_hour;
    }
    else if (current_hour > finish_hour){
        result_hour = (24-current_hour) + finish_hour;
    }
    else{
        if (current_minute > finish_minute){
            result_hour = 23;
        }
        else if (current_minute < finish_minute){
            result_hour = 0;
        }
        else{
            if (current_second > finish_second){
                result_hour = 23;
            }
            else if (current_second < finish_second){
                result_hour = 0;
            }
            else{
                result_hour = 24;
                result_minute = 0;
                result_second = 0;
            }
        }
    }

    if (current_minute < finish_minute){
        result_minute = finish_minute - current_minute;
    }
    else if (current_minute > finish_minute){
        result_minute = (60-current_minute) + finish_minute;
        result_hour --;
    }
    else {
        result_minute = 0;
    }

    if (current_second < finish_second){
        result_second = finish_second - current_second;
    }
    else if (current_second > finish_second){
        result_second = (60-current_second) + finish_second;
        if (result_minute > 0){
            result_minute --;
        }
        else{
            result_minute = 59;
            result_hour --;
        }
    }
    else{
        result_second = 0;
    }

    printf("%.2d:%.2d:%.2d", result_hour, result_minute, result_second);
    
    return 0;
}