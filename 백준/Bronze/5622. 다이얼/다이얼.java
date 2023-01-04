import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class Main{    

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        
        String str = br.readLine();
        String[] range = {"ABC", "DEF", "GHI", "JKL", "MNO", "PQRS", "TUV", "WXYZ"};
        int num = 0;
        
        for (int i=0; i < str.length(); i++){
            char strIdx = str.charAt(i);
            for (int j=0; j<range.length; j++){
                for (int k=0; k < range[j].length(); k++){
                    if (strIdx == range[j].charAt(k)){
                        num += (2 + j + 1);
                    }
                }
            }
        }

        bw.write(num + "\n");
        bw.flush();
        bw.close();
        br.close();
    }
}