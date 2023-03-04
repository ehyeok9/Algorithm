class Solution {
    public int[] solution(String[] wallpaper) {
        int lux = Integer.MAX_VALUE; int luy = Integer.MAX_VALUE;
        int rdx = -1; int rdy = -1;
        
        for (int i=0; i<wallpaper.length;i++){
            String str = wallpaper[i];
            for (int j=0; j<str.length(); j++){
                char c = str.charAt(j);
                if (c == '#'){
                    if (i < lux){
                        lux = i;
                    }
                    if (j < luy){
                        luy = j;
                    }
                    if (rdx < i+1){
                        rdx = i+1;
                    }
                    if (rdy < j+1){
                        rdy = j+1;
                    }
                    
                }
            }
        }
        int[] answer = {lux, luy, rdx, rdy};
        return answer;
    }
}