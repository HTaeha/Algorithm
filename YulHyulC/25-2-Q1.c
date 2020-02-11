#include <stdio.h>
#include <stdlib.h>

int main(){
    int max_len;
    printf("Please input max sentence length\n");
    scanf("%d",&max_len);
    getchar();
    char * stc = (char *)malloc(sizeof(char)*(max_len+1));
    gets(stc);

    int i,j;
    int len = strlen(stc);
    int before = len-1;
    for(i=len-1;i>=0;i--){
        if(stc[i] == ' '){
            for(j=i+1;j<=before;j++){
                printf("%c",stc[j]);
            }
            printf(" ");
            before = i-1;
        }
        if(i==0){
            for(j=0;j<=before;j++){
                printf("%c",stc[j]);
            }
        }
    }
    free(stc);
    return 0;
}
