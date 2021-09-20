// 상호 평가
// https://programmers.co.kr/learn/courses/30/lessons/83201

package weekly

func Week2(scores [][]int) string {
	result := ""
	var avg float64
	for i, v := range scores {
		// 내가 매긴 점수가 최솟값인지 체크.
		minFlag := true
		// 내가 매긴 점수가 최댓값인지 체크.
		maxFlag := true
		myScore := v[i]
		sum := 0
		for col := 0; col < len(scores); col++ {
			v2 := scores[col][i]
			sum += v2
			if i == col {
				continue
			}
			if v2 <= myScore {
				minFlag = false
			}
			if v2 >= myScore {
				maxFlag = false
			}
		}

		if minFlag || maxFlag { // 내 점수 제외
			avg = float64(sum-myScore) / float64(len(scores)-1)
		} else {
			avg = float64(sum) / float64(len(scores))
		}
		result += eval(avg)
	}
	return result
}

// 학점 매기기.
func eval(score float64) string {
	switch {
	case score >= 90:
		return "A"
	case score >= 80:
		return "B"
	case score >= 70:
		return "C"
	case score >= 50:
		return "D"
	default:
		return "F"
	}
}
