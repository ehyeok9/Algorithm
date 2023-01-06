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
        
        while (true) {
            int n = Integer.parseInt(br.readLine());
            if (n == 0){
                break;
            }

            bw.write(eratos(n) + "\n");
        }

        bw.flush();
        bw.close();
        br.close();
    }

    public static int eratos(int n){
        int[] array = new int[(n*2)+1];
        array[1] = 1;
        int result = 0;

        for (int i=2; (i*i)<= 2*n; i++){
            if (sosu(i)){
                for (int j= i*2; j <= 2*n; j+=i){
                    array[j] = 1;
                }
            }
        }

        for (int i=n+1; i <=n*2; i++) {
            if (array[i] == 0){
                result++;
            }
        }

        return result;
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