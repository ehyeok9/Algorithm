import java.util.*;
class Solution {
    boolean[] visited;
    int answer = 0;
    public int solution(int k, int[][] dungeons) {
        int[][] output = new int[dungeons.length][2];
        visited = new boolean[dungeons.length];
        permutation(dungeons, k, output, 0, dungeons.length);
        return answer;
    }
    
    public void permutation(int[][] dungeons, int k, int[][] output, int depth, int r){
        if (depth == r){
            int tmp = k;
            int cnt = 0;
            for (int i=0; i<output.length; i++){
                int minpiro = output[i][0];
                int byepiro = output[i][1];
                // System.out.println(String.format("%d / %d", minpiro, byepiro));
                if (tmp >= minpiro){
                    tmp -= byepiro;
                    cnt++;
                }
            }
            if (cnt > answer){
                answer = cnt;
            }
            return;            
        }
        
        for (int i=0; i < dungeons.length; i++){
            if (visited[i] == false){
                visited[i] = true;
                output[depth][0] = dungeons[i][0];
                output[depth][1] = dungeons[i][1];
                permutation(dungeons, k, output, depth+1, r);
                visited[i] = false; 
            }
        }
    }
}