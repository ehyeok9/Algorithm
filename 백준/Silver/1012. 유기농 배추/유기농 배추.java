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
    static int result;
    static int yrange;
    static int xrange;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        
        int t = Integer.parseInt(br.readLine());
        for (int i=0; i<t; i++){
            String[] input = br.readLine().split(" ");
            xrange = Integer.parseInt(input[0]);
            yrange = Integer.parseInt(input[1]);
            int k = Integer.parseInt(input[2]);
            array = new int[yrange][xrange];
            visited = new boolean[yrange][xrange];

            for (int j=0; j < k; j++){
                String[] point = br.readLine().split(" ");
                array[Integer.parseInt(point[1])][Integer.parseInt(point[0])] =1;
            }

            result = 0;
            for (int y=0; y<yrange; y++){
                for (int x=0; x<xrange; x++){
                    if (array[y][x] == 1 && !visited[y][x]){
                        bfs(y, x);
                    }
                }
            }
            bw.write(result + "\n");
        }

        
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
                if (check(ny, nx) && array[ny][nx] == 1 && !visited[ny][nx]){
                    deque.add(new Pair(ny, nx));
                    visited[ny][nx] = true;
                }
            }
        }

        result++;
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