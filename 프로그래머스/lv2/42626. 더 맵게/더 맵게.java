import java.util.*;
class Solution {
    public int solution(int[] scoville, int K) {
        int answer = 0;
        PriorityQueue<Integer> pq = new PriorityQueue<>();
        for (int i=0; i<scoville.length; i++){
            pq.add(scoville[i]);
        }
        
        while (true){
            boolean flag = true;
            for (int val : pq){
                if (val < K){
                    flag = false;
                    break;
                }
            }
            if (flag){
                break;
            }
            if (pq.size() == 1){
                return -1;
            }
            int a = pq.poll();
            int b = pq.poll();
            pq.add(a+(b*2));
            answer++;
        }
        return answer;
    }
}