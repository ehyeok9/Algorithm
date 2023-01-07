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
    int first;
    int second;

    public Pair(int first, int second){
        this.first = first;
        this.second = second;
    }
}

public class Main{
    static int cnt = 0;
    static int val = 0;
    static int k;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        
        int n = Integer.parseInt(br.readLine());
        String sb = "";
        for (int i=0; i<(n/4); i++) {
            sb += "long ";
        }
        bw.write(sb + "int");
        bw.flush();
        bw.close();
        br.close();
    }

    public static void merge_sort(int[] array , int p, int r){
        if (p < r){
            int q = (p+r)/2;
            merge_sort(array, p, q);
            merge_sort(array, q+1, r);
            merge(array, p, q, r);
        }
    }

    public static void merge(int[] array, int p, int q, int r){
        int i = p; int j = q+1; int t = 1;
        int[] tmp = new int[array.length+1];

        while (i <= q && j <= r){
            if (array[i] <= array[j]){
                tmp[t++] = array[i++];
            } else {
                tmp[t++] = array[j++];
            }
        }

        while (i <= q){
            tmp[t++] = array[i++];
        }

        while (j <= r){
            tmp[t++] = array[j++];
        }

        i = p; t = 1;
        while(i <= r){
            cnt++;
            if (cnt == k){
                val = tmp[t];
                break;
            }
            array[i++] = tmp[t++];
        }
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