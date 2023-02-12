import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.PriorityQueue;

class Point{
    int y;
    int x;
    int day;
    public Point(int y, int x, int day){
        this.y = y;
        this.x = x;
        this.day = day;
    }
}

public class Main{
    static int n;
    static int m;
    static int[][] array;
    static boolean[][] visited;
    static int[] dy = {-1, 1, 0, 0};
    static int[] dx = {0, 0, -1, 1};
    static int result = 0;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        
        String[] input = br.readLine().split(" ");
        n = Integer.parseInt(input[0]);
        m = Integer.parseInt(input[1]);

        array = new int[m][n];
        visited = new boolean[m][n];
        boolean flag = true;
        for (int i=0; i<m; i++){
            String[] tmp = br.readLine().split(" ");
            for (int j=0; j< n; j++){
                array[i][j] = Integer.parseInt(tmp[j]);
                if (array[i][j] == 0){
                    flag = false;
                }
            }
        }
        
        
        if (flag) {
            bw.write(0 + "\n");
        } else {
            ArrayList<Point> param = new ArrayList<>();
            for (int y=0; y < m; y++){
                for (int x=0; x<n; x++){
                    if (array[y][x] == 1){
                        param.add(new Point(y, x, 0));
                    }
                }
            }

            bfs(param);

            boolean tomato = false;
            for (int y=0; y < m; y++){
                for (int x=0; x<n; x++){
                    if (array[y][x] == 0){
                        tomato = true;
                        break;
                    }
                }
            }
            if (tomato){
                bw.write(-1 + "\n");
            } else {
                bw.write(result + "\n");
            }
        }

        bw.flush();
        bw.close();
        br.close();    
    }

    public static void bfs(ArrayList<Point> param){
        ArrayDeque<Point> deque = new ArrayDeque<>();
        for (Point po : param){
            deque.add(po);
            visited[po.y][po.x] = true;
        }

        while (!deque.isEmpty()){
            Point node = deque.pollFirst();
            result = node.day;
            for (int i=0; i<4; i++){
                int y = node.y + dy[i];
                int x = node.x + dx[i];
                
                if (y < 0 || y >= m || x < 0 || x >= n) continue;
                if (array[y][x] == -1 || array[y][x] == 1) continue;
                if (visited[y][x] == true) continue;
                array[y][x] = 1;
                deque.add(new Point(y, x, node.day+1));
                visited[y][x] = true;
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