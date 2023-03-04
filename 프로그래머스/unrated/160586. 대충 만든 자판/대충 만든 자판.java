import java.util.*;

class Solution {
    public int[] solution(String[] keymap, String[] targets) {
        int[] answer = new int[targets.length];
        HashMap<Character, Integer> map = new HashMap<>();
        for (int i=0; i<keymap.length; i++){
            String str = keymap[i];
            for (int j=0; j<str.length(); j++){
                char c = str.charAt(j);
                if (map.containsKey(c)){
                    int val = map.get(c);
                    if (j+1 < val){
                        map.put(c, j+1);
                    }
                } else {
                    map.put(c, j+1);
                }
            }
        }
        
        for (int i=0; i<targets.length; i++){
            int sum = 0;
            String str = targets[i];
            for (int j=0; j<str.length(); j++){
                char c = str.charAt(j);
                if (map.containsKey(c)){
                    sum += map.get(c);
                } else{
                    sum = -1;
                    break;
                }
            }
            answer[i] = sum;
        }
        return answer;
    }
}