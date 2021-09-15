// 입실 퇴실
// https://programmers.co.kr/learn/courses/30/lessons/86048?language=go
package main

import "fmt"

func solution(enter []int, leave []int) []int {
	result := make([]int, len(enter)+1, len(enter)+1)
	room := make(map[int]bool)

	ei, li := 0, 0

	for ei < len(enter) || li < len(leave) {
		if !room[leave[li]] {
			result[enter[ei]] = len(room)
			for k := range room {
				result[k] += 1
			}
			room[enter[ei]] = true
			ei += 1
		} else {
			delete(room, leave[li])
			li += 1
		}
	}
	return result[1:]
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
