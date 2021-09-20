package main

import (
	"fmt"

	"github.com/HTaeha/Programmers/WeeklyChallenge/weekly"
)

func main() {
	// 1번
	price := 3
	money := 20
	count := 4

	result := weekly.Week1(price, money, count)
	fmt.Println(result)

	// 7번
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

	meets := weekly.Week7_2(e, l)
	fmt.Println(meets)

	// Week3
	scores := [][]int{
		{100, 90, 98, 88, 65},
		{50, 45, 99, 85, 77},
		{47, 88, 95, 80, 67},
		{61, 57, 100, 80, 65},
		{24, 90, 94, 75, 65},
	}
	Week2 := weekly.Week2(scores)
	fmt.Println("Week2 : ", Week2)
}
