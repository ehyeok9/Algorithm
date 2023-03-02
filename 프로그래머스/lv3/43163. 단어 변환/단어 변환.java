import java.util.*;

class Pair {
    int ans;
    String str;
    
    public Pair(int ans, String str){
        this.ans = ans;
        this.str = str;
    }
}

class Solution {
    boolean[] visited;
    public int solution(String begin, String target, String[] words) {        
        visited = new boolean[words.length];
        ArrayDeque<Pair> deque = new ArrayDeque<>();
        for (int i=0; i< words.length; i++){
            if (judge(begin, words[i])){
                visited[i] = true;
                deque.add(new Pair(1, words[i]));
            }
        }
        
        while(!deque.isEmpty()){
            Pair node = deque.poll();
            // System.out.println(node.str);
            if (node.str.equals(target)){
                return node.ans;
            }
            
            for (int i=0; i< words.length; i++){
                if (visited[i] == false && judge(node.str, words[i])){
                    deque.add(new Pair(node.ans + 1, words[i]));
                    visited[i] = true;
                }
            }
        }
        
        
        return 0;
    }
    
    public boolean judge(String a, String b){
        int cnt = 0;
        for (int i=0; i< a.length(); i++){
            char na = a.charAt(i);
            char nb = b.charAt(i);
            if (na != nb) cnt++;
            if (cnt > 1) return false;
        }
        return true;
    }
    
    
}