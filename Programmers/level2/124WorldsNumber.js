function solution(n) {
    var answer = '';

    while(n > 0){
        let rest = n%3
        n = Math.floor(n/3)

        if (rest == 0){
            n -= 1
            rest = 4
        }
        answer = rest.toString() + answer
    }
    return answer;
}

const n = 10
console.log(solution(n))