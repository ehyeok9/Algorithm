import java.util.*;
class Solution {
    public int[] solution(int brown, int yellow) {
        int sum = brown + yellow;
        int[] answer = new int[2];
        for (int i=3; i<sum/2; i++){
            if (sum%i == 0){
                int garo = Math.max(sum/i, i);
                int sero = Math.min(sum/i, i);
                int br = garo*2 + sero*2 -4;
                if (br == brown){
                    answer[0] = garo;
                    answer[1] = sero;
                    return answer;
                }
            }
        }
        return answer;
    }
}