#include <stdio.h>

int main(void) {
    int arr[10];
    int i,j,k;
    int n;
    int count = 0;
    int cipher = 0;
    long long int result = 0;
    scanf("%d",&n);
    for(i=0;i<10;i++){
        arr[i] = 0;
    }

    while(1){
        if(n == count){
            result = arr[cipher];
            for(i=cipher-1;i>=0;i--){
                result *= 10;
                result += arr[i];
            }
            printf("%lld",result);
            return 0;
        }

        arr[0]++;

        for(i=0;i<cipher;i++){
            for(j=i+1;j<=cipher;j++){
                if(arr[i] == 10 || arr[i] >= arr[j]){
                    arr[i] = 0;
                    arr[i+1]++;
                    if(arr[i] <= arr[i-1] && i!=0){
                        arr[i] = arr[i-1]+1;
                    }
                    if(arr[i+1] == 10){
                        cipher++;
                        if(cipher == 10){
                            printf("-1");
                            return -1;
                        }
                        arr[i+1] = arr[i]+1;
                        arr[cipher] = arr[cipher-1]+1;
                    }
                }
            }
        }
        if(arr[0] == 10){
            cipher = 1;
            arr[0] = 0;
            arr[1] = 1;
        }
        count++;
    }
}
