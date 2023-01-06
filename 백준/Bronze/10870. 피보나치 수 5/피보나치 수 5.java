import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.lang.reflect.Array;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Comparator;
import java.util.HashMap;
import java.util.Map;
import java.util.jar.Attributes.Name;


class Pair{
    int age;
    int order;
    String name;

    public Pair(int first, int second, String name){
        this.age = first;
        this.order = second;
        this.name =name;
    }
}

public class Main{    
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        
        int n = Integer.parseInt(br.readLine());
        bw.write(calc(n) + "\n");

        bw.flush();
        bw.close();
        br.close();
    }
    public static int calc(int n){
        if (n == 1){
            return 1;
        } else if (n == 0){
            return 0;
        }
        return calc(n-1)+ calc(n-2);
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