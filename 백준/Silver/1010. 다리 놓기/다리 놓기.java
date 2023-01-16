import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Arrays;


public class Main{
    static int[][] array;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        
        int t = Integer.parseInt(br.readLine());
        for (int i=0; i<t; i++){
            String[] input = br.readLine().split(" ");
            int n = Integer.parseInt(input[1]);
            array = new int[n+1][n+1];
            int r = Integer.parseInt(input[0]);
            bw.write(combination(n, r) + "\n");
        }

        
        bw.flush();
        bw.close();
        br.close();
    }

    public static int combination(int n, int r){
        if (n == r || r == 0 ){
            return 1;
        }
        if (array[n][r] > 0){
            return array[n][r];
        }
        return array[n][r] = combination(n-1, r-1) + combination(n-1, r);
    }
}