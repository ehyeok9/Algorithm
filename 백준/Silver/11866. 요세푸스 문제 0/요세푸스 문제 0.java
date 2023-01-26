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

public class Main{
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        
        String[] input = br.readLine().split(" ");
        int n = Integer.parseInt(input[0]);
        int k = Integer.parseInt(input[1]);
        Deque<Integer> deque = new ArrayDeque<>();
        
        for (int i=1; i<=n ;i++){
            deque.add(i);
        }

        Iterator it = deque.iterator();
        ArrayList<Integer> array = new ArrayList<>();
        int cnt = 0;
        while(deque.size() > 1){
            int num = deque.pollFirst();
            cnt++;
            if (cnt == k){
                cnt = 0;
                array.add(num);
            } else{
                deque.add(num);
            }
        }
        array.add(deque.poll());
        
        StringBuilder sb = new StringBuilder();
        sb.append("<");
        for (int i=0; i<array.size(); i++){
            if (i == array.size()-1){
                sb.append(array.get(i) +">");
            } else {
                sb.append(array.get(i) +", ");
            }
        }
        System.out.print(sb);
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