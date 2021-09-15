// 입실 퇴실
// https://programmers.co.kr/learn/courses/30/lessons/86048?language=go
package main

import "fmt"

func solution(enter []int, leave []int) []int {
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

// i index의 값을 제거한다.
func remove(s []int, i int) []int {
	s[i] = s[len(s)-1]
	return s[:len(s)-1]
}

func numberInSlice(a int, list []int) bool {
	for _, b := range list {
		if b == a {
			return true
		}
	}
	return false
}

func main() {
	// 1 ~ 1000 length
	e := []int{1, 3, 2}
	l := []int{1, 2, 3}
	// e := []int{1, 4, 2, 3}
	// l := []int{2, 1, 3, 4}
	// e := []int{3, 2, 1}
	// l := []int{2, 1, 3}
	// e := []int{3, 2, 1}
	// l := []int{1, 3, 2}
	// e := []int{1, 4, 2, 3}
	// l := []int{2, 1, 4, 3}
	// e := []int{1, 2, 3}
	// l := []int{1, 2, 3}

	//     [1,3,2]	[1,2,3]	[0,1,1]
	// [1,4,2,3]	[2,1,3,4]	[2,2,1,3]
	// [3,2,1]	[2,1,3]	[1,1,2]
	// [3,2,1]	[1,3,2]	[2,2,2]
	// [1,4,2,3]	[2,1,4,3]	[2,2,0,2]

	meets := solution(e, l)
	fmt.Println(meets)
}
