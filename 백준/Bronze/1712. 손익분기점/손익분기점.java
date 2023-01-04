import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class Main{    

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        
        String[] input = br.readLine().split(" ");
        int pix = Integer.parseInt(input[0]);
        int var = Integer.parseInt(input[1]);
        int price = Integer.parseInt(input[2]);

        if (price - var <= 0) {
            bw.write(-1 + "\n");
        } else {
            bw.write((pix/(price - var)+1)+ "\n");
        }

        bw.flush();
        bw.close();
        br.close();
    }
}