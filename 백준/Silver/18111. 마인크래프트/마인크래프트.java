import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.text.Format;
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Deque;
import java.util.Iterator;
import java.io.*;

class Pair{
    int first;
    int second;

    public Pair(int first, int second){
        this.first = first;
        this.second = second;
    }
}

public class Main{
    static Deque<Pair> deque;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        
        String[] input = br.readLine().split(" ");
        int n = Integer.parseInt(input[0]);
        int m = Integer.parseInt(input[1]);
        int b = Integer.parseInt(input[2]);

        int[][] array = new int[n][m];
        int min = Integer.MAX_VALUE;
        int max = Integer.MIN_VALUE;
        for (int i=0; i< n; i++){
            String[] tmp = br.readLine().split(" ");
            for (int j=0; j <m; j++){
                array[i][j] = Integer.parseInt(tmp[j]);
                if (array[i][j] < min){
                    min = array[i][j];
                }
                if (array[i][j] > max){
                    max = array[i][j];
                }
            }
        }

        int second = Integer.MAX_VALUE;
        int height = -1;

        for (int floor= min; floor <= max; floor++){
            int sec = 0;
            int minus = 0;
            int plus = 0;
            for (int i=0; i<n; i++){
                for (int j=0; j<m; j++){
                    int val = array[i][j];
                    if (val < floor){
                        minus += (floor-val);
                    } else if (val > floor){
                        plus += (val - floor);
                    }
                }
            }
            int land = b + plus - minus;
            if (land < 0){
                continue;
            }
            sec += (plus*2 + minus);

            if (sec < second){
                second = sec;
                height = floor;
            } else if (sec == second && floor > height){
                second = sec;
                height = floor;
            }
        }

        bw.write(second + " " + height + "\n");


        bw.flush();
        bw.close();
        br.close();    
    }
    
    public static void printArray(int[] tmp){
        StringBuilder sb = new StringBuilder();
        for (int i=0; i<tmp.length; i++){
            sb.append(tmp[i] + " ");
        }
        System.out.println(sb);
    }
}