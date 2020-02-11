#include <stdio.h>

int memo[12] = {1,2,4,};
int cond(int num){
    if(num == 1){
        return 1;
    }else if(num==2){
        return 2;
    }else if(num==3){
        return 4;
    }else if(memo[num]){
        return memo[num];
    }else{
        return memo[num] = cond(num-1) + cond(num-2) + cond(num-3);
    }
}
int main(){
    int T,n;
    scanf("%d",&T);

    while(T--){
        scanf("%d",&n);
        printf("%d\n",cond(n));
    }
    return 0;
}
