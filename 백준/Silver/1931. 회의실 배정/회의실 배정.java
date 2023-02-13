import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayList;
import java.util.Collection;
import java.util.Collections;
import java.util.Comparator;

class Pair{
    int y;
    int x;
    
    public Pair(int y, int x){
        this.y = y;
        this.x = x;
    }
}

public class Main{

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        
        int n = Integer.parseInt(br.readLine());
        ArrayList<Pair> list = new ArrayList<>();
        int min = Integer.MAX_VALUE;
        int max = Integer.MIN_VALUE;
        for (int i=0; i<n; i++){
            String[] input = br.readLine().split(" ");
            int start = Integer.parseInt(input[0]);
            int end = Integer.parseInt(input[1]);
            if (start < min){
                min = start;
            }
            if (start > max){
                max = start;
            }
            list.add(new Pair(start, end));
        }
        
        Comparator<Pair> comparator = new Comparator<>() {
            
            @Override
            public int compare(Pair a, Pair b){
                if (a.x != b.x){
                    return a.x-b.x;
                }
                return a.y - b.y;
            }
        };

        Collections.sort(list, comparator);
        // for (Pair node : list){
        //     System.out.print(node.x + " ");
        // }

        int result = 1;
        int prev = list.get(0).x;
        for (int i=1; i<n; i++){
            Pair tmp = list.get(i);
            if (tmp.y >= prev){
                prev = tmp.x;
                result++;
            }
        }

        bw.write(result + "\n");

        bw.flush();
        bw.close();
        br.close();    
    }
    
    public static void printArray(int[][] tmp){
        StringBuilder sb = new StringBuilder();
        for (int i=0; i<tmp.length; i++){
            for (int j=0; j<tmp[i].length; j++){
                sb.append(tmp[i][j]);
            }
            sb.append("\n");
        }
        System.out.println(sb);
    }
}