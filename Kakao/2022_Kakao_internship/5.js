const solution = (rc, operations) => {
    for(let operation of operations){
        if(operation == "ShiftRow"){
            ShiftRow(rc);
        }else if(operation == "Rotate"){
            Rotate(rc);
        }
    }

    return rc;
}

const ShiftRow = (arr) => {
    const row = arr.pop();
    arr.unshift(row);
}

const Rotate = (arr) => {
    const rowLen = arr.length;

    for(let i=rowLen-2;i>=0;i--){
        const change = arr[i].pop();
        arr[i+1].push(change);
    }
    const temp = arr[rowLen-1].shift();
    for(let i=0;i<rowLen-2;i++){
        const change = arr[i+1].shift();
        arr[i].unshift(change);
    }
    arr[rowLen-2].unshift(temp)
}

const rc = [[1, 2, 3], [4, 5, 6], [7, 8, 9]];
const operations = ["Rotate", "ShiftRow"];

console.log(solution(rc, operations));