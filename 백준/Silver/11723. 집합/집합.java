import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
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
        
        int m = Integer.parseInt(br.readLine());
        set = new HashSet<>();
        
        for (int i=0; i<m; i++){
            String[] input = br.readLine().split(" ");
            
            String command = input[0];
            if (command.equals("all")){
                set = new HashSet<>();
                for (int j=1; j<=20; j++){
                    set.add(j);
                }
                continue;
            } else if (command.equals("empty")){
                set = new HashSet<>();
                continue;
            }

            int value = Integer.parseInt(input[1]);
            if (command.equals("add")){
                set.add(value);
            } else if (command.equals("remove")){
                set.remove(value);
            } else if (command.equals("check")){
                if (findVal(value)){
                    bw.write(1 + "\n");
                } else{
                    bw.write(0 + "\n");
                }
            } else if (command.equals("toggle")){
                if (findVal(value)){
                    set.remove(value);
                } else{
                    set.add(value);
                }
            }
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