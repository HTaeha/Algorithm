function solution(progresses, speeds) {
    var answer = [];
    var days = []

    for(let i=0;i<progresses.length;i++){
        const sub = 100 - progresses[i]
        const temp = sub/speeds[i]
        days.push(Math.ceil(temp))
    }

    let standard = days[0]
    let count = 0
    for(let i=0;i<days.length;i++){
        if (standard < days[i]){
            answer.push(count)
            standard = days[i]
            count = 1
        }else{
            count += 1
        }
    }
    answer.push(count)

    return answer;
}

const progresses = [93, 30, 55]
const speeds = [1, 30, 5]
console.log(solution(progresses, speeds))