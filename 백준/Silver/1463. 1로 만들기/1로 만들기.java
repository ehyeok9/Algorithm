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
    static int[] array;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        
        int n = Integer.parseInt(br.readLine());
        array = new int[n+1];
        array[1] = Integer.MAX_VALUE;

        dp(n, 0);

        bw.write(array[1] + "\n");
        bw.flush();
        bw.close();
        br.close();    
    }

    public static void dp(int n, int cnt){
        // System.out.println(String.format("n = %d / cnt = %d", n, cnt));
        if (n == 1){
            if (cnt < array[n]){
                array[n] = cnt;
            }
            return;
        }
        
        if (array[n] != 0 && array[n] < cnt){
            return;
        }
        array[n] = cnt;

        if (n%3 == 0){
            dp(n/3, cnt+1);
        }

        if (n%2 == 0){
            dp(n/2 , cnt+1);
        }

        dp(n-1, cnt+1);
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