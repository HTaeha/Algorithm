#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(){
    int n,t;
    int i,j;
    int arr[200000];
    int index=0;
    int max=0;
    int time;
    unsigned long long temp = 0;
    unsigned long long result;
    int result_t;
    int temp_arr;

    scanf("%d",&n);

    while(n--){
        scanf("%d",&arr[index++]);
        if(max < arr[index-1]){
            max = arr[index-1];
        }
    }
    scanf("%d",&t);
    
    for(i=1;i<=max;i++){
        time = t + i;
        for(j=0;j<index;j++){
            if(arr[j] <= i){
                temp += time;
                continue;
            }else{
                temp_arr = arr[j];
                while(temp_arr > 0){
                    temp_arr -= i;
                    temp += time;
                }
            }
        }
        if(i == 1){
            result = temp;
            result_t = 1;
        }else if(result > temp){
            result = temp;
            result_t = i;
        }else if(result == temp){
            if(result_t > i){
                result_t = i;
            }
        }
        temp = 0;
    }

    printf("%llu %d",result, result_t);

    return 0;
}
