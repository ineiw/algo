#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

// 파라미터로 주어지는 문자열은 const로 주어집니다. 변경하려면 문자열을 복사해서 사용하세요.
int getPalindromeLen(const char* s,int idx,int sLen);
int max(int a,int b);

int solution(const char* s) {
    int answer = 0;
    int maxCnt = 0;
    
    for(int i=0;i<strlen(s);i++){
        maxCnt = max(maxCnt,getPalindromeLen(s,i,strlen(s)));
    }
    answer = maxCnt;
    return answer;
}

int getPalindromeLen(const char * s,int idx,int sLen){
    int res = 1;
    int res2 = 0;
    for (int i=1;i<=idx;i++){
        if(idx+i > sLen)
            break;
        if(s[idx-i] == s[idx+i])
            res +=2;
        else
            break;
    }
    
    for (int i=1;i<=idx;i++){
        if(idx+i-1 > sLen)
            break;
        if(s[idx-i] == s[idx+i-1])
            res2 +=2;
        else
            break;
    }
    
    return max(res,res2);
}

int max(int a,int b){
    if (a > b)
        return a;
    else
        return b;
}