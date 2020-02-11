#include <stdio.h>

typedef struct{
    char name[20];
    char author[10];
    int page;
}BookManager;
int main(){
    BookManager bm[3];
    int i;

    for(i=0;i<3;i++){
        printf("author: ");
        gets(bm[i].author);
        printf("book name: ");
        gets(bm[i].name);
        printf("page number: ");
        scanf("%d",&bm[i].page);
        getchar();
    }
    for(i=0;i<3;i++){
        printf("book %d\n",i+1);
        printf("author: ");
        puts(bm[i].author);
        printf("book name: ");
        puts(bm[i].name);
        printf("page number: ");
        printf("%d\n",bm[i].page);
    }
    return 0;
}
