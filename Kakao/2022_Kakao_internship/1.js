function solution(survey, choices) {
    var answer = '';

    const types = {
        R: 0,
        T: 0,
        C: 0,
        F: 0,
        J: 0,
        M: 0,
        A: 0,
        N: 0,
    };

    for (let i = 0; i < survey.length; i++) {
        if (choices[i] > 4) {
            types[survey[i][1]] += choices[i] - 4;
        } else if (choices[i] < 4) {
            types[survey[i][0]] += 4 - choices[i];
        }
    }

    if (types['R'] < types['T']) {
        answer += 'T';
    } else {
        answer += 'R';
    }
    if (types['C'] < types['F']) {
        answer += 'F';
    } else {
        answer += 'C';
    }
    if (types['J'] < types['M']) {
        answer += 'M';
    } else {
        answer += 'J';
    }
    if (types['A'] < types['N']) {
        answer += 'N';
    } else {
        answer += 'A';
    }

    return answer;
}

const survey = ["AN", "CF", "MJ", "RT", "NA"];
const choices = [5, 3, 2, 7, 5];
console.log(solution(survey, choices));