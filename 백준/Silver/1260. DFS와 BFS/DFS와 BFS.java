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

import javax.swing.text.AbstractDocument.BranchElement;

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
    static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        
        String[] input = br.readLine().split(" ");
        int n = Integer.parseInt(input[0]);
        int m = Integer.parseInt(input[1]);
        int r = Integer.parseInt(input[2]);

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
        dfs(r);
        System.out.println();
        visited = new boolean[n+1];
        bfs(r);

        bw.flush();
        bw.close();
        br.close();    
    }

    public static void dfs(int start){
        System.out.print(start + " ");
        visited[start] = true;
        ArrayList<Integer> arr = map.get(start);
        if (arr != null){
            Collections.sort(arr);
            for (int val: arr){
                if (!visited[val]){
                    dfs(val);
                }
            }
        }
    }

    public static void bfs(int start){
        StringBuilder sb = new StringBuilder();
        visited[start] = true;
        deque.add(start);
        while(!deque.isEmpty()){
            int node = deque.pollFirst();
            sb.append(node + " ");
            ArrayList<Integer> tmp = map.get(node);
            if (tmp != null){
                Collections.sort(tmp);
                for (int val : tmp){
                    if (!visited[val]){
                        visited[val] = true;
                        deque.add(val);
                    }
                }
            }

        }
        System.out.println(sb);
    }

    public static void printArray(int[] tmp){
        StringBuilder sb = new StringBuilder();
        for (int i=0; i<tmp.length; i++){
            sb.append(tmp[i] + " ");
        }
        System.out.println(sb);
    }
}