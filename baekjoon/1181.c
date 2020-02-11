#include <stdio.h>
#include <string.h>
#include <stdlib.h>
int compare(const void *a, const void *b);
int main(void) {
    int num;
    int i;

    scanf("%d",&num);
    char word[num][51]; //각 단어 행에 하나씩 저장

    for(i=0;i<num;i++){
        scanf("%s",word+i);
    }
    qsort(word,num,sizeof(word[0]),compare);

    for(i=0;i<num;i++){ //같은 단어는 하나만 나오게 출력
        if(!strcmp(word+i,word+i+1)){
            continue;
        }else{
            printf("%s\n",word+i);
        }
    }

    return 0;
}
int compare(const void *a, const void *b){
    int a_len;
    int b_len;
    a_len = strlen(a);
    b_len = strlen(b);
    if(a_len == b_len){
        return strcmp((char*)a, (char*)b);
    }else if(a_len > b_len){
        return 1; 
    }else{
        return -1;
    }
}
