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

import javax.swing.text.AbstractDocument.BranchElement;

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
    static int[] array1;
    static int[] array2;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        
        int t = Integer.parseInt(br.readLine());
        for (int i=0; i<t; i++){
            int n = Integer.parseInt(br.readLine());
            array2 = new int[n+1];
            if (n == 0){
                bw.write("1 0\n");
                continue;
            }
            fibo(n);
            bw.write(array2[n-1] + " " + array2[n] + "\n");
        }

        bw.flush();
        bw.close();
        br.close();    
    }

    public static int fibo(int n){
        if (array2[n] != 0){
            return array2[n];
        }
        if (n == 1 || n == 0){
            return array2[n] = n;
        }
        return array2[n] = fibo(n-1) + fibo(n-2);
    }
    
    public static void printArray(int[] tmp){
        StringBuilder sb = new StringBuilder();
        for (int i=0; i<tmp.length; i++){
            sb.append(tmp[i] + " ");
        }
        System.out.println(sb);
    }
}