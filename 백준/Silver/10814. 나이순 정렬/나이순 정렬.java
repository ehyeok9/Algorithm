import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.lang.reflect.Array;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Comparator;
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
        Pair[] array = new Pair[n];

        for (int i=0; i<n; i++){
            String[] temp = br.readLine().split(" ");
            array[i] = new Pair(Integer.parseInt(temp[0]), i, temp[1]);
        }
        Arrays.sort(array, new Comparator<Pair>() {
            @Override
            public int compare(Pair prev, Pair after) {
                if (prev.age < after.age){
                    return -1;
                } else if (prev.age > after.age){
                    return 1;
                } else {
                    if (prev.order < after.order){
                        return -1;
                    } else if (prev.order > after.order){
                        return 1;
                    } else {
                        return 0;
                    }
                }
            }
        });

        for (Pair val : array){
            bw.write(val.age + " " + val.name +"\n");   
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