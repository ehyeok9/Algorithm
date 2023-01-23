import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.text.Format;
import java.io.*;

public class Main{
    static long[] result;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        
        int n = Integer.parseInt(br.readLine());
        
        for (int i=0; i<n; i++){
            int num = Integer.parseInt(br.readLine());
            result = new long[num+1];
            bw.write(dp(num) + "\n");
        }

        bw.flush();
        bw.close();
        br.close();    
    }

    public static long dp(int n){
        if (result[n] != 0){
            return result[n];
        }
        if (n <= 3){
            return 1;
        }
        return result[n] = dp(n-2) + dp(n-3);
    }
    
}