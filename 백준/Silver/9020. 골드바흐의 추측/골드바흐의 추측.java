import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayList;


class Pair{
    int first;
    int second;

    public Pair(int first, int second){
        this.first = first;
        this.second = second;
    }
}

public class Main{    
    static int[] gold = new int[10001];
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        
        int test = Integer.parseInt(br.readLine());
        eratos();

        for (int i=0; i< test; i++){
            int num = Integer.parseInt(br.readLine());
            ArrayList<Pair> array = new ArrayList<>();
            Pair result = new Pair(-1, -1);
            for (int j=2; j<=num/2; j++){
                if (gold[j] == 0 && gold[num -j] == 0){
                    result = new Pair(j, num-j);
                }
            }
            bw.write(result.first + " " + result.second + "\n");
        }

        bw.flush();
        bw.close();
        br.close();
    }

    public static Pair getMini(ArrayList<Pair> array){
        Pair mini = array.get(0);
        int value = Math.abs(mini.first - mini.second);
        
        for (int i=1; i<array.size(); i++){
            Pair temp = array.get(i);
            int tval = Math.abs(temp.first - temp.second);
            if (tval < value){
                mini = temp;
            }
        }

        return mini;
    }

    public static void eratos(){
        gold[1] = 1;

        for (int i=2; (i*i)<= 10000; i++){
            if (sosu(i)){
                for (int j= i*2; j <= 10000; j+=i){
                    gold[j] = 1;
                }
            }
        }
    }

    public static boolean sosu(int num){
        if (num == 1){
            return false;
        }
        for (int i=2; i< num; i++){
            if (num%i == 0){
                return false;
            }
        }
        return true;
    }

    public static void printArray(int[][] arr){
        for (int i = 0; i < arr.length; i++) {
            int[] inArr = arr[i];
            for (int j = 0; j < inArr.length; j++) {
                System.out.print(inArr[j] + " ");
            }
            System.out.println();
        }
    }
}