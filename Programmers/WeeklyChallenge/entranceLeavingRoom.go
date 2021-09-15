// 입실 퇴실
// https://programmers.co.kr/learn/courses/30/lessons/86048?language=go
// 틀린 풀이
package main

import (
	"fmt"
)

func solution(enter []int, leave []int) []int {
	meets := make([]map[int]bool, len(enter), len(enter))
	for i := range meets {
		meets[i] = map[int]bool{}
	}
	result := []int{}

	room, enter := firstRoom(enter, leave[0])

	fmt.Println(room, enter, leave)
	for _, v := range leave {
		fmt.Println("v: ", v, room)
		fmt.Println("meets : ", meets)
		if numberInSlice(v, room) {
			meets = countMember(meets, room, v)
			room = removeVal(room, v)
		} else {
			for _, v2 := range enter {
				room = append(room, v2)
				enter = removeVal(enter, v2)
				if v2 == v {
					break
				}
			}
			meets = countMember(meets, room, v)
			room = removeVal(room, v)
		}
	}

	fmt.Println(meets)
	for _, v := range meets {
		fmt.Println("v", v, len(v))
		result = append(result, len(v))
	}
	return result
}

func firstRoom(enter []int, firstLeave int) ([]int, []int) {
	room := []int{}
	for _, v := range enter {
		room = append(room, v)
		if v == firstLeave {
			enter = enter[1:]
			break
		} else {
			enter = enter[1:]
		}
	}

	return room, enter
}

func countMember(meets []map[int]bool, room []int, person int) []map[int]bool {
	for _, v := range room {
		for _, v2 := range room {
			if v != v2 {
				meets[v-1] = setAdd(meets[v-1], v2)
			}
		}
	}

	return meets
}

func setAdd(s map[int]bool, v int) map[int]bool {
	s[v] = true
	return s
}

func numberInSlice(a int, list []int) bool {
	for _, b := range list {
		if b == a {
			return true
		}
	}
	return false
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

func main() {
	// 1 ~ 1000 length
	// e := []int{1, 3, 2}
	// l := []int{1, 2, 3}
	// e := []int{1, 4, 2, 3}
	// l := []int{2, 1, 3, 4}
	// e := []int{3, 2, 1}
	// l := []int{2, 1, 3}
	// e := []int{3, 2, 1}
	// l := []int{1, 3, 2}
	// e := []int{1, 4, 2, 3}
	// l := []int{2, 1, 4, 3}
	e := []int{1, 2, 3}
	l := []int{1, 2, 3}

	//     [1,3,2]	[1,2,3]	[0,1,1]
	// [1,4,2,3]	[2,1,3,4]	[2,2,1,3]
	// [3,2,1]	[2,1,3]	[1,1,2]
	// [3,2,1]	[1,3,2]	[2,2,2]
	// [1,4,2,3]	[2,1,4,3]	[2,2,0,2]

	meets := solution(e, l)
	fmt.Println(meets)

	a := []int{0, 1, 2, 3, 4, 5}
	for v := range a {
		fmt.Println("v : ", v)
		fmt.Println("before : ", a)
		a = removeVal(a, 1)
		fmt.Println("after : ", a)
	}
	fmt.Println(a)
}
