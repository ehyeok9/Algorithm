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
        
        int n = Integer.parseInt(br.readLine());
        Deque<Integer> stack = new ArrayDeque<>();
        ArrayList<Integer> list = new ArrayList<>();

        for (int i=1; i<=n; i++){
            int t = Integer.parseInt(br.readLine());
            list.add(t);    
        }

        int cnt = 1;
        boolean flag = true;        
        ArrayList<Character> result = new ArrayList<>();
        for (int i=0; i<n; i++){
            int num = list.get(i);
            if (!stack.isEmpty() && stack.getLast() == num){
                stack.pollLast();
                result.add('-');
                continue;
            }

            if (num >= cnt){
                for (int j=cnt; j<=num; j++){
                    stack.add(cnt++);
                    result.add('+');
                }
                stack.pollLast();
                result.add('-');
                continue;
            }
            if (num < cnt && !stack.isEmpty() && stack.getLast() >= num){
                while (!stack.isEmpty()) {
                    int val = stack.pollLast();
                    result.add('-');
                    if (val == num){
                        break;
                    }
                }
                continue;
            } else{
                flag = false;
                bw.write("NO\n");
                break;
            }         
        }

        if (flag){
            for (char c : result){
                bw.write(c + "\n");
            }
        }

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