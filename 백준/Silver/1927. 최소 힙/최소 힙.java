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
    static int[] array;
    static boolean[] visited;
    static int[] dy = {-1, 1};
    static int xrange = 100001;
    static int end;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        
        int n = Integer.parseInt(br.readLine());
        PriorityQueue<Integer> queue = new PriorityQueue<>();

        for (int i=0; i<n; i++){
            int num = Integer.parseInt(br.readLine());
            if (num == 0){
                if (queue.isEmpty()){
                    bw.write(0 + "\n");
                } else{
                    bw.write(queue.poll() + "\n");
                }
            } else {
                queue.add(num);
            }
        }

        bw.flush();
        bw.close();
        br.close();    
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