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
        
        int[][] array = new int[101][101];

        int tcase = Integer.parseInt(br.readLine());
        for (int i=0; i<tcase; i++){
            String[] input = br.readLine().split(" ");
            int row = Integer.parseInt(input[0]);
            int col = Integer.parseInt(input[1]);

            for (int j=row; j<row+10; j++){
                for (int k=col; k<col+10; k++){
                    array[j][k] = 1;
                }
            }
        }

        int result = 0;

        for (int i=1; i< 101; i++){
            for (int j=1; j< 101; j++){
                if (array[i][j] == 1){
                    result++;
                }
            }
        }

        bw.write(result+"\n");
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