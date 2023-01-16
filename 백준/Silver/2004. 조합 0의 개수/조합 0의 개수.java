import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;

import javax.print.DocFlavor.STRING;


public class Main{
    static int[][] array;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        
        String[] input = br.readLine().split(" ");
        int n = Integer.parseInt(input[0]);
        int m = Integer.parseInt(input[1]);

        int num2 = zero2(n) - zero2(m) - zero2(n-m);
        int num10 = zero5(n) - zero5(m) - zero5(n-m);

        bw.write(Math.min(num2, num10) + "\n");
        
        bw.flush();
        bw.close();
        br.close();
    }

    public static int zero5(int num){
        int cnt = 0; 
        while(num >= 5){
            cnt += num/5;
            num /= 5;
        }
        return cnt;
    }
    public static int zero2(int num){
        int cnt = 0; 
        while(num >= 2){
            cnt += num/2;
            num /= 2;
        }
        return cnt;
    }
}