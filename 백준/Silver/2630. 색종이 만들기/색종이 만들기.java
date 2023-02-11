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
    static int result0 = 0;
    static int result1 = 0;
    static int[][] array;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        
        n = Integer.parseInt(br.readLine());
        array = new int[n+1][n+1];

        for (int y=0; y<n; y++){
            String[] input = br.readLine().split(" ");
            for (int x=0; x<n; x++){
                array[y+1][x+1] = Integer.parseInt(input[x]);
            }
        }

        conquer(1, 1, n);

        bw.write(result0 + "\n");
        bw.write(result1 + "\n");
        bw.flush();
        bw.close();
        br.close();    
    }

    public static void conquer(int y, int x, int n){
        if (n == 1){
            if (array[y][x] == 1){
                result1++;
            } else {
                result0++;
            }
            return;
        }
        if (judge1(y, x, n)){
            result1++;
            return;
        }

        if (judge0(y, x, n)){
            result0++;
            return;
        }

        int num = n/2;
        conquer(y, x, num);
        conquer(y, x+num, num);
        conquer(y+num, x, num);
        conquer(y+num, x+num, num);
    }

    public static boolean judge1(int y, int x, int num){
        for (int i=y; i<y+num; i++){
            for (int j=x; j<x+num; j++){
                if (array[i][j] == 0){
                    return false;
                }
            }
        }
        return true;
    }

    public static boolean judge0(int y, int x, int num){
        for (int i=y; i<y+num; i++){
            for (int j=x; j<x+num; j++){
                if (array[i][j] == 1){
                    return false;
                }
            }
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