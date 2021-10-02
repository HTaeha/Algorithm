function solution(w, h) {
    const small = w < h ? w:h

    for(let i=small;i>1;i--){
        if(w%i == 0 && h%i == 0){
            return w*h - (w+h-i)
        }
    }
    return w*h - (w+h-1)
}

const w = 8
const h = 12
console.log(solution(w, h))