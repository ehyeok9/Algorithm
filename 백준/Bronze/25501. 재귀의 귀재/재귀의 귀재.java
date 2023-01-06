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
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        
        int n = Integer.parseInt(br.readLine());
        
        for (int i=0; i<n; i++){
            String tcase = br.readLine();
            bw.write(isPalindrome(tcase) + " " + cnt + "\n");
            cnt = 0;
        }

        bw.flush();
        bw.close();
        br.close();
    }
    public static int isPalindrome(String str){
        return recursion(str, 0, str.length()-1);
    }
    public static int recursion(String str, int l, int r){
        cnt++;
        if (l >= r){
            return 1;
        } else if (str.charAt(r) != str.charAt(l)){
            return 0;
        } else{
            return recursion(str, l+1, r-1);
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