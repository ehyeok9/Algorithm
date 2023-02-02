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
    static long[] array;
    static long m;
    static ArrayList<Integer> result;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        
        String[] ip = br.readLine().split(" ");
        int n = Integer.parseInt(ip[0]);
        m = Long.parseLong(ip[1]);

        String[] input = br.readLine().split(" ");
        array = new long[n];

        for (int i=0; i<n; i++){
            array[i] = Long.parseLong(input[i]);
        }
        input = null;

        bw.write(binarySearch(0, (long)Integer.MAX_VALUE + 1) + "\n");
        bw.flush();
        bw.close();
        br.close();    
    }

    public static long binarySearch(long lo, long hi){
        while (lo+1 < hi){
            long mid = (lo +hi)/2;
            if (cutting(mid)){
                lo = mid;
            } else {
                hi = mid;
            }
        }
        return lo;
    }

    public static boolean cutting(long val){
        long sum = 0;
        for (int i=0; i<array.length; i++){
            long tmp = array[i] - val;
            if (tmp > 0){
                sum += tmp;
            }
        }
        if (sum >= m){
            return true;
        }
        return false;
    }

    
    
    public static void printArray(int[] tmp){
        StringBuilder sb = new StringBuilder();
        for (int i=0; i<tmp.length; i++){
            sb.append(tmp[i] + " ");
        }
        System.out.println(sb);
    }
}