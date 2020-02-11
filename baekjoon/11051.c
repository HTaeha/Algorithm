#include <stdio.h>

const int mod = 10007;
int memo[1000][1000] = {1,1,};
int bino(int n,int k){
	if(n==k || k==0){
		return 1;
	}
	if(memo[n][k] != 0){
		return memo[n][k]%mod;
	}
	return memo[n][k] = bino(n-1,k-1)%mod+bino(n-1,k)%mod;
}
int main(void) {
	int n,k;
	scanf("%d %d",&n,&k);
	printf("%d",bino(n,k)%mod);
	return 0;
}

