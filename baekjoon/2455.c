#include <stdio.h>

int main(){
    int in[4];
    int out[4];
    int i;
    int max;
    int result[3];

    for(i=0;i<4;i++){
        scanf("%d",&out[i]);
        scanf("%d",&in[i]);
    }

    result[0] = in[0];
    result[1] = result[0] - out[1] + in[1];
    result[2] = result[1] - out[2] + in[2];
    max = result[0];
    for(i=0;i<3;i++){
        if(max<result[i]){
            max = result[i];
        }
    }

    printf("%d",max);

    return 0;
}
