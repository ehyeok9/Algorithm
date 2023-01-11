import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.lang.reflect.Array;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Comparator;


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
        
        int n = Integer.parseInt(br.readLine());
        String[] array = new String[n];

        for (int i=0; i<n; i++){
            array[i] = br.readLine();
        }
        Arrays.sort(array, new Comparator<String>() {
            @Override
            public int compare(String o1, String o2) {
                if (o1.length() < o2.length()){
                    return -1;
                } else if (o1.length() > o2.length()){
                    return 1;
                } else {
                    if (o1.compareTo(o2) < 0){
                        return -1;
                    } else if (o1.compareTo(o2) > 0){
                        return 1;
                    } else{
                        return 0;
                    }
                }
            }
        });
        String prev = "";

        for (String val : array){
            if (val.equals(prev)){
                continue;
            }
            bw.write(val+"\n");   
            prev = val;
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