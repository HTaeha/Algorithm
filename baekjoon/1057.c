#include <stdio.h>

int main(){
    int N, n1,n2;
    int count=1;
    scanf("%d %d %d",&N,&n1,&n2);

    while(N = (N+1)/2){
        if(n1<n2){
            if(n1%2 == 1 && n2 == n1+1){
                printf("%d",count);
                return 0;
            }
        }else{
            if(n2%2 == 1 && n1 == n2+1){
                printf("%d",count);
                return 0;
            }
        }
        if(n1%2 == 0){
            n1 = n1/2;
        }else{
            n1 = (n1+1)/2;
        }
        if(n2%2 == 0){
            n2 = n2/2;
        }else{
            n2 = (n2+1)/2;
        }
        count++;
    }
    printf("-1");
    return 0;
}
