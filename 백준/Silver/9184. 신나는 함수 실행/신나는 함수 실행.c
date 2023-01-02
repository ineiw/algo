#include <stdio.h>

int w(int a, int b, int c){
    printf("%d %d %d\n",a,b,c);
    if(a<=0 || b<=0 || c<=0) return 1;
    else if(a>20 || b>20 || c>20) return w(20,20,20);
    else if(a<b && b<c) return w(a,b,c-1)+w(a,b-1,c-1)-w(a,b-1,c);
    else return w(a-1,b,c)+w(a-1,b-1,c)+w(a-1,b,c-1)-w(a-1,b-1,c-1);
}

int w2(int a, int b, int c){
    int dp[51][51][51];

    if(a<=0 || b<=0 || c<=0) return 1;
    else if(a>20 || b>20 || c>20) return w2(20,20,20);

    for(int i=0;i<=a;i++){
        for(int j=0;j<=b;j++){
            for(int k=0;k<=c;k++){
                if(i<=0 || j<=0 || k<=0) dp[i][j][k] = 1;
                else if(i>20 || j>20 || k>20) dp[i][j][k] = dp[20][20][20];
                else if(i<j && j<k) dp[i][j][k] = dp[i][j][k-1]+dp[i][j-1][k-1]-dp[i][j-1][k];
                else dp[i][j][k] = dp[i-1][j][k]+dp[i-1][j-1][k]+dp[i-1][j][k-1]-dp[i-1][j-1][k-1];
            }
        }
    }

    return dp[a][b][c];
}

int main(){
    int a,b,c,res;

    while(1){
        scanf("%d %d %d",&a,&b,&c);
        if(a == -1 && b == -1 && c == -1) break;
        res = w2(a,b,c);

        printf("w(%d, %d, %d) = ",a,b,c);
        printf("%d\n",res);
    }

    return 0;
}