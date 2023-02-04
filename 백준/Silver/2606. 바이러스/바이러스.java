import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;
import java.util.Deque;
import java.util.HashMap;
import java.util.HashSet;
import java.util.Iterator;

class Pair{
    int first;
    int second;

    public Pair(int first, int second){
        this.first = first;
        this.second = second;
    }
}

public class Main{
    static boolean[] visited;
    static Deque<Integer> deque;
    static HashMap<Integer, ArrayList<Integer>> map;
    static int result = 0;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        
        int n = Integer.parseInt(br.readLine());
        int m = Integer.parseInt(br.readLine());

        map = new HashMap<>();
        for (int i=0; i<m; i++){
            String[] in = br.readLine().split(" ");
            int key = Integer.parseInt(in[0]);
            int value = Integer.parseInt(in[1]);
            
            ArrayList<Integer> tmp;
            if (map.containsKey(key)){
                tmp = map.get(key);
            } else{
                tmp = new ArrayList<>();
            }
            tmp.add(value);
            map.put(key, tmp);

            if (map.containsKey(value)){
                tmp = map.get(value);
            } else {
                tmp = new ArrayList<>();
            }
            tmp.add(key);
            map.put(value, tmp);
        }

        deque = new ArrayDeque<>();
        visited = new boolean[n+1];
        bfs(1);
        
        bw.write(result + "\n");
        bw.flush();
        bw.close();
        br.close();    
    }

    public static void bfs(int start){
        visited[start] = true;
        deque.add(start);
        while(!deque.isEmpty()){
            int node = deque.pollFirst();
            ArrayList<Integer> tmp = map.get(node);
            if (tmp != null){
                for (int val : tmp){
                    if (!visited[val]){
                        visited[val] = true;
                        deque.add(val);
                        result++;
                    }
                }
            }

        }
    }

    public static void printArray(int[] tmp){
        StringBuilder sb = new StringBuilder();
        for (int i=0; i<tmp.length; i++){
            sb.append(tmp[i] + " ");
        }
        System.out.println(sb);
    }
}