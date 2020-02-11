#include <stdio.h>
#include <stdlib.h>

int compare(void *a, void *b);
int main(void) {
    int n,k,i,j;
    long long result=0;

    scanf("%d %d",&n,&k);
    int arr[n+1];
    int temp[k+1];

    for(i=0;i<n;i++){
        scanf("%d",&arr[i]);
    }

    for(i=0;i<n-k+1;i++){
        for(j=0;j<k;j++){
            temp[j]=arr[i+j];
          //  printf("\ttemp[%d] : %d\n",j,temp[j]);
        }
        qsort(temp, k, sizeof(temp[0]),compare);
        for(j=0;j<k;j++){
            printf("\ttemp[%d] : %d\n",j,temp[j]);
        }

        printf("temp[%d] : %d\n",(k+1)/2-1,temp[(k+1)/2-1]);
        result = result + temp[(k+1)/2-1];
    }

    printf("%lld",result);

    return 0;
}
int compare(void *a, void *b){
    if(*(int*)a > *(int*)b){
        return 1;
    }else if(*(int*)a<*(int*)b){
        return -1;
    }else{
        return 0;
    }
}
