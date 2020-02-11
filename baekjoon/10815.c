#include <stdio.h>

int main(){
    int N,M,num,flag = 0,i;
    scanf("%d",&N);
    int len = N;
    int arr[N];

    while(N--){
        scanf("%d",&arr[N]);
    }
    scanf("%d",&M);
    while(M--){
        scanf("%d",&num);
        for(i=0;i<len;i++){
            if(num == arr[i]){
                printf("1 ");
                flag = 1;
                break;
            }
        }
        if(flag == 0){
            printf("0 ");
        }
        flag = 0;
    }
    return 0;
}
