#include <stdio.h>

int main(){
    FILE* fp = fopen("mystory.txt","rt");
    int fpos;
    int res;

    fpos = ftell(fp);
    fseek(fp,0,SEEK_END);
    res = ftell(fp);
    fseek(fp,fpos,SEEK_SET);
    printf("%d\n",res);
    fclose(fp);
    fp = NULL;

    return 0;
}
