#include <stdio.h>

int main(){
    int T;
    int n1,n2;
    int result,max;

    scanf("%d",&T);

    while(T--){
        scanf("%d %d",&n1,&n2);

        if(n1<n2){
            max = result = n2;
        }else{
            max = result = n1;
        }
        while(1){
            if(result%n2 == 0 && result%n1 == 0){
                printf("%d\n",result);
                break;
            }
            result += max;
        }
    }
    return 0;
}
