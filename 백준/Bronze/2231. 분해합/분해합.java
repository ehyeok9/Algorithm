import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayDeque;
import java.util.Deque;
import java.util.Stack;

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
        int result = -1;

        for (int i=1; i<=n ;i++){
            int total = i;
            int temp = i; 
            while(temp > 0){
                total += (temp%10);
                temp /= 10;
            }

            if (total == n){
                result = i;
                break;
            }
        }

        if (result == -1){
            bw.write(0 + "\n");
        } else{
            bw.write(result + "\n");
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