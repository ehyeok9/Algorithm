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
        
        while(true){
            String line = br.readLine();
            if (line.equals(".")){
                break;
            }
            Deque<Character> stack = new ArrayDeque<>();
            boolean result = true;
            for (int i=0; i< line.length(); i++){
                char c = line.charAt(i);
                if (c == '(' || c =='['){
                    stack.add(c);
                    continue;
                }
                if (c == ']'){
                    if (stack.isEmpty()){
                        result = false;
                        break;
                    }
                    else if (stack.pollLast() == '['){
                        continue;
                    } else{
                        result = false;
                        break;
                    }
                }
                if (c == ')'){
                    if (stack.isEmpty()){
                        result = false;
                        break;
                    }
                    else if (stack.pollLast() == '('){
                        continue;
                    } else{
                        result = false;
                        break;
                    }
                }
            }
            if (!stack.isEmpty()){
                result = false;
            }
            if (result){
                bw.write("yes\n");
            } else{
                bw.write("no\n");
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