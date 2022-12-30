import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class Main{    
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        
        int cycle = 0;
        int input = Integer.parseInt(br.readLine());
        int temp = input;
        
        do {
            int left, right;

            if (temp < 10){
                left = 0;
                right = temp;
            } else{
                right = temp%10;
                temp -= right;
                left = temp/10;
            }

            temp = left + right;
            temp = (right*10) + (temp%10);
            cycle += 1;

        } while (temp != input);

        bw.write(cycle + "\n");

        bw.flush();
        bw.close();
        br.close();
    }
}