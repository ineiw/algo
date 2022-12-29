#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int recursion(const char *s,int l,int r,int cnt){
    if(l >= r) return -cnt;
    else if (s[l] != s[r]) return cnt;
    else return recursion(s,l+1,r-1,cnt+1);
}

int isPalindrome(const char *s){
    return recursion(s, 0, strlen(s)-1,1);
}

int main(){
    int n;
    char * s = malloc(1001 * sizeof(char));
    scanf("%d",&n);
    for (int i=0;i<n;i++){
        
        int cnt,flag = 0;
        scanf("%s",s);
        
        cnt = isPalindrome(s);
        if(cnt < 0) {
            flag = 1;
            cnt=-cnt;
        }

        printf("%d %d\n",flag,cnt);
    }
}