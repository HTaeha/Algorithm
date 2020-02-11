#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_NUM 100
typedef struct{
    char name[50];
    char tel[50];
}PhoneManager;
void LoadData(PhoneManager* pm){
    FILE* fp = fopen("data.txt","rt");
    int end;
    int index=0;

    if(fp == NULL){
        printf("Data file open error\n");
        return ;
    }
    while(1){
        end = fscanf(fp,"%s %s",pm[index++].name,pm[index++].tel);
        if(end ==EOF){
            break;
        }
    }
    fclose(fp);
}
void StoreData(PhoneManager* pm, int len){
    FILE* fp = fopen("data.txt","wt"); 
    int i;

    if(fp == NULL){
        printf("File open error");
        return ;
    }
    for(i=0;i<len;i++){
        fprintf(fp,"%s %s",pm[i].name,pm[i].tel);
    }
    fclose(fp);
}
void menu(void){
    printf("***** MENU *****\n");
    printf("1. Insert\n");
    printf("2. Delete\n");
    printf("3. Search\n");
    printf("4. Print All\n");
    printf("5. Exit\n");
}
void insert(PhoneManager * pm, int* len){
    printf("[INSERT]\n");
    printf("Input Name : ");
    scanf("%s",pm[*len].name);
    printf("Input Tel Number : \n");
    scanf("%s",pm[*len].tel);
    *len++;
    printf("\t\tData Inserted\n");
}
void delete(PhoneManager* pm, int* len){
    int i;
    char name[20];
    printf("[DELETE]\n");
    printf("Please input name to delete\n");
    scanf("%s",name);
    for(i=0;i<*len;i++){
        if(strcmp(name,pm[i].name)){
            
        }
    }
}
int main(){
    int num;
    PhoneManager parr[MAX_NUM];
    int parr_len=0;

    LoadData(parr);
    while(1){
        menu();
        scanf("%d",&num);
        printf("Choose the item: %d\n",num);
        switch(num){
            case 1:
                insert(parr, &parr_len);
                break;
            case 2:
            case 3:    
            case 4:
            case 5:
            printf("[EXIT]\n");
            StoreData(parr,parr_len);
                return 0;
            default:
                printf("Please choose 1~5 number\n");
        }
    }
}
