import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Deque;
import java.util.HashMap;
import java.util.HashSet;
import java.util.Iterator;
import java.util.Map;
import java.util.Stack;

import javax.print.DocFlavor.STRING;

class Pair {
    int first; 
    int second;

    public Pair(int first, int second) {
        this.first = first;
        this.second = second;
    }
}
public class Main{
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        
        int n = Integer.parseInt(br.readLine());
        String[] input = br.readLine().split(" ");
        HashMap<String, Integer> map = new HashMap<>();

        for (int i=0; i< input.length; i++){
            String num = input[i];
            if (map.containsKey(num)) {
                map.put(num, map.get(num)+1);
            } else {
                map.put(num, 1);
            }
        }

        int m = Integer.parseInt(br.readLine());
        String[] val = br.readLine().split(" ");
        for (int i=0; i < m; i++){
            String num = val[i];
            if (map.containsKey(num)){
                bw.write(map.get(num) + " ");
            } else{
                bw.write(0 + " ");
            }
        }
        bw.flush();
        bw.close();
        br.close();
    }

    

    public static void printArray(char[][] arr){
        StringBuilder sb = new StringBuilder();

        for (int i = 1; i < arr.length; i++) {
            for (int j = 1; j < arr[i].length; j++) {
                sb.append(arr[i][j]);
            }
            sb.append('\n');
        }
        System.out.println(sb);
        
    }
}