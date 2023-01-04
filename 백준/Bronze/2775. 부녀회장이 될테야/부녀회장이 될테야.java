import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Arrays;

public class Main{    
    static int[][] memo = new int[15][15];
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        
        int testcase = Integer.parseInt(br.readLine());
        
        for(int i=1; i < memo.length; i++){
            memo[0][i] = i;
        }


        for (int i=0; i<testcase; i++){
            int k = Integer.parseInt(br.readLine());
            int n = Integer.parseInt(br.readLine());

            bw.write(people(k, n) + "\n");
        }
        bw.flush();
        bw.close();
        br.close();
    }

    public static int people(int k, int n){
        if (k != 0){
            for (int i=1; i<=k; i++){
                for (int j=1; j <= n; j++){
                    memo[i][j] = sum(i-1, j);
                }
            }
        }
        return memo[k][n];
    }

    public static int sum(int k, int n){
        int result = 0;
        for (int i=1; i<=n; i++){
            result += memo[k][i];
        }
        return result;
    }

    public static void printArray(int[][] arr){
        for (int i = 0; i < arr.length; i++) {
            int[] inArr = arr[i];
            for (int j = 0; j < inArr.length; j++) {
                System.out.print(inArr[j] + " ");
            }
            System.out.println();
        }
    }
}