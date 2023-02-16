class Solution {
    public int solution(int[][] sizes) {
        int answer = Integer.MAX_VALUE;
        
        int mn = 0;
        int mx = 0;
        for (int i=0; i<sizes.length; i++){
            if (sizes[i][0] > sizes[i][1]){
                if (sizes[i][0] > mx) {
                    mx = sizes[i][0];
                }
                if (sizes[i][1] > mn){
                    mn = sizes[i][1];
                }
            } else {
                if (sizes[i][1] > mx) {
                    mx = sizes[i][1];
                }
                if (sizes[i][0] > mn){
                    mn = sizes[i][0];
                }
            }
        }
        answer = mn*mx;
        return answer;
    }
}