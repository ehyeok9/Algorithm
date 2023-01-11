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
        
        int[][] array = new int[9][9];
        int maxVal = -1;
        int row = -1;
        int col = -1;

        for (int i=0; i<9; i++){
            String[] element = br.readLine().split(" ");
            for (int j=0; j<9; j++){
                int val = Integer.parseInt(element[j]);
                if (val > maxVal){
                    maxVal = val;
                    row = i;
                    col = j;
                }
            }
        }

        bw.write(maxVal + "\n");
        bw.write((row+1) + " " + (col+1));

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