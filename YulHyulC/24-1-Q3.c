#include <stdio.h>

int main(){
    FILE* fp = fopen("mystory.txt","rt");
    int ch;

    if(fp == NULL){
        printf("File open error");
        return -1;
    }
    while(feof(fp)==0){
        ch = fgetc(fp);
        putchar(ch);
    }
    fclose(fp);
    fp = NULL;
    return 0;
}
