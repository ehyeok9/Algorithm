import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class Main{
    static char[][] array;
    static int adding;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        
        int n = Integer.parseInt(br.readLine());
        array = new char[n+1][n+1];
        
        adding = n;
        fillArray(1, n, 1, n, n);
        printArray(array);
        
        bw.flush();
        bw.close();
        br.close();
    }

    static void fillArray(int rowS, int rowE, int colS, int colE, int len){
        if (len == 3){
            for (int i=rowS; i<= rowE; i++){
                for (int j=colS; j <= colE; j++){
                    if (i == (rowS+1) && j == (colS+1)){
                        array[i][j] = ' ';
                    }else {
                        array[i][j] = '*';
                    }
                }
            }
            return;
        }

        int num = len/3;
        
        for (int i=0; i < 3; i++){
            fillArray(rowS, rowE-num*2, colS+num*i, colE-(num*(2-i)), num);
            if (i == 1){
                for (int x=rowS+num; x <= rowE-num; x++){
                    for (int y=colS+num*i; y <= colE-(num*(2-i)); y++){
                        array[x][y] = ' ';
                    }
                }
            } else {
                fillArray(rowS + num, rowE-num, colS+num*i, colE-(num*(2-i)), num);
            }
            fillArray(rowS + num*2, rowE, colS+num*i, colE-(num*(2-i)), num);
        }

        
    }

    public static void printArray(char[][] arr){
        StringBuilder sb = new StringBuilder();

        for (int i = 1; i < arr.length; i++) {
            for (int j = 1; j < arr[i].length; j++) {
                sb.append(arr[i][j]);
            }
            sb.append('\n');
        }
        System.out.println(sb);
        
    }
}