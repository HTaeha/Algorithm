#include <stdio.h>

int main(){
    int num;
    int i;
    int left, right;

    scanf("%d",&num);
    i=2;

    if(num==1){
        printf("1/1");
        return 0;
    }
    while(1){
        if((num<=((i*i)+i)/2) && (num > ((i*i)-i)/2)){
            if(i%2 == 0){
                left = num-((i*i)/2 - i/2);
                right = i+1 - left;
                printf("%d/%d",left,right);
            }else{
                right = num-((i*i)/2 - i/2);
                left = i+1 - right;
                printf("%d/%d",left,right);
            }
            break;
        }
        i++;
    }

    return 0;
}
