import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.text.Format;
import java.util.Arrays;
import java.io.*;

public class Main{
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        
        String query = br.readLine();
        int tcase = Integer.parseInt(br.readLine());
        
        for (int i=0; i < tcase; i++){
            String[] input = br.readLine().split(" ");
            String str = query.substring(Integer.parseInt(input[1]), Integer.parseInt(input[2])+1);
            bw.write(countString(str, input[0])+"\n");
        }
        
        bw.flush();
        bw.close();
        br.close();    
    }

    public static int countString(String value, String alpha){
        char tmp = alpha.charAt(0);
        // System.out.println(value);
        int result = 0;
        for (char i : value.toCharArray()){
            if (tmp == i){
                result++;
            }
        }
        return result;
    }
}