#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(){
    int s1, s2;
    int ans1, ans2;
    int flag=0;

    scanf("%d %d",&s1, &s2);

  //  int* s1_case;
   // s1_case = (int*)malloc(sizeof(int) * s1);
    while(s1--){
        scanf("%d %d", &ans1, &ans2);
        if(ans1 != ans2){
            flag = 1;
        }
    }
    if(flag == 1){
        printf("Wrong Answer");
        return 0;
    }
    while(s2--){
        scanf("%d %d", &ans1, &ans2);
        if(ans1 != ans2){
            flag = 1;
        }
    }
    if(flag == 1){
        printf("Why Wrong!!!");
        return 0;

    }

    printf("Accepted");

    return 0;
}
