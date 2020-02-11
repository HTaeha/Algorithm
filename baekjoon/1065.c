#include <stdio.h>

int main(){
    int num,i;
    int result=0;
    int a,b,c;

    scanf("%d",&num);

    for(i=1;i<=num;i++){
        if(i<100){
            result++;
        }else if(i<1000){
            a = i%10;
            b = (i/10)%10;
            c = i/100;
            if(a-b == b-c){
                result++;
            }
        }
    }
    printf("%d\n",result);
    return 0;
}
