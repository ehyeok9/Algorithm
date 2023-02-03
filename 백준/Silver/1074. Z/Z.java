import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

class Pair{
    int first;
    int second;

    public Pair(int first, int second){
        this.first = first;
        this.second = second;
    }
}

public class Main{
    static int n;
    static int r;
    static int c;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        
        String[] input = br.readLine().split(" ");
        n = Integer.parseInt(input[0]);
        r = Integer.parseInt(input[1]);
        c = Integer.parseInt(input[2]);
        int powVal = (int)Math.pow(2, n);
        conquer(1, 1, powVal, 0);

        bw.flush();
        bw.close();
        br.close();    
    }

    public static void conquer(int y, int x, int n, int value){
        int range = n/2;
        // System.out.println(String.format("y=%d, x=%d, n=%d", y, x, n));
        if ((c+1 < x || x+n-1 < c+1) || (r+1 < y || y+n-1 < r+1)){
            return;
        }
        if (y == r+1 && x == c+1){
            System.out.println(value);
            return;
        }
        if (n == 0){
            return;
        }

        int stance = (int)Math.pow(n/2, 2);
        conquer(y, x, range, value);
        conquer(y, x+range, range, value+stance);
        conquer(y+range, x, range, value+stance*2);
        conquer(y+range, x+range, range, value+stance*3);
    }
    
    public static void printArray(int[][] tmp){
        StringBuilder sb = new StringBuilder();
        for (int i=0; i<tmp.length; i++){
            for (int j=0; j< tmp[i].length; j++){
                sb.append(tmp[i][j] + " ");
            }
            sb.append("\n");
        }
        System.out.println(sb);
    }
}