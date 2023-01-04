import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Arrays;
import java.util.Stack;

public class Main{    
    static int[][] memo = new int[15][15];
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        
        int n = Integer.parseInt(br.readLine());
        
        if (n%5 == 0){
            bw.write((n/5 + "\n"));
        } else if (n == 4 || n == 7){
            bw.write(-1 + "\n");
        } else if (n%5 == 3){
            bw.write(((n/5 + 1) + "\n"));
        } else if (n%5 == 4){
            bw.write(((n/5 + 2) + "\n"));
        } else if (n%5 == 1){
            bw.write(((n/5 + 1) + "\n"));
        } else if (n%5 == 2){
            bw.write(((n/5 + 2) + "\n"));
        }

        bw.flush();
        bw.close();
        br.close();
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