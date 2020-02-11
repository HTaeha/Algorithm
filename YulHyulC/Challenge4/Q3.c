#include <stdio.h>

typedef struct{
    double real;
    double imagin;
}ComplexNum;
ComplexNum sum(ComplexNum n1,ComplexNum n2){
    ComplexNum res;

    res.real = n1.real + n2.real;
    res.imagin = n1.imagin + n2.imagin;

    return res;
}
ComplexNum mul(ComplexNum n1, ComplexNum n2){
    ComplexNum res;

    res.real = n1.real*n2.real - n1.imagin*n2.imagin;
    res.imagin = n1.real*n2.imagin + n1.imagin*n2.real;

    return res;
}
int main(){
    ComplexNum cn[2],result;
    int i;

    for(i=0;i<2;i++){
        scanf("%lf",&cn[i].real);
        scanf("%lf",&cn[i].imagin);
    }
    result = sum(cn[0],cn[1]);
    printf("Result of sum] real : %lf, imaginary : %lf\n",result.real,result.imagin);
    result = mul(cn[0],cn[1]);
    printf("Result of mul] real: %lf, imaginary : %lf\n",result.real,result.imagin);

    return 0;
}
