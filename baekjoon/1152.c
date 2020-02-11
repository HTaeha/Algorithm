#include <stdio.h>
#include <string.h>

int main(){
    char arr[1000000];
    int i;
    int count=1;

    fgets(arr, sizeof(arr),stdin);
    arr[strlen(arr)-1]=0;

    for(i=0;i<1000000;i++){
        if(arr[i]==' '){
            if(i==0 || i==strlen(arr)-1){
                continue;
            }
            count++;
        }else if(arr[i]==0){
            break;
        }
    
    }
    printf("%d\n",count);

    return 0;
}
