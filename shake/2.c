#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int compare(const void *a, const void *b){
    double* n1=(double*)a;
    double* n2=(double*)b;

    if(*n1 > *n2){
        return 1;
    }else if(*n1 == *n2){
        return 0;
    }else{
        return -1;
    }
}
int main(){
    int n,k;
    int Pi;
    int x,y;
    double answer = 0;
    double temp;
    double* res;
    int index = 0;
    int i,j;
    int num;

    scanf("%d %d",&n,&k);

    res = (double*)malloc(sizeof(double)*n);
    num = n;
    while(n--){
        scanf("%d", &Pi);
        while(Pi--){
            scanf("%d %d", &x, &y);
            temp = x*x + y*y;
            if(answer < temp){
                answer = temp;
            }
        }
        res[index++] = answer;
        answer = 0;
    }

    qsort(res, num, sizeof(double), compare);
/*
    for(i=0;i<index;i++){
        printf("res[%d] : %f\n",i,res[i]);
    }*/
    printf("%.2f", res[k-1]);
    free(res);
    return 0;
}
