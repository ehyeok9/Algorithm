import java.util.*;

class Solution {
    boolean[] visited;
    public int solution(int n, int[][] computers) {
        int answer = 0;
        visited = new boolean[n];
        
        for (int i=0; i< computers.length; i++){
            for (int j=0; j<computers[i].length; j++){
                if (computers[i][j] == 1 && visited[j] == false){
                    bfs(computers, j);
                    answer++;
                }
            }
        }
        return answer;
    }
    
    public void bfs(int[][] computers, int num){
        ArrayDeque<Integer> deque = new ArrayDeque<>();
        
        for (int i=0; i < computers[num].length; i++){
            if (computers[num][i] == 0) continue;
            if (visited[i] == true) continue;
    
            deque.add(i);
            visited[i] = true;
        }
        
        while (!deque.isEmpty()){
            int node = deque.pollFirst();
            
            for (int i=0; i<computers[node].length; i++){
                if (computers[node][i] == 0) continue;
                if (visited[i] == true) continue;
                deque.add(i);
                visited[i] = true;
            }   
        }
    }
}