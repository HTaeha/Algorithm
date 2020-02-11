#include <stdio.h>

int main(){
    int X;
    int result=1;
    int wood = 64;
    int min_wood = 64;

    scanf("%d",&X);

    while(1){
        min_wood /= 2;
        if(wood == X){
            break;
        }
        if(wood - min_wood >= X){
            wood -= min_wood;
            result--;
        }
        result++;
    }
    printf("%d",result);
    return 0;
}

