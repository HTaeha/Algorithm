#include <stdio.h>

const int mod=1000000007;
typedef unsigned long long ULONG;
typedef struct{
    ULONG f[2][2];
}Matrix2x2;
Matrix2x2 mult(Matrix2x2 A, Matrix2x2 B){
    Matrix2x2 C;
    C.f[0][0] = (A.f[0][0]%mod*B.f[0][0]%mod + A.f[0][1]%mod*B.f[1][0]%mod)%mod;
    C.f[0][1] = (A.f[0][0]%mod*B.f[0][1]%mod + A.f[0][1]%mod*B.f[1][1]%mod)%mod;
    C.f[1][0] = (A.f[1][0]%mod*B.f[0][0]%mod + A.f[1][1]%mod*B.f[1][0]%mod)%mod;
    C.f[1][1] = (A.f[1][0]%mod*B.f[0][1]%mod + A.f[1][1]%mod*B.f[1][1]%mod)%mod;
    return C;
}
Matrix2x2 Matrix_Power(Matrix2x2 A,ULONG n){
    if(n>1){
        A = Matrix_Power(A,n/2);
        A = mult(A,A);
        if(n&1){
            Matrix2x2 F1 = {1,1,1,0};
            A = mult(A,F1);
        }
    }
    return A;
}
int main(){
    ULONG n;
    Matrix2x2 F = {1,1,1,0};
    scanf("%llu",&n);
    F = Matrix_Power(F,n);
    printf("%llu",F.f[0][1]);
    return 0;
}
