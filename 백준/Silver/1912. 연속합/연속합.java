import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.text.Format;
import java.util.Arrays;
import java.io.*;

public class Main{
    static int[] result;
    static int[] value;
    static long num;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        
        int n = Integer.parseInt(br.readLine());
        String[] input = br.readLine().split(" ");
        value = new int[n];
        for (int i=0; i<n; i++){
            value[i] = Integer.parseInt(input[i]);
        }
        input = null;
        result = new int[n+1];

        result[0] = value[0];
        num= result[0];
        for (int i=1; i < n; i++){
            dp(i);
        }

        bw.write(num+"\n");

        bw.flush();
        bw.close();
        br.close();    
    }

    public static void dp(int n){
        int a = result[n-1] + value[n];
        if (a > value[n]){
            result[n] = a;
        } else{
            result[n] = value[n];
        }
        num = Math.max(num, result[n]);    
    }
    
}