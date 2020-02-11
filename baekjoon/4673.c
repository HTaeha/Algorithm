#include <stdio.h>
int check_selfnum(int num);
int main(){
    int i;
    for(i=1;i<10000;i++){
        if(!check_selfnum(i)){
            printf("%d\n",i);
        }
    }
    return 0;
}
int check_selfnum(int num){
    int j,result;
    if(num<10){
        for(j=1;j<num;j++){
            result = j + j;
            if(num==result){
                return 1;
            }            
        }
    }else if(num<100){
         for(j=num-18;j<num;j++){
            result = j + j%10 + j/10;
            if(num==result){
                return 1;
            }            
        }
        
    }else if(num<1000){
          for(j=num-27;j<num;j++){
//            result = j + j%10 + (j%100)/10 + j/100;
              result = j + j%10 + (j/10)%10 + j/100;
              if(num==result){
                return 1;
            }            
        }
   
    }else if(num<10000){
           for(j=num-36;j<num;j++){
//            result = j + j%10 + (j%100)/10 + (j%1000)/1000 + j/1000;
               result = j + j%10 + (j/10)%10 + (j/100)%10 + j/1000;
            if(num==result){
                return 1;
            }            
        }
  
    }
    return 0;
}
