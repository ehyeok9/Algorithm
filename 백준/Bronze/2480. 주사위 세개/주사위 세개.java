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
        int num1 = Integer.parseInt(input[0]);
        int num2 = Integer.parseInt(input[1]);
        int num3 = Integer.parseInt(input[2]);

        if ((num1 - num2) == 0 && (num2 - num3) == 0 && (num3 - num1) == 0){
            bw.write(10000 + num1*1000+ "\n");    
        } else if ((num1 - num2) == 0) {
            bw.write(1000 + num1*100 + "\n");    
        } else if ((num2 - num3) == 0) {
            bw.write(1000 + num2*100 + "\n");    
        } else if ((num3 - num1) == 0) {
            bw.write(1000 + num3*100 + "\n");    
        } else {
            int max = -1;
            if (num1 >= num2) {
                if (num1 >= num3){
                    max = num1;
                } else{
                    max = num3;
                }
            } else if (num2 >= num3){
                max = num2;
            } else{
                max = num3;
            }
            bw.write(max*100 + "\n");
        }

        bw.flush();
        bw.close();
        br.close();
    }
}