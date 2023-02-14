import java.util.*;
class Pair{
    int progress;
    int speed;
    
    public Pair(int progress, int speed){
        this.speed = speed;
        this.progress = progress;
    }
}

class Solution {
    public int[] solution(int[] progresses, int[] speeds) {
        int[] answer;
        ArrayDeque<Pair> deque = new ArrayDeque<>();
        
        for (int i=0; i<progresses.length; i++){
            deque.add(new Pair(progresses[i], speeds[i]));
        }
        
        ArrayList<Integer> result = new ArrayList<>();
        while (!deque.isEmpty()){
            Pair first = deque.pollFirst();
            if (first.progress < 100){
                int loop = deque.size();
                first.progress += first.speed;
                deque.add(first);
                for (int i=0; i<loop; i++){
                    Pair tmp = deque.pollFirst();
                    tmp.progress += tmp.speed;
                    deque.add(tmp);
                }
            } else {
                int num = 1;
                while(!deque.isEmpty()){
                    Pair tmp = deque.pollFirst();
                    if (tmp.progress < 100){
                        deque.addFirst(tmp);
                        break;
                    } else {
                        num++;
                    }
                }
                result.add(num);
            }
        }
        answer = new int[result.size()];
        for (int i=0; i<result.size(); i++){
            answer[i] = result.get(i);
        }
        
        return answer;
    }
}