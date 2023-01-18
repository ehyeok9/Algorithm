import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.Stack;

class Pair{
    int first;
    int second;

    public Pair(int first, int second){
        this.first = first;
        this.second = second;
    }
}
public class Main{
    static int a = 0;
    static int b = 0;
    static int[] array;
    static int[][][] result = new int[101][101][101];
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        
        while(true) {
            String[] input = br.readLine().split(" ");
            int a = Integer.parseInt(input[0]);
            int b = Integer.parseInt(input[1]);
            if (a == 0 && b == 0){
                break;
            }
            if (a > b){
                bw.write("Yes\n");    
            } else{
                bw.write("No\n");    
            }
        }

        bw.flush();
        bw.close();
        br.close();
    }
    
    public static int dp(int a, int b, int c){
        if (result[a+50][b+50][c+50] != 0){
            return result[a+50][b+50][c+50];
        }
        if (a <= 0 || b <= 0 || c <= 0){
            return 1;
        }
        if (a > 20 || b > 20 || c > 20){
            dp(20, 20, 20);
        }
        if (a<b && b<c){
            return dp(a, b, c-1) + dp(a, b-1, c-1) - dp(a, b-1, c);
        }
        return dp(a-1, b, c) + dp(a-1, b-1, c) + dp(a-1, b, c-1) - dp(a-1, b-1, c-1);
    }

}