#include <stdio.h>

long long int GCD(long long int x,long long int y);
int main(){
    long long int result=1;
    long long int i;
    long long int n1,n2,min;

    scanf("%lld",&n1);
    scanf("%lld",&n2);

    result = GCD(n1,n2);

    for(i=0;i<result;i++){
        printf("1");
    }

    return 0;
}
long long int GCD(long long int x, long long int y){
    if(x==0){
        return y;
    }else if(y==0){
        return x;
    }
    if(x<y){
        return GCD(x,y%x);
    }else{
        return GCD(x%y,y);
    }
}
