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
import java.util.PriorityQueue;

class Pair{
    int first;
    int second;

    public Pair(int first, int second){
        this.first = first;
        this.second = second;
    }
}

public class Main{
    static int n;
    static int m;
    static HashMap<Integer, ArrayList<Integer>> map;
    static boolean[] visited;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        
        String[] input = br.readLine().split(" ");
        n = Integer.parseInt(input[0]);
        m = Integer.parseInt(input[1]);
        map = new HashMap<>();

        for (int i=0; i<m; i++){
            String[] edge = br.readLine().split(" ");
            int a = Integer.parseInt(edge[0]);
            int b = Integer.parseInt(edge[1]);

            ArrayList<Integer> tmp = new ArrayList<>();
            if (map.containsKey(a)){
                tmp = map.get(a);
            }
            tmp.add(b);
            map.put(a, tmp);

            tmp = new ArrayList<>();
            if (map.containsKey(b)){
                tmp = map.get(b);
            }
            tmp.add(a);
            map.put(b, tmp);
        }

        visited = new boolean[n+1];
        int result = 0;
        for (int i=1; i<=n; i++){
            if (visited[i] == false){
                result++;
                bfs(i);
            }
        }

        bw.write(result + "\n");

        bw.flush();
        bw.close();
        br.close();    
    }

    public static void bfs(int val){
        ArrayDeque<Integer> deque = new ArrayDeque<>();
        deque.add(val);
        visited[val] = true;
        
        while(!deque.isEmpty()){
            int node = deque.pollFirst();
            if (map.containsKey(node)){
                ArrayList<Integer> values = map.get(node);
            
                for (int num : values){
                    if (!visited[num]){
                        deque.add(num);
                        visited[num] = true;
                    }
                }
            }
        }
    }

    public static void printArray(int[][] tmp){
        StringBuilder sb = new StringBuilder();
        for (int i=0; i<tmp.length; i++){
            for (int j=0; j<tmp[i].length; j++){
                sb.append(tmp[i][j]);
            }
            sb.append("\n");
        }
        System.out.println(sb);
    }
}