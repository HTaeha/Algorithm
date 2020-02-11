#include <stdio.h>
#include <math.h>

int MAX_QUEUE_SIZE = 51;
typedef int element;
typedef struct{
    element queue[MAX_QUEUE_SIZE];
    int front,rear;
}QueueType;
void init(QueueType *q);
void enqueue(QueueType *q,element item);
element dequeue(QueueType *q);
void ope2(QueueType *q);
void ope3(QueueType *q);
int main(){
    QueueType q;
    init(&q);
    int N,M;
    int num;
    int i;
    int count = 0;
    scanf("%d %d",&N,&M);
    MAX_QUEUE_SIZE = N;
    for(i=0;i<N;i++){
        enqueue(&q,i+1);
    }
    while(M--){
        scanf("%d",&num);
        while(1){
            if((q.front+1)%MAX_QUEUE_SIZE == num){
                dequeue(&q);
                break;
            }
            printf("front:%d num:%d\n",(q.front+1)%MAX_QUEUE_SIZE,num);
            if(num > (q.front+1)%MAX_QUEUE_SIZE){
                if(num-(q.front+1)%MAX_QUEUE_SIZE < N-num+(q.front+1)%MAX_QUEUE_SIZE){
                    printf("A\n");
                    count += num-(q.front+1)%MAX_QUEUE_SIZE;
                    for(i=0;i<num-(q.front+1)%MAX_QUEUE_SIZE;i++){
                        ope2(&q);
                    }
                }else{
                    printf("B\n");
                    count += N-num+(q.front+1)%MAX_QUEUE_SIZE;
                    for(i=0;i<N-num+(q.front+1)%MAX_QUEUE_SIZE;i++){
                        ope3(&q);
                    }
                }
            }else{
                if((q.front+1)%MAX_QUEUE_SIZE - num < N-(q.front+1)%MAX_QUEUE_SIZE+num){
                    printf("C\n");
                    count += (q.front+1)%MAX_QUEUE_SIZE-num;
                    for(i=0;i<(q.front+1)%MAX_QUEUE_SIZE-num;i++){
                        ope3(&q);
                    }
                }else{
                    printf("D\n");
                    count += N-(q.front+1)%MAX_QUEUE_SIZE+num;
                    for(i=0;i<N-(q.front+1)%MAX_QUEUE_SIZE+num;i++){
                        ope2(&q);
                    }
                }
            }
        }
        printf("count : %d\n",count);

    }
    printf("%d",count);
    return 0;
}
void init(QueueType *q){
    q->front = 0;
    q->rear = 0;
}
void enqueue(QueueType *q,element item){
    q->queue[(++q->rear)%MAX_QUEUE_SIZE] = item;

}
element dequeue(QueueType *q){
    (q->front++)%MAX_QUEUE_SIZE;
    return q->queue[q->front];
}
void ope2(QueueType *q){
    enqueue(q,dequeue(q));
}
void ope3(QueueType *q){
    int r = q->rear;
    int f = q->front;

    while(r != (q->front+1)%MAX_QUEUE_SIZE){
        ope2(q);
    }
}
