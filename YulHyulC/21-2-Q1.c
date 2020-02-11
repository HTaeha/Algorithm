#include <stdio.h>
#include <stdlib.h>

int main(){
    char arr[100]={0,};
    int i;
    int result=0;

    scanf("%s",arr);

    for(i=0;i<50;i++){
        printf("arr[%d] = %c\n",i,arr[i]);
    }
    i=0;
    while(arr[i]!=0){
        
        if(arr[i]>=48 && arr[i]<=57){
            result = result + (int)(arr[i]-'0');
            printf("i:%d,result:%d\n",i,result);
        }

        i++;
    }
    printf("%d\n",result);

    return 0;
}

