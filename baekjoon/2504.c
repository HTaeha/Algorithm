#include <stdio.h>

#define MAX_STACK_SIZE 51
typedef char element;
typedef struct{
    element stack[MAX_STACK_SIZE];
    int top;
}StackType;
void init(StackType *s);
int is_empty(StackType *s);
int is_full(StackType *s);
void push(StackType *s, element item);
element pop(StackType *s);
int main(void) {
    StackType s;
    char temp;
    int result=0;
    int count_s=1;
    int count_l=1;
    int flag = 0;
    element temp1;

    init(&s);
    while((temp = getchar()) != EOF){
        if(temp == '('){
            push(&s,temp);
            count_s *= 2;
            flag =0;
        }else if(temp == '['){
            push(&s,temp);
            count_l *= 3;
            flag = 0;
        }else if(temp == ')'){
            temp1 = pop(&s);
            if(temp1 == '('){
                if(flag==0){
                    result += count_s*count_l;
                }
                count_s /= 2;
            }else if(temp1==0){
                printf("0");
                return 0;
            }else if(temp1 == '['){
                printf("0");
                return 0;
            }
            flag = 1;
        }else if(temp == ']'){
            temp1 = pop(&s);
            if(temp1 == '['){
                if(flag==0){
                    result += count_s*count_l;
                }               
                count_l /= 3;
            }else if(temp1==0){
                printf("0");
                return 0;
            }else if(temp1 == '('){
                printf("0");
                return 0;
            }
            flag = 1;
        }
    }
    if(s.top != -1){
        printf("0");
    }else{
        printf("%d",result);
    }
    return 0;
}
void init(StackType *s){
    s->top = -1;
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
void push(StackType *s, element item){
    s->top++;
    s->stack[s->top]=item;
}
element pop(StackType *s){
    if(is_empty(s)){
        return 0;
    }else{
        return s->stack[s->top--];
    }
}
