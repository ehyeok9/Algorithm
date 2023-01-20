import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.text.Format;
import java.io.*;

public class Main{
    static int[][][] result = new int[102][102][102];
    public static void main(String[] args) throws IOException {
        try {
            BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
            BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
            StringBuilder sb = new StringBuilder();
            while (true) {
                String[] input = br.readLine().split(" ");
                int[] natural = new int[3];
                for (int i=0; i< 3; i++){
                    natural[i] = Integer.parseInt(input[i]);
                }
                if (natural[0] == -1 && natural[1] == -1 && natural[2] == -1){
                    break;
                }
                int a = natural[0];
                int b = natural[1];
                int c = natural[2];
                
                sb.append(String.format("w(%d, %d, %d) = %d\n", a, b, c, w(a,b,c)));
            }

            System.out.print(sb);
            bw.flush();
            bw.close();
            br.close();   
        } catch (Exception e) {
        }
    }

    public static int w(int a, int b, int c){
        if (result[a+50][b+50][c+50] != 0){
            return result[a+50][b+50][c+50];
        }
        if (a <= 0 || b <= 0 || c <= 0){
            return 1;
        }

        if (a > 20 || b > 20 || c > 20){
            return result[a+50][b+50][c+50] = w(20, 20, 20);   
        }

        if (a < b && b < c){
            return result[a+50][b+50][c+50] = w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c);
        }
        return result[a+50][b+50][c+50] = w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1);
    }

}