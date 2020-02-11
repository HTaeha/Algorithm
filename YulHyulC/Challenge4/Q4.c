#include <stdio.h>
#include <stdlib.h>

int main(){
    FILE* fp = fopen("text.txt","rt");
    int acount=0,pcount=0;
    char word[50];
    int ret;
    int state;

    if(fp == NULL){
        printf("file open error\n");
        return -1;
    }
    while(1){
        ret = fscanf(fp,"%s",word);
        if(ret == EOF){
            break;
        }
        printf("word : %s\n",word);
        if(word[0] == 'A'){
            acount++;
        }else if(word[0] == 'P'){
            pcount++;
        }
    }
    printf("The number of word to start 'A' : %d\n",acount);
    printf("The number of word to start 'P' : %d\n",pcount);

    state = fclose(fp);
    if(state == EOF){
        printf("file close error\n");
        return -1;
    }
    return 0;
}
