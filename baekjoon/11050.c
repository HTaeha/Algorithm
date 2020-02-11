#include <stdio.h>

int main(){
    int n,k;
    int res=1;
    int res1=1,res2=1;
    scanf("%d %d",&n,&k);

    while(k != 0){
        res1 = res1*n;
        res2 = res2*k;
        n--;
        k--;
    }
    res = res1/res2;
    printf("%d",res);
    return 0;
}
