import java.util.ArrayList;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int day = scanner.nextInt();
        ArrayList<Integer> cars = new ArrayList<Integer>();
        int cnt = 0;

        for (int i=0; i<5;i++){
            cars.add(scanner.nextInt());
        }

        for (Integer car: cars){
            if (car == day){
                cnt += 1;
            }
        }
        System.out.println(cnt);
    }
}
