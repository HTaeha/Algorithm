#include <stdio.h>

int main(){
    FILE* fp = fopen("mystory.txt","wt");
    char arr[20];
    int ch;
    
    fputs("#name: ",fp);
    scanf("%s",arr);
    getchar();
    fputs(arr,fp);

    fputs("\n#ID number: ",fp);
    scanf("%s",arr);
    getchar();
    fputs(arr,fp);

    fputs("\n#phone number: ",fp);
    scanf("%s",arr);
    getchar();
    fputs(arr,fp);

    fclose(fp);

    return 0;
}
