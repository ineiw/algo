#include <stdio.h>

int main(){

    int n,dp[1000000];
    scanf("%d", &n);
    dp[0]=1;
    dp[1]=2;
    for(int i=2;i<n;i++){
        dp[i]=(dp[i-1]+dp[i-2])%15746;
    }
    printf("%d", dp[n-1]%15746);
    return 0;
}