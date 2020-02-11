#include <stdio.h>

int main(){
    int N;
    scanf("%d",&N);
    int arr[N];
    int len = N;
    int count = 0,i,j;
    int standard,res=0;
    while(N--){
        scanf("%d",&arr[len-N-1]);
    }
    for(i=len-1;i>=0;i--){
        standard = arr[i];
        for(j=i-1;j>=0;j--){
            if(standard > arr[j]){
                count++;
                standard = arr[j];
            }
        }
        if(res < count){
            res = count;
        }
        count=0;
    }
    printf("%d",res);
    return 0;
}
