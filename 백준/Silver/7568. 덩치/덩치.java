import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Deque;
import java.util.Stack;

class Pair {
    int first; 
    int second;

    public Pair(int first, int second) {
        this.first = first;
        this.second = second;
    }
}
public class Main{
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        
        int n = Integer.parseInt(br.readLine());
        ArrayList<Pair> list = new ArrayList<>();
        for (int i=0; i<n; i++) {
            String[] input = br.readLine().split(" ");
            list.add(new Pair(Integer.parseInt(input[0]), Integer.parseInt(input[1])));
        }

        int[] result = new int[n];
        for (int i=0; i<list.size(); i++){
            int cnt = 0;
            Pair taget = list.get(i);
            for (int j=0; j< list.size(); j++){
                if (list.get(j).first > taget.first && list.get(j).second > taget.second){
                    cnt++;
                }
            }
            result[i] = cnt+1;
        }
        
        for (int i=0; i< result.length; i++){
            bw.write(result[i] + " ");
        }



        bw.flush();
        bw.close();
        br.close();
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