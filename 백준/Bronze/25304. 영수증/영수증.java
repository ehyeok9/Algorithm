import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class Main{    
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        
        Integer X = Integer.parseInt(br.readLine());
        Integer n = Integer.parseInt(br.readLine());
        int result = 0;

        for (int i =0; i < n ; i++) {
            String[] input = br.readLine().split(" ");
            int price = Integer.parseInt(input[0]);
            int num = Integer.parseInt(input[1]);

            result += (price*num);
        }

        if (X - result == 0){
            bw.write("Yes");
        } else{
            bw.write("No");
        }
        bw.flush();
        bw.close();
        br.close();
    }
}