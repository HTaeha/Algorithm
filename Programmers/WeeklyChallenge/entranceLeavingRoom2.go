// 입실 퇴실
// https://programmers.co.kr/learn/courses/30/lessons/86048?language=go
package main

import "fmt"

func solution(enter []int, leave []int) []int {
	meets := make([][]int, len(enter)+1, len(enter)+1)
	// meets := make([]map[int]bool, len(enter)+1, len(enter)+1)
	// for i := range meets {
	// 	meets[i] = map[int]bool{}
	// }
	result := make([]int, len(enter)+1, len(enter)+1)
	room := []int{}

	ei, li := 0, 0

	for ei < len(enter) || li < len(leave) {
		fmt.Println(meets, room, ei, li)
		if !numberInSlice(leave[li], room) {
			meets[enter[ei]] = room[:]
			// meets[leave[li]] = setAdd(meets[leave[li]], enter[ei])
			room = append(room, enter[ei])
			ei += 1
		} else {
			room = removeVal(room, leave[li])
			li += 1
		}
	}

	fmt.Println(meets)
	fmt.Println()
	temp := make([]map[int]bool, len(enter)+1, len(enter)+1)
	for i := range temp {
		temp[i] = map[int]bool{}
	}
	for i, a := range meets {
		// temp[i] = a[:]
		for _, v := range a {
			setAdd(temp[i], v)
			setAdd(temp[v], i)
			// if !numberInSlice(i, temp[v]) {
			// 	// result[v] += 1
			// 	fmt.Println(i, v, temp)
			// 	temp[3] = append(temp[3], 1)
			// 	fmt.Println(i, v, temp)
			// 	// meets[v] = append(meets[v], i)
			// 	// fmt.Println(i, v, meets)
			// }
		}
	}
	fmt.Println(temp)
	for i, a := range temp {
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

func setAdd(s map[int]bool, v int) map[int]bool {
	s[v] = true
	return s
}

func main() {
	// 1 ~ 1000 length
	// e := []int{1, 3, 2}
	// l := []int{1, 2, 3}
	e := []int{1, 4, 2, 3}
	l := []int{2, 1, 3, 4}
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

	test := make([][]int, 5, 5)
	test[0] = []int{}
	test[1] = []int{}
	test[2] = []int{3}
	test[3] = []int{}

	// fmt.Println(test)
	// for i, a := range test {
	// 	fmt.Println(i, a)
	// 	for _, v := range a {
	// 		if !numberInSlice(i, test[v]) && v != i {
	// 			fmt.Println(v, i, test)
	// 			test[3] = append(test[3], i)
	// 			fmt.Println(test)
	// 		}
	// 	}
	// }
	// // test[3] = append(test[3], 2)
	// fmt.Println(test)

}
