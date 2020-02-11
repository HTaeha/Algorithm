#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(){
    int n,m;
    int arr[100000];
    int index=0;
    int i,j,k;
    int key;
    int count = 0;
    int start;
    int flag = 0;
    int answer=0;

    scanf("%d %d", &n, &m);
    
    while(n--){
        scanf("%d", &arr[index++]);
    }

    start = 0;
    for(i=0;i<index;i++){
        for(j=i;j<index;j++){
            for(k=i;k<j;k++){
                if(arr[k] == arr[j]){
                    if(answer < count){
                        answer = count;
                    }
                    flag = 1;
                    break;
                }
            }
            if(flag == 1){
                break;
            }
            count++;
        }
        if(flag){
            count = 0;
            flag = 0;
            continue;
        }
    }
    printf("%d",answer);
    return 0;
}
