import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.Deque;
import java.util.HashMap;
import java.util.HashSet;
import java.util.Iterator;
import java.util.List;
import java.util.Map;
import java.util.Stack;

import javax.print.DocFlavor.STRING;

class Pair {
    int first; 
    int second;

    public Pair(int first, int second) {
        this.first = first;
        this.second = second;
    }
}
public class Main{
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        
        int r = Integer.parseInt(br.readLine());
        ArrayList<Pair> list = new ArrayList<>();
        int maxX =0; int maxY =0;

        for (int i=0; i <6 ; i++){
            String[] tmp = br.readLine().split(" ");
            int tidx = Integer.parseInt(tmp[0]);
            int val = Integer.parseInt(tmp[1]);
            list.add(new Pair(tidx, val));
            if (tidx == 1 || tidx == 2){
                if (val > maxX){
                    maxX = val;
                }
            } else {
                if (val > maxY){
                    maxY = val;
                }
            }
        }
        
        int result = maxX*maxY;
        list.addAll(list);
        
        for (int i=3; i<list.size(); i++){
            if (list.get(i-1).first == list.get(i-3).first
                && list.get(i).first == list.get(i-2).first){
                result -= (list.get(i-1).second * list.get(i-2).second);
                break;
            }
        }

        bw.write(r*result + "\n");
        bw.flush();
        bw.close();
        br.close();
    }

    

    public static void printArray(char[][] arr){
        StringBuilder sb = new StringBuilder();

        for (int i = 1; i < arr.length; i++) {
            for (int j = 1; j < arr[i].length; j++) {
                sb.append(arr[i][j]);
            }
            sb.append('\n');
        }
        System.out.println(sb);
        
    }
}