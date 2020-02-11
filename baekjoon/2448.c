#include <stdio.h>

int main(){
    int i,j,k;
    int num;

    scanf("%d",&num);

    for(i=0;i<num;i++){
        for(j=num-i-1;j>0;j--){
            printf(" ");
        }
        printf("*");
        printf("\n");
    }
    return 0;
}
