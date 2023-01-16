import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Arrays;
import java.util.HashMap;


public class Main{
    static int[][] array;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        
        int t = Integer.parseInt(br.readLine());
        for (int i=0; i<t; i++){
            int num = Integer.parseInt(br.readLine());
            HashMap<String, Integer> map = new HashMap<>();
            for (int j=0; j<num; j++){
                String[] input = br.readLine().split(" ");
                if (map.containsKey(input[1])){
                    map.put(input[1], map.get(input[1])+1);
                } else{
                    map.put(input[1], 1);
                }
            }
            
            int result = 1;
            for (Integer k : map.values()) {
                result *= (k+1);
            }
            bw.write(--result + "\n");

        }

        
        bw.flush();
        bw.close();
        br.close();
    }

    public static int combination(int n, int r){
        if (n == r || r == 0 ){
            return 1;
        }
        if (array[n][r] > 0){
            return array[n][r];
        }
        return array[n][r] = combination(n-1, r-1) + combination(n-1, r);
    }
}