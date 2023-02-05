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
    static int yrange;
    static int xrange;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        
        String[] input = br.readLine().split(" ");
        yrange = Integer.parseInt(input[0]);
        xrange = Integer.parseInt(input[1]);
        array = new int[yrange][xrange];
        visited = new boolean[yrange][xrange];

        for (int i=0; i<yrange; i++){
            String line = br.readLine();
            for (int j=0; j<xrange; j++){
                array[i][j] = Integer.parseInt(line.substring(j, j+1));
            }
        }
        
        bfs(0, 0);
        bw.write(array[yrange-1][xrange-1] + "\n");

        bw.flush();
        bw.close();
        br.close();    
    }

    public static void bfs(int y, int x){
        Deque<Pair> deque = new ArrayDeque<>();
        deque.add(new Pair(y, x));
        visited[y][x] = true;

        while (!deque.isEmpty()){
            Pair node = deque.pollFirst();

            for (int i=0; i<4; i++){
                int ny = node.first + dy[i];
                int nx = node.second + dx[i];
                
                if (check(ny, nx) && array[ny][nx] != 0 && !visited[ny][nx]){
                    array[ny][nx] = array[node.first][node.second] +1;
                    deque.add(new Pair(ny, nx));
                    visited[ny][nx] = true;
                }
            }
        }
    }

    public static boolean check(int y, int x){
        if (y <0 || y >= yrange){
            return false;
        }
        if (x <0 || x >= xrange){
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