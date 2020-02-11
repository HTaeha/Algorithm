#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(){
    int n, d, l;
    int arr[13];
    int index = 1;
    int min;
    int min_index;
    double temp_min = 1000;
    double temp;
    int temp_d;
    int count = 0;
    int len_l;
    int res;

    scanf("%d %d %d",&n,&d,&l);

    len_l = l;
    while(l--){
        scanf("%d",&arr[index]);
        temp = arr[index]/(index);
        if(temp_min > temp){
            temp_min = temp;
            min = arr[index];
            min_index = index;
        }
        index++;
    }
    printf("%d %d\n", min, min_index);

    temp_d = d;
    while(temp_d>len_l){
        temp_d -= min_index;
        count++;
    }
    temp_d += min_index;
    count--;
    res = count * min;
    printf("temp_d : %d count : %d\n",temp_d,count);

    return 0;
}
