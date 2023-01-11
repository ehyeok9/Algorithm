import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Arrays;
import java.util.Stack;

public class Main{    
    
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        
        int m = Integer.parseInt(br.readLine());
        int n = Integer.parseInt(br.readLine());

        int total = 0;
        int mini = -1;

        for (int i=m; i <=n; i++) {
            if (sosu(i)){
                total += i;
                if (mini == -1){
                    mini = i;
                }
            }
        }

        if (total == 0){
            bw.write(-1+"\n");
        }else {
            bw.write(total + "\n" + mini);
        }

        bw.flush();
        bw.close();
        br.close();
    }

    public static boolean sosu(int num){
        if (num == 1){
            return false;
        }
        for (int i=2; i< num; i++){
            if (num%i == 0){
                return false;
            }
        }
        return true;
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