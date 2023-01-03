import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class Main{    

    public static int construct(int a) {
        int num = a;
        while(a > 0){
            int last = a%10;
            num += last;
            a /= 10;
        }
        return num;
    }
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int[] count = new int[10001];
        
        for (int i=1; i< 10001; i++) {
            int num = construct(i);
            if (num <= 10000) {
                count[num] += 1;
            }
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