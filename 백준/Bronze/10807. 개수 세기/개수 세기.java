import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class Main{    
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        
        int N = Integer.parseInt(br.readLine());
        int[] base = new int[401];

        String[] temp = br.readLine().split(" ");
        for (int i=0; i < temp.length; i++) {
            int num = Integer.parseInt(temp[i]);
            if (num < 0){
                num += 210;
            }
            base[num] += 1;
        }

        int result = Integer.parseInt(br.readLine());
        if (result < 0){
            result += 210;
        }
        bw.write(base[result] + "\n");


        bw.flush();
        bw.close();
        br.close();
    }
}