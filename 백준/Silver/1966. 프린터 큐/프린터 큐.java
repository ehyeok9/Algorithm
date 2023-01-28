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
        
        int t = Integer.parseInt(br.readLine());
        for (int i=0; i<t; i++){
            String[] value = br.readLine().split(" ");
            String[] input = br.readLine().split(" ");
            int m = Integer.parseInt(value[1]);

            deque = new ArrayDeque<>();
            for (int j=0; j<input.length; j++){
                Pair tmp = new Pair(Integer.parseInt(input[j]), j);
                deque.add(tmp);
            }

            int result = 0;
            while(true){
                int max = findMax();
                Pair tmp = deque.pollFirst();
                if (tmp.first < max){
                    deque.add(tmp);
                    continue;
                }
                if (tmp.first == max && tmp.second == m){
                    bw.write(++result + "\n");
                    break;
                }
                if (tmp.first == max){
                    result++;
                    continue;
                }
            }
        }
        bw.flush();
        bw.close();
        br.close();    
    }

    public static int findMax(){
        int max = 0;
        for (Pair tmp : deque){
            if (tmp.first > max){
                max = tmp.first;
            }
        }
        return max;        
    }
    
    public static void printArray(int[] tmp){
        StringBuilder sb = new StringBuilder();
        for (int i=0; i<tmp.length; i++){
            sb.append(tmp[i] + " ");
        }
        System.out.println(sb);
    }
}