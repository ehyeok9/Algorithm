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
        
        String[] input = br.readLine().split(" ");
        int m = Integer.parseInt(input[0]);
        int n = Integer.parseInt(input[1]);
        int[] array = new int[n+1];
        array[1] = 1;

        for (int i=2; (i*i)<= n; i++){
            if (sosu(i)){
                for (int j= i*2; j <= n; j+=i){
                    array[j] = 1;
                }
            }
        }

        for (int i=m; i <=n; i++) {
            if (array[i] == 0){
                bw.write(i+"\n");        
            }
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