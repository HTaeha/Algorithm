#include <stdio.h>
#include <stdlib.h>

int main(){
    int * num = (int *)malloc(sizeof(int)*5);
    int su,i;
    int index=0;
    int len =5;
    while(1){
        scanf("%d",&num[index]);
        index++;
        if(num[index-1]==-1){
            break;
        }
        if(index == len){
            num = (int *)realloc(num,sizeof(int)*(len+3));
            len += 3;
        }
    }
    for(i=0;i<index;i++){
        printf("%d",num[i]);
    }
    free(num);
    return 0;
}
