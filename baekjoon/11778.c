#include <stdio.h>

#define SIZE 2
int div = 1000000007;
long long int matrix[2][2] = {1,1,1,0};
typedef struct{
    long long int f[2][2];
}Matrix2x2;
long long int GCD(long long int big, long long int small){
    if(small == 0){
        return 0;
    }
    return big%small ? GCD(small,big%small) : small;
}
Matrix2x2 mul(Matrix2x2 A, Matrix2x2 B){
    Matrix2x2 C;
    C.f[0][0] = A.f[0][0]*B.f[0][0] + A.f[0][1]*B.f[1][0];
    C.f[1][0] = A.f[1][0]*B.f[0][0] + A.f[1][1]*B.f[1][0];
    C.f[0][1] = A.f[0][0]*B.f[0][1] + A.f[0][1]*B.f[1][1];
    C.f[1][1] = A.f[1][0]*B.f[0][1] + A.f[1][1]*B.f[1][1];
    return C;
}
Matrix2x2 pow(Matrix2x2 A, long long int n){
    if(n == 1){
        return A;
    }else if(n%2 == 0){
        return pow(mul(A,A),n/2);
    }else{
        return mul(A, pow(mul(A,A),(n-1)/2));
    }
}
long long int Fib(long long int a){
    if(a<2){
        return a;
    }
    Matrix2x2 temp={1,1,1,0};
    temp = pow(temp,a);
    return temp.f[1][0];
}
int main(){
    long long int n,m;
    long long int b,s;

    scanf("%lld %lld",&n,&m);
    if(n>m){
        b = n;
        s = m;
    }else{
        b = m;
        s = n;
    }
    printf("Fib(%lld) : %lld, Fib(%lld): %lld\n",b,Fib(b),s,Fib(s));
    printf("%lld",GCD(Fib(b),Fib(s))%div);

    return 0;
}
