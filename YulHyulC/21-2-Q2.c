#include <stdio.h>
#include <stdlib.h>
#include <string.h>
int main(){
    char str1[20];
    char str2[20];
    char str3[40];

    fgets(str1, sizeof(str1),stdin);
    fgets(str2, sizeof(str2),stdin);

    str1[strlen(str1)-1] = 0;
    str2[strlen(str2)-1] = 0;

    strcpy(str3,str1);
    strcat(str3,str2);

    printf("%s\n",str3);

    return 0;
}
