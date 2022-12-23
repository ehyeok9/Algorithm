import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;
import java.util.List;


public class Main{    
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        
        int num = Integer.parseInt(br.readLine());
        List<ArrayList<Integer>> list = new ArrayList<ArrayList<Integer>>();

        for (int i=0; i<num; i++){
            String[] line = br.readLine().split(" ");
            int x = Integer.parseInt(line[0]);
            int y = Integer.parseInt(line[1]);
            ArrayList<Integer> temp = new ArrayList<>();
            
            temp.add(x);
            temp.add(y);
            list.add(temp);
        }

        Collections.sort(list, new Comparator<ArrayList<Integer>>() {

            @Override
            public int compare(ArrayList<Integer> o1, ArrayList<Integer> o2) {
                if (o2.get(1) > o1.get(1)){
                    return -1;
                } else if (o2.get(1) < o1.get(1)){
                    return 1;
                } else {
                    if (o2.get(0) > o1.get(0)){
                        return -1;
                    } else{
                        return 1;
                    }
                }
            }
            
        }) ;

        for (ArrayList<Integer> value : list){
            bw.write(value.get(0) + " " + value.get(1) + "\n");
        }

        bw.close();
        br.close();
    }
}