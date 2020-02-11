#include <stdio.h>

const long long mod = 1000000007;
long long memo[4000000]={1,1,};
long long fac(long long num){
    if(num==1 || num==0){
        return 1;
    }
    if(memo[num] != 0){
        return memo[num]%mod;
    }

    return memo[num] = num*fac(num-1)%mod;
}
long long mul(long long a,long long b){
    if(b==0){
        return 1;
    }else if(b==1){
        return a%mod;
    }else if(b%2==0){
        return mul((a*a)%mod,b/2)%mod;
    }else if(b%2==1){
        return a*mul((a*a)%mod,(b-1)/2)%mod;
    }
}
int main(){
    long long n, k,ans1,ans2;

    scanf("%lld %lld",&n,&k);
    ans1 = fac(n)%mod;
    ans2 = fac(k)*fac(n-k)%mod;
    ans2 = mul(ans2,mod-2)%mod;
    printf("%lld",(ans1*ans2)%mod);

    return 0;
}
