// 입실 퇴실
// https://programmers.co.kr/learn/courses/30/lessons/86048?language=go
package weekly

func Week7(enter []int, leave []int) []int {
	meets := make([][]int, len(enter)+1, len(enter)+1)
	result := make([]int, len(enter)+1, len(enter)+1)
	room := []int{}

	ei, li := 0, 0

	for ei < len(enter) || li < len(leave) {
		if !numberInSlice(leave[li], room) {
			for _, b := range room {
				meets[enter[ei]] = append(meets[enter[ei]], b)
			}
			room = append(room, enter[ei])
			ei += 1
		} else {
			room = removeVal(room, leave[li])
			li += 1
		}
	}

	for i, a := range meets {
		for _, v := range a {
			if !numberInSlice(i, meets[v]) {
				meets[v] = append(meets[v], i)
			}
		}
	}
	for i, a := range meets {
		result[i] = len(a)
	}

	return result[1:]
}

// s slice에서 가장 먼저 나온 v값을 제거한다.
func removeVal(s []int, v int) []int {
	for i, val := range s {
		if val == v {
			s = remove(s, i)
			break
		}
	}
	return s
}

// s slice에서 index i의 값을 제거한다.
func remove(s []int, i int) []int {
	s[i] = s[len(s)-1]
	return s[:len(s)-1]
}

// slice에 int n값이 존재하는지 알려준다.
func numberInSlice(n int, s []int) bool {
	for _, v := range s {
		if v == n {
			return true
		}
	}
	return false
}
