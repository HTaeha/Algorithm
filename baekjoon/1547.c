#include <stdio.h>

int main(){
    int a, b;
    int M;
    int result=1;

    scanf("%d",&M);

    while(M--){
        scanf("%d %d",&a,&b);
        if(a == result){
            result = b;
        }else if(b == result){
            result = a;
        }
    }
    printf("%d",result);
    return 0;
}
