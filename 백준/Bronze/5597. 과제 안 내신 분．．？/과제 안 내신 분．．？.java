import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class Main{    
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int[] count = new int[31];

        for (int i=0; i<28; i++) {
            int n = Integer.parseInt(br.readLine());
            count[n] += 1;
        }

        for (int i=1; i<count.length; i++){
            if (count[i] == 0){
                bw.write(i + "\n");
            }
        }
        
        bw.flush();
        bw.close();
        br.close();
    }
}