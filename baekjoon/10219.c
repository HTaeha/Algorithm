#include <stdio.h>

int main(){
    int T;
    int H,W;
    int i,j;
    char arr[11][11];
    char res[11][11];
    scanf("%d",&T);

    while(T--){
        scanf("%d %d",&H,&W);
        getchar();
        for(i=0;i<H;i++){
            for(j=0;j<W;j++){
                scanf("%c",&arr[i][j]);
                res[i][W-j-1] = arr[i][j];
            }
            getchar();
        }
        for(i=0;i<H;i++){
            for(j=0;j<W;j++){
                printf("%c",res[i][j]);
            }
            printf("\n");
        }
    }
    return 0;
}
