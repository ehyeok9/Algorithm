import java.util.*;

class Solution {
    
    public boolean solution(String[] phone_book) {
        boolean answer = true;
        Arrays.sort(phone_book);
        for (int i=0; i< phone_book.length-1; i++){
            String str = phone_book[i];
            String val = phone_book[i+1];
            if (str.length() > val.length()) continue;
            val = val.substring(0, str.length());
            if (str.equals(val)) return false;
        }
        return answer;
    }
    
}