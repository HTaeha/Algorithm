#include <stdio.h>

#define MAX_STACK_SIZE 100000
typedef int element;
typedef struct{
    element stack[MAX_STACK_SIZE];
    int top;
}StackType;
void init(StackType *s);
int is_empty(StackType *s);
int is_full(StackType *s);
void push(StackType *s, element num);
element pop(StackType *s);
int main(){
    StackType s;
    init(&s);
    int n;
    int num;
    int count=1;
    int i;

    scanf("%d",&n);
    char result[2*n];
    int index=0;

    while(n--){
        scanf("%d",&num);
        if(s.top == -1){
            result[index++]='+';
            push(&s,count++);
        } 
        while(num > s.stack[s.top]){
            result[index++]='+';
            push(&s,count++);
        }

        if(num != s.stack[s.top]){
            printf("NO");
            return 0;
        }
        result[index++]='-';
        pop(&s);
    }
    for(i=0;i<index;i++){
        printf("%c\n",result[i]);
    }

    return 0;
}
void init(StackType *s){
    s->top = -1;
    s->stack[0] = 0;
}
int is_empty(StackType *s){
    if(s->top == -1){
        return 1;
    }else{
        return 0;
    }
}
int is_full(StackType *s){
    if(s->top == MAX_STACK_SIZE-1){
        return 1;
    }else{
        return 0;
    }
}
void push(StackType *s, element num){
    if(is_full(s)){
        
    }else{
        s->stack[++s->top] = num;
    }
}
element pop(StackType *s){
    if(is_empty(s)){
    
    }else{
        return s->stack[s->top--];
    }
}
