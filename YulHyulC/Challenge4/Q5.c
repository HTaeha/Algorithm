#include <stdio.h>

int main(){
    FILE* f1 = fopen("d1.txt","rt");
    FILE* f2 = fopen("d2.txt","rt");
    int ch1,ch2;
    int s1,s2;

    if(f1 == NULL){
        printf("f1 file open error\n");
        return -1;
    }else if(f2 == NULL){
        printf("f2 file open error\n");
        return -1;
    }
    while(1){
        ch1 = fgetc(f1);
        ch2 = fgetc(f2);
        if(ch1 == EOF || ch2 == EOF){
            break;
        }
        if(ch1 != ch2){
            printf("d1.txt != d2.txt\n");
            return 0;
        }
    }
    printf("d1.txt == d2.txt\n");
    s1 = fclose(f1);
    s2 = fclose(f2);
    if(s1 ==EOF){
        printf("f1 file close error\n");
        return -1;
    }else if(s2 ==EOF){
        printf("f2 file close error\n");
        return -1;
    }

    return 0;
}
