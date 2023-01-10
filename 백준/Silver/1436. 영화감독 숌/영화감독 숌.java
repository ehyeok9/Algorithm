import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayDeque;
import java.util.ArrayList;
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
        int cnt = 0;
        int val = 666;
        while(true){
            if (checkNum(val)){
                cnt++;
            }
            if (cnt == n){
                bw.write(val + "\n");
                break;
            }
            val++;
        }

        bw.flush();
        bw.close();
        br.close();
    }

    public static boolean checkNum(int num){
        int cnt = 0;
        while(num > 0){
            if (num%10 == 6){
                cnt++;
            } else{
                cnt = 0;
            }
            num /= 10;

            if (cnt == 3) {
                return true;
            }
        }
        return false;
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