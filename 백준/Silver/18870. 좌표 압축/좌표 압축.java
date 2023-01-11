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
    static int[] gold = new int[10001];
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        
        int n = Integer.parseInt(br.readLine());
        String[] input = br.readLine().split(" ");
        int[] array = new int[n];

        for (int i=0; i<n;i++){
            array[i] = Integer.parseInt(input[i]);
        }

        Arrays.sort(array);
        HashMap<Integer, Integer> map = new HashMap<>();

        int prev = array[0];
        map.put(prev, 0);
        int idx = 1;
        
        for (int i=1; i<array.length; i++){
            if (prev == array[i]){
                continue;
            }
            map.put(array[i], idx);
            idx++;
            prev = array[i];            
        }

        for (int i=0; i<input.length; i++){
            int temp = Integer.parseInt(input[i]);
            bw.write(map.get(temp) + " ");
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