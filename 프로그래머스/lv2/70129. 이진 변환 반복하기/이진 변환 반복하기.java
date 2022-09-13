class Solution {
    int cnt = 0;
    int loopCnt = 0;
    public String replace0ToEmpty(String s){
        String res = "";
        for(int i=0;i<s.length();i++){
            if(s.charAt(i) == '0'){
                this.cnt+=1;
                continue;
            }
            res += "1";
        }
        return res;
    }
    public String stringLenToBin(int sLen){
        int dec = sLen;
        String resTring = "";
        while(dec != 0){
            resTring = Integer.toString(dec%2) + resTring;
            dec /= 2;
        }
        return resTring;
    }
    public int[] solution(String s) {
        int[] answer = {0,0};
        
        while(!s.equals("1")){
            this.loopCnt+=1;
            s = replace0ToEmpty(s);
            s = stringLenToBin(s.length());
        }
            
        answer[0] = this.loopCnt;
        answer[1] = this.cnt;
        return answer;
    }
}