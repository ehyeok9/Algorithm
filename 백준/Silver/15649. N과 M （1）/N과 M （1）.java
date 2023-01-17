import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;


public class Main{
    static int[] array;
    static int[] tmp;
    static boolean[] visited;
    static ArrayList<ArrayList<Integer>> result;
    static int m;
    static int n;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        
        String[] input = br.readLine().split(" ");
        n = Integer.parseInt(input[0]);
        m = Integer.parseInt(input[1]);

        result = new ArrayList<>();
        visited = new boolean[n+1];
        tmp = new int[m+1];

        dfs(0);
        
        bw.flush();
        bw.close();
        br.close();
    }

    public static void dfs(int num){
        if (num == m) {
            StringBuilder sb = new StringBuilder();
            for (int i=0; i< tmp.length-1; i++){
                sb.append(tmp[i] + " ");
            }
            System.out.println(sb);
            return;
        }

        for (int i=0; i< n; i++){
            if (visited[i] == false){
                tmp[num] = i+1;
                visited[i] = true;
                dfs(num+1);
                visited[i] = false;
            }
        }
        return;
    }
}