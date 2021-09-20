// https://programmers.co.kr/learn/courses/30/lessons/82612
// 부족한 금액 계산하기

package weekly

func Week1(price int, money int, count int) int64 {
	sum := price * count * (count + 1) / 2
	if money >= sum {
		return 0
	} else {
		return int64(sum - money)
	}
}
