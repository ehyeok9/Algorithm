import java.util.*;

class Pair{
    int val;
    int loc;
    
    public Pair(int val, int loc){
        this.val = val;
        this.loc = loc;
    }
}

class Solution {
    static int[] array = new int[10];
    public int solution(int[] priorities, int location) {
        
        ArrayDeque<Pair> deque = new ArrayDeque<>();
        for (int i=0; i< priorities.length; i++){
            deque.add(new Pair(priorities[i], i));
            array[priorities[i]] += 1;
        }
        
        int result = 0;
        while (true) {
            Pair tmp = deque.pollFirst();
            System.out.println(tmp.val);
            if (judge(tmp.val)){
                result++;
                array[tmp.val] -= 1;
                if (tmp.loc == location){
                    return result;
                }
            } else {
                deque.add(tmp);
            }
            
        }
    }
    
    public static boolean judge(int loc){
        for (int i=9; i> loc; i--){
            if (array[i] > 0){
                return false;
            }
        }
        return true;
    }
}