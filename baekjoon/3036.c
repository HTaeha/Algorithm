#include <stdio.h>

int main(){
    int N;
    int result1;
    int min,i;
    int first,other;

    scanf("%d",&N);
    N--;
    scanf("%d",&first);
    while(N--){
        scanf("%d",&other);
        if(first<other){
            min = first;
        }else{
            min = other;
        }
        for(i=min;i>=1;i--){
            if(first%i == 0 && other%i == 0){
                result1 = i;
                break;
            }
        }
        printf("%d/%d\n",first/result1,other/result1);
    }
    return 0;
}
