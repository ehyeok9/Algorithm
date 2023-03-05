class Solution {
    public int solution(String t, String p) {
        int answer = 0;
        long pval = Long.parseLong(p);
        int len = t.length()-p.length()+1;
        for (int i=0; i<len; i++){
            long num = Long.parseLong(t.substring(i, i+p.length()));
            System.out.println(num);
            if (num <= pval) answer++;
        }
        return answer;
    }
}