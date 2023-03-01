import java.util.*; 

class Solution {
    int answer = 0;
    public int solution(int[] numbers, int target) {
        dfs(numbers, target, 0, 0, numbers.length);
        return answer;
    }
    
    public void dfs(int[] numbers, int target, int num, int depth, int r){
        if (depth == r){
            if (target == num){
                answer++;
            }
            return;
        }
        
        dfs(numbers, target, num+numbers[depth], depth+1, r);
        dfs(numbers, target, num-numbers[depth], depth+1, r);
    }
}