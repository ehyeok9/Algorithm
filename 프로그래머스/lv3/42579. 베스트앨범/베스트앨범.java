import java.util.*;

class Pair1{
    int idx;
    int val;
    public Pair1(int idx, int val){
        this.idx = idx;
        this.val = val;
    }
}

class Pair2{
    String key;
    int total;
    public Pair2(String idx, int val){
        this.key = idx;
        this.total = val;
    }
}

class Solution {
    public int[] solution(String[] genres, int[] plays) {
        int[] answer;
        HashMap<String, ArrayList<Pair1>> map = new HashMap<>();
        for (int i=0; i< genres.length; i++){
            String key = genres[i];
            Pair1 src = new Pair1(i, plays[i]);
            
            ArrayList<Pair1> value = new ArrayList<>();
            if (map.containsKey(key)){
                value = map.get(key);
            }
            value.add(src);
            map.put(key, value);
        }
        
        Set<String> set = map.keySet();
        ArrayList<Pair2> genretop = new ArrayList<>();
        for (String key : set){
            genretop.add(new Pair2(key, getSum(map.get(key))));
        }
        
        Collections.sort(genretop, new Comparator<Pair2>() {
           @Override
            public int compare(Pair2 a, Pair2 b){
                return b.total - a.total;
            }
        });
        
        ArrayList<Integer> result = new ArrayList<>();
        for (int i=0; i<genretop.size(); i++){
            Pair2 genre = genretop.get(i);
            
            ArrayList<Pair1> values = map.get(genre.key);
            Collections.sort(values, new Comparator<Pair1>() {
               @Override
                public int compare(Pair1 a, Pair1 b){
                    return b.val - a.val;
                }
            });
            
            result.add(values.get(0).idx);
            if (values.size() != 1){
                result.add(values.get(1).idx);
            }
        }
        
        answer = new int[result.size()];
        for (int i=0; i<answer.length; i++){
            answer[i] = result.get(i);
        }
        return answer;
    }
    
    public int getSum(ArrayList<Pair1> arr){
        int total = 0;
        for (Pair1 val : arr){
            total += val.val;
        }
        return total;
    }
}