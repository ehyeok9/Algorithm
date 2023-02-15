import java.util.*;

class Solution {
    boolean solution(String s) {
        boolean answer = true;
        ArrayDeque<Character> deque = new ArrayDeque<>();
        
        for (int i=0; i<s.length(); i++){
            char data = s.charAt(i);
            if (deque.isEmpty()){
                deque.add(data);
            } else if (data == ')' && deque.getLast() == '('){
                deque.pollLast();
            } else if (data == '('){
                deque.add(data);
            } else {
                return false;
            }
        }
        
        if (!deque.isEmpty()){
            return false;
        }

        return answer;
    }
}