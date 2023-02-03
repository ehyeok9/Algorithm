import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.HashMap;
import java.util.HashSet;
import java.util.Iterator;

class Pair{
    int first;
    int second;

    public Pair(int first, int second){
        this.first = first;
        this.second = second;
    }
}

public class Main{
    static HashSet<Integer> set;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        
        String[] input = br.readLine().split(" ");
        int n = Integer.parseInt(input[0]);
        int m = Integer.parseInt(input[1]);

        HashMap<String, String> map = new HashMap<>();
        for (int i=0; i<n; i++){
            String[] line = br.readLine().split(" ");
            map.put(line[0], line[1]);
        }

        for (int i=0; i<m; i++){
            String id = br.readLine();
            bw.write(map.get(id) + "\n");
        }
        bw.flush();
        bw.close();
        br.close();    
    }
    
    public static boolean findVal(int value){
        for (int i : set){
            if (i == value){
                return true;
            }
        }
        return false;
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