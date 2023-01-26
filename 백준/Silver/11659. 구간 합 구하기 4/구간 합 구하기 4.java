import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.text.Format;
import java.util.Arrays;
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
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        
        String[] num = br.readLine().split(" ");
        int arrayN = Integer.parseInt(num[0]);

        String[] input = br.readLine().split(" ");
        int[] value = new int[arrayN+1];
        int[] sumVal = new int[arrayN+1];
        for (int i=1; i <= arrayN; i++){
            value[i] = Integer.parseInt(input[i-1]);
            sumVal[i] = sumVal[i-1] + value[i];
        }
        input = null;

        int tcase = Integer.parseInt(num[1]);
        for (int i=0; i< tcase; i++){
            String[] tmp = br.readLine().split(" ");
            int b = Integer.parseInt(tmp[1]);
            int a = Integer.parseInt(tmp[0]);
            bw.write(sumVal[b]- sumVal[a-1] +"\n");
        }
        bw.flush();
        bw.close();
        br.close();    
    }
}