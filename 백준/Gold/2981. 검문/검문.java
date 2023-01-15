import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.Deque;
import java.util.HashMap;
import java.util.HashSet;
import java.util.Iterator;
import java.util.List;
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
        int[] input = new int[n];
        for (int i=0; i<n ; i++){
            input[i] = Integer.parseInt(br.readLine());
        }

        Arrays.sort(input);
        int value = input[1] - input[0];
        for (int i=2; i<n; i++){
            value = gcd(value, input[i] - input[i-1]);
            
        }

        for (int i=2; i<=value; i++){
            if (value%i == 0){
                bw.write(i + " ");
            }
        }

        
        bw.flush();
        bw.close();
        br.close();
    }

    public static int gcd(int a, int b){
        if (a%b == 0){
            return b;
        }
        return gcd(b, a%b);
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