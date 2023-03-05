import java.util.*;

class Solution {
    public String solution(String[] cards1, String[] cards2, String[] goal) {
        String answer = "Yes";
        ArrayDeque<String> card1 = new ArrayDeque<>();
        ArrayDeque<String> card2 = new ArrayDeque<>();
        for (int i=0; i<cards1.length; i++){
            card1.add(cards1[i]);
        }
        for (int i=0; i<cards2.length; i++){
            card2.add(cards2[i]);
        }
        
        for (int i=0; i<goal.length; i++){
            String gl = goal[i];
            String cd1 = "";
            String cd2 = "";
            if (!card1.isEmpty()){
                cd1 = card1.getFirst();
            }
            if (!card2.isEmpty()){
                cd2 = card2.getFirst();
            }
            
            if (cd1.equals(gl)){
                card1.poll();
            } else if (cd2.equals(gl)){
                card2.poll();
            } else {
                return "No";
            }
        }
        return answer;
    }
}