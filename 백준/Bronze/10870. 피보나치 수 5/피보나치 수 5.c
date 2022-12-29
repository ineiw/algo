#include <stdio.h>

int rec(int a,int b,int depth);

int main(){
    int n;
    scanf("%d",&n);
    
    printf("%d",rec(0,1,n));
    return 0;
}

int rec(int a,int b,int depth){
    if(depth == 0){
        return a;
    }
    return rec(b,b+a,depth-1);
}