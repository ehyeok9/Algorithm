import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.text.Format;
import java.util.Arrays;
import java.io.*;

public class Main{
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        
        String query = br.readLine();
        int tcase = Integer.parseInt(br.readLine());
        int[][] sumVal = new int[query.length()+1][];
        int[] tmp = new int[26];
        sumVal[0] = tmp.clone();
        for (int i=1; i <= query.length(); i++){
            int num = query.charAt(i-1) - 'a';
            tmp[num] += 1;
            sumVal[i] = tmp.clone();
        }

        for (int i=0; i < tcase; i++){
            String[] input = br.readLine().split(" ");
            int num = input[0].charAt(0) - 'a';
            int a = Integer.parseInt(input[1]);
            int b = Integer.parseInt(input[2]);    
            // System.out.println(String.format("(a=%d, b=%d, valA=%d, valB=%d) ", a, b, sumVal[a][num], sumVal[b+1][num]));
            bw.write(sumVal[b+1][num] - sumVal[a][num] + "\n");
        }
        
        bw.flush();
        bw.close();
        br.close();    
    }
    
    public static void printArray(int[] tmp){
        StringBuilder sb = new StringBuilder();
        for (int i=0; i<tmp.length; i++){
            sb.append(tmp[i] + " ");
        }
        System.out.println(sb);
    }
}