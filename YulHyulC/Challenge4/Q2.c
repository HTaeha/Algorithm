#include <stdio.h>
#include <stdlib.h>

#define len 30
typedef struct{
    char name[len];
    char author[len];
    int page;
}BookManager;
int main(){
    BookManager * bm[3];
    int i;

    for(i=0;i<3;i++){
        bm[i]= (BookManager *)malloc(sizeof(BookManager)*1);
    }
    for(i=0;i<3;i++){
        printf("author: ");
        gets(bm[i]->author);
        printf("book name: ");
        gets(bm[i]->name);
        printf("page number: ");
        scanf("%d",&bm[i]->page);
        getchar();
    }
    for(i=0;i<3;i++){
        printf("book %d\n",i+1);
        printf("author: ");
        puts(bm[i]->author);
        printf("book name: ");
        puts(bm[i]->name);
        printf("page number: ");
        printf("%d\n",bm[i]->page);
    }
    for(i=0;i<3;i++){
        free(bm[i]);
    }
    return 0;
}
