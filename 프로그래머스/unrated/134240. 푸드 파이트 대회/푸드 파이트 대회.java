class Solution {
    public String solution(int[] food) {
        String answer = "";
        for(int i=1; i<food.length; i++){
            int num = food[i]/2;
            for (int j=0; j<num; j++) answer += (char)(i + '0');
        }
        int len = answer.length()-1;
        answer += '0';
        for (int i=len; i >= 0; i--){
            answer += answer.charAt(i);
        }
        return answer;
    }
}