#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <cmath>
using namespace std;

int main(){
	int list[26][26], list_2[26][26] = {};
	int a;
	
	for (int i=1; i<=25; i++){
		for(int j=1; j<=25; j++){
			scanf("%d", &a);
			list[i][j] = a;
		}
	}
	
	for (int i=1; i<=24;i++){
		for (int j=1; j<=25; j++){
			int cnt = 0;
			if (i == 1 && j == 1){
				cnt = list[i+1][j] + list[i][j+1] + list[i+1][j+1];
				if (list[i][j] == 0 && cnt == 3){
					list_2[i][j] = 1;
				}
				else if (list[i][j] == 1 && (cnt >= 4 || cnt <= 1)){
					list_2[i][j] = 0;
				}
				else if (list[i][j] == 1 && (cnt == 2 || cnt == 3)){
					list_2[i][j] = 1;
				}
			}
			else if (i ==1 && j == 25){
				cnt = list[i+1][j] + list[i][j-1] + list[i+1][j-1];
				if (list[i][j] == 0 && cnt == 3){
					list_2[i][j] = 1;
				}
				else if (list[i][j] == 1 && (cnt >= 4 || cnt <= 1)){
					list_2[i][j] = 0;
				}
				else if (list[i][j] == 1 && (cnt == 2 || cnt == 3)){
					list_2[i][j] = 1;
				}
			}
			else if (i == 25 && j == 1){
				cnt = list[i-1][j] + list[i-1][j+1] + list[i][j+1];
				if (list[i][j] == 0 && cnt == 3){
					list_2[i][j] = 1;
				}
				else if (list[i][j] == 1 && (cnt >= 4 || cnt <= 1)){
					list_2[i][j] = 0;
				}
				else if (list[i][j] == 1 && (cnt == 2 || cnt == 3)){
					list_2[i][j] = 1;
				}
			}
			else if (i == 25 && j == 25){
				cnt = list[i-1][j] + list[i-1][j-1] + list[i][j-1];
				if (list[i][j] == 0 && cnt == 3){
					list_2[i][j] = 1;
				}
				else if (list[i][j] == 1 && (cnt >= 4 || cnt <= 1)){
					list_2[i][j] = 0;
				}
				else if (list[i][j] == 1 && (cnt == 2 || cnt == 3)){
					list_2[i][j] = 1;
				}
			}
			else if (i == 25){
				cnt = list[i-1][j-1] + list[i-1][j] + list[i-1][j+1] + list[i][j-1] + list[i][j+1];
				if (list[i][j] == 0 && cnt == 3){
					list_2[i][j] = 1;
				}
				else if (list[i][j] == 1 && (cnt >= 4 || cnt <= 1)){
					list_2[i][j] = 0;
				}
				else if (list[i][j] == 1 && (cnt == 2 || cnt == 3)){
					list_2[i][j] = 1;
				}
			}
			else if (i == 1){
				cnt = list[i][j-1] + list[i][j+1] + list[i+1][j-1] + list[i+1][j] + list[i+1][j+1];
				if (list[i][j] == 0 && cnt == 3){
					list_2[i][j] = 1;
				}
				else if (list[i][j] == 1 && (cnt >= 4 || cnt <= 1)){
					list_2[i][j] = 0;
				}
				else if (list[i][j] == 1 && (cnt == 2 || cnt == 3)){
					list_2[i][j] = 1;
				}
			}
			else if (j == 1){
				cnt = list[i-1][j] + list[i-1][j+1] + list[i][j+1] + list[i+1][j+1] + list[i+1][j];
				if (list[i][j] == 0 && cnt == 3){
					list_2[i][j] = 1;
				}
				else if (list[i][j] == 1 && (cnt >= 4 || cnt <= 1)){
					list_2[i][j] = 0;
				}
				else if (list[i][j] == 1 && (cnt == 2 || cnt == 3)){
					list_2[i][j] = 1;
				}
			}
			else if (j == 25){
				cnt = list[i-1][j-1] + list[i][j-1] + list[i+1][j-1] + list[i-1][j] + list[i+1][j];
				if (list[i][j] == 0 && cnt == 3){
					list_2[i][j] = 1;
				}
				else if (list[i][j] == 1 && (cnt >= 4 || cnt <= 1)){
					list_2[i][j] = 0;
				}
				else if (list[i][j] == 1 && (cnt == 2 || cnt == 3)){
					list_2[i][j] = 1;
				}
			}
			else{
				cnt = list[i-1][j-1] + list[i-1][j] + list[i-1][j+1] + list[i][j-1] + list[i][j+1] + list[i+1][j-1] + list[i+1][j] + list[i+1][j+1];
				if (list[i][j] == 0 && cnt == 3){
					list_2[i][j] = 1;
				}
				else if (list[i][j] == 1 && (cnt >= 4 || cnt <= 1)){
					list_2[i][j] = 0;
				}
				else if (list[i][j] == 1 && (cnt == 2 || cnt == 3)){
					list_2[i][j] = 1;
				}
			}
		}
	}
	
	for (int i=1; i<=25; i++){
		for(int j=1; j<=25; j++){
			printf("%d ", list_2[i][j]);
		}
		printf("\n");
	}
	
	return 0;
}

