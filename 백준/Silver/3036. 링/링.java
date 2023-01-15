import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Arrays;


public class Main{
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        
        int n = Integer.parseInt(br.readLine());
        String[] read = br.readLine().split(" ");
        int[] input = new int[n];
        for (int i=0; i<n ; i++){
            input[i] = Integer.parseInt(read[i]);
        }
        
        int first = input[0];
        for (int i=1; i<n; i++){
            int num = gcd(first, input[i]);
            bw.write(first/num+"/" + input[i]/num + "\n");
        }

        
        bw.flush();
        bw.close();
        br.close();
    }

    public static int gcd(int a, int b){
        if (a%b == 0){
            return b;
        }
        return gcd(b, a%b);
    }
}