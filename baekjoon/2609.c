#include <stdio.h>

int main(){
    int n1,n2;
    int result1, result2,max;
    int min,i;

    scanf("%d %d",&n1,&n2);
    if(n1<n2){
        max = result2 = n2;
        min = n1;
    }else{
        max = result2 = n1;
        min = n2;
    }
    for(i=min;i>=1;i--){
        if(n1%i == 0 && n2%i == 0){
            result1 = i;
            printf("%d\n",result1);
            break;
        }
    }
    while(1){
        if(result2%n2 == 0 && result2%n1 == 0){
            printf("%d\n",result2);
            break;
        }
        result2 += max;
    }
    return 0;
}
