import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayList;


class Pair{
    int first;
    int second;

    public Pair(int first, int second){
        this.first = first;
        this.second = second;
    }
}

public class Main{    
    static int[] gold = new int[10001];
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        
        String[] input = br.readLine().split(" ");
        int n = Integer.parseInt(input[0]);
        int m = Integer.parseInt(input[1]);

        int[][] a = new int[n][m];
        int[][] b = new int[n][m];

        for (int i=0; i<n; i++){
            String[] element = br.readLine().split(" ");
            for (int j=0; j<m; j++){
                a[i][j] = Integer.parseInt(element[j]);
            }
        }

        for (int i=0; i<n; i++){
            String[] element = br.readLine().split(" ");
            for (int j=0; j<m; j++){
                b[i][j] = Integer.parseInt(element[j]);
            }
        }

        for (int i=0; i<n; i++){
            for (int j=0; j< m; j++){
                bw.write((a[i][j] + b[i][j]) + " ");
            }
            bw.write("\n");
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