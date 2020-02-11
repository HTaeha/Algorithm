#include <stdio.h>

int main(){
    FILE* fp = fopen("mystory.txt","at");
    char arr[20];

    fputs("\n#favorite food: ",fp);
    scanf("%s",arr);
    fputs(arr,fp);

    fputs("\n#hobby: ",fp);
    scanf("%s",arr);
    fputs(arr,fp);

    fclose(fp);
    fp = NULL;

    return 0;
}
