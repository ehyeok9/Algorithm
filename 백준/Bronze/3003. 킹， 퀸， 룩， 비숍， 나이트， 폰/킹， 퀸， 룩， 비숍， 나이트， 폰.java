import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class Main{    
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        
        String[] piece = br.readLine().split(" ");
        int[] right = {1,1,2,2,2,8};

        for (int i=0; i < piece.length; i++){
            bw.write(right[i] - Integer.parseInt(piece[i]) + " ");
        }

        bw.flush();
        bw.close();
        br.close();
    }
}