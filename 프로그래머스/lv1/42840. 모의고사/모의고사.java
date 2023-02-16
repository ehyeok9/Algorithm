import java.util.*;

class Solution {
    public int[] solution(int[] answers) {
        int[] su1 = {1,2,3,4,5};
        int[] su2 = {2,1,2,3,2,4,2,5};
        int[] su3 = {3,3,1,1,2,2,4,4,5,5};
        
        int[] result = new int[3];
        for (int i=0; i<answers.length; i++){
            if (su1[i%su1.length] == answers[i]){
                result[0]++;
            } 
            if (su2[i%su2.length] == answers[i]){
                result[1]++;
            } 
            if (su3[i%su3.length] == answers[i]){
                result[2]++;
            }
        }
        
        int mx = 0;
        for (int i=0; i<3; i++){
            if (result[i] > mx){
                mx = result[i];
            }
        }
        
        ArrayList<Integer> list = new ArrayList<>();
        for (int i=0; i<3; i++){
            if (result[i] == mx){
                list.add(i+1);
            }
        }
        
        int[] answer = new int[list.size()];
        for (int i=0; i<list.size(); i++){
            answer[i] = list.get(i);
        }
        return answer;
    }
}