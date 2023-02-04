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
    static int[][] array;
    static boolean[][] visited;
    static int[] dy = {-1, 1, 0 , 0};
    static int[] dx = {0 , 0, -1, 1};
    static ArrayList<Integer> result = new ArrayList<>();
    static int n;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        
        n = Integer.parseInt(br.readLine());
        array = new int[n][n];
        visited = new boolean[n][n];
        for (int i=0; i<n; i++){
            String input = br.readLine();
            for (int j=0; j<n; j++){
                array[i][j] = Integer.parseInt(input.substring(j, j+1));
            }
        }
        
        for (int i=0; i<n; i++){
            for (int j=0; j<n; j++){
                if (array[i][j] == 1 && !visited[i][j]){
                    bfs(i, j);
                }
            }
        }

        bw.write(result.size() + "\n");
        Collections.sort(result);
        for (int val : result){
            bw.write(val + "\n");
        }
        
        bw.flush();
        bw.close();
        br.close();    
    }

    public static void bfs(int y, int x){
        Deque<Pair> deque = new ArrayDeque<>();
        deque.add(new Pair(y, x));
        int sum = 1;
        while (!deque.isEmpty()){
            Pair node = deque.pollFirst();
            visited[node.first][node.second] = true;

            for (int i=0; i <4; i++){
                int ny = node.first + dy[i];
                int nx = node.second + dx[i];
                if (check(ny, nx) && !visited[ny][nx]){
                    if (array[ny][nx] == 1){
                        deque.add(new Pair(ny, nx));
                        sum++;
                    }
                    visited[ny][nx] = true;
                }
            }
        }
        result.add(sum);
    }

    public static boolean check(int y, int x){
        if (y >= n || y < 0){
            return false;
        }
        if (x >= n || x < 0){
            return false;
        }
        return true;
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