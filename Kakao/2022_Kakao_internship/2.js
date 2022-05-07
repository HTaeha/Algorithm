function solution(queue1, queue2) {
    var answer = 0;
    let sum1 = 0;
    let sum2 = 0;
    let front1 = 0;
    let front2 = 0;

    queue1.forEach((value) => {
        sum1 += value
    });
    queue2.forEach((value) => {
        sum2 += value
    });

    while(true){
        if(sum1 < sum2){
            // const item = queue2.shift();
            const item = queue2[front2];
            front2 += 1;
            delete queue2[0];
            queue1.push(item);
            sum1 += item;
            sum2 -= item;
        }else if(sum1 > sum2){
            // const item = queue1.shift();
            const item = queue1[front1];
            front1 += 1;
            delete queue1[0];
            queue2.push(item);
            sum2 += item;
            sum1 -= item;
        }else{
            break;
        }

        if(sum1 == 0 || sum2 == 0){
            return -1;
        }

        // if(front1 == 1000){
        //     queue1.splice(0, 1000);
        // }
        // if(front2 == 1000){
        //     queue2.splice(0, 1000);
        // }

        answer += 1;
    }

    return answer;
}

const queue1 = [3, 2, 7, 2]
const queue2 = [4, 6, 5, 1]

console.log(solution(queue1, queue2));