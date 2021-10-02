function solution(numbers, target) {
    var answer = 0;
    const stack  = []
    stack.push([numbers[0], 0])
    stack.push([-numbers[0], 0])

    while(stack.length > 0){
        let [temp, index] = stack.pop()

        if (index == numbers.length-1){
            if(temp == target){
                answer += 1
            }
        } else {
            stack.push([temp + numbers[index+1], index+1])
            stack.push([temp - numbers[index+1], index+1])
        }
    }

    return answer;
}

const numbers = [1, 1, 1, 1, 1]
const target = 3

console.log(solution(numbers, target))