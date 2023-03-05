import java.util.*;

class Solution {
    public int[] solution(String today, String[] terms, String[] privacies) {        
        HashMap<String, Integer> tmap = new HashMap<>();
        for (int i=0; i<terms.length; i++){
            String[] tmp = terms[i].split(" ");
            tmap.put(tmp[0], Integer.parseInt(tmp[1]));
        }
        
        String[] str = today.split("[.]");
        int tyear = Integer.parseInt(str[0]);
        int tmonth = Integer.parseInt(str[1]);
        int tday = Integer.parseInt(str[2]);
        // System.out.println(String.format("%d %d %d", tyear, tmonth, tday));
        ArrayList<Integer> list = new ArrayList<>();
        for (int i=0; i<privacies.length; i++){
            String[] tmp = privacies[i].split(" ");
            int pmonth = tmap.get(tmp[1]);
            
            String[] date = tmp[0].split("[.]");
            int year = Integer.parseInt(date[0]);
            int month = Integer.parseInt(date[1]);
            int day = Integer.parseInt(date[2]);
            
            month += pmonth;
            if (month > 12){
                if (month%12 == 0){
                    year += month/12-1;
                    month = 12;
                } else {
                    year += month/12;
                    month %= 12;
                }
            }
            // System.out.println(String.format("%d %d %d",year, month, day));
            if (year < tyear) {
                list.add(i+1);
            } else if (year == tyear){
                if (month < tmonth){
                    list.add(i+1);
                } else if (month == tmonth){
                    if (day <= tday){
                        list.add(i+1);
                    }
                }
            }
        }
        Collections.sort(list);
        int[] answer = new int[list.size()];
        for (int i=0; i<answer.length; i++){
            answer[i] = list.get(i);
        }
        return answer;
    }
}