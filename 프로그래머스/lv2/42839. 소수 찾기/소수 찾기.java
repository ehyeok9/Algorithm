import java.util.*;

class Solution {
    int answer = 0;
    ArrayList<Character> list = new ArrayList<>();
    HashSet<Integer> set = new HashSet<>();
    boolean[] visited;
    
    public int solution(String numbers) {
        for (int i=0; i<numbers.length(); i++){
            list.add(numbers.charAt(i));
        }
        
        for (int i=1; i<=list.size(); i++){
            visited = new boolean[list.size()];
            char[] output = new char[i];
            permutation(output, i, 0);
        }
        return set.size();
    }
    
    public void permutation(char[] arr, int r, int depth){
        if (depth == r){
            String tmp = "";
            for (int i=0; i<r; i++){
                tmp += arr[i];
            }
            int num = Integer.parseInt(tmp);
            System.out.println(num);
            if (judge(num)){
                set.add(num);
            }
            return;
        }
        
        for (int i=0; i< list.size(); i++){
            if (visited[i] == false){
                visited[i] = true;
                arr[depth] = list.get(i);
                permutation(arr, r, depth+1);
                visited[i] = false;
            }
        }
    }
    
    public boolean judge(int num){
        if (num == 0 || num == 1) return false;
        for (int i=2; i< num; i++){
            if (num%i == 0){
                return false;
            }
        }
        return true;
    }
    
}