#include <stdio.h>

int main(void) {
	int num;
	int arr[10]={0,};
	int i, max1,max2;
	
	scanf("%d",&num);

    if(num == 0){
        printf("1");
        return 0;
    }
	while(num > 0){
        arr[num%10]++;
		num = num/10;
	}
	
	max1 = arr[0];
	for(i=0;i<10;i++){
		if(i==6 || i==9){
			continue;
		}else{
			if(max1 < arr[i]){
				max1 = arr[i];
			}
		}
	}
	max2 = arr[6]+arr[9];
	if(max2%2 == 0){
		if(max1 < max2/2){
			printf("%d",max2/2);
		}else{
			printf("%d",max1);
		}
	}else{
		if(max1 < (max2+1)/2){
			printf("%d",(max2+1)/2);
		}else{
			printf("%d",max1);
		}
	}
	
	return 0;
}

