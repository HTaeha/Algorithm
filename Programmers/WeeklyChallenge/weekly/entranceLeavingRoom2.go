// 입실 퇴실
// https://programmers.co.kr/learn/courses/30/lessons/86048?language=go
package weekly

func Week7_2(enter []int, leave []int) []int {
	// index 0을 사용하지 않기 위해 length를 1추가해서 slice정의.
	// index는 person number를 뜻하고 index 안의 값은 만난 사람 수를 뜻한다.
	result := make([]int, len(enter)+1, len(enter)+1)
	// 현재 방의 상태. 누가 들어와 있는지 알 수 있다.
	// key : person number
	// val : true/false 존재하는지 여부
	room := make(map[int]bool)

	// enter index, leave index
	// enter, leave slice에서 보고 있는 index를 각각 의미한다.
	ei, li := 0, 0

	for ei < len(enter) || li < len(leave) {
		if !room[leave[li]] { // 나갈 사람이 방에 존재하지 않을 때
			// 방에 들어갈 다음 사람을 입장시킨다.
			// 방에 들어간 사람은 현재 방에 존재하는 사람들을 만났으므로 추가해준다.
			result[enter[ei]] = len(room)
			// 기존에 방에 존재하던 사람은 한 명이 들어왔으므로 1씩 추가해준다.
			for k := range room {
				result[k] += 1
			}
			// 방에 들어온 사람을 표시해주고 ei 1증가.
			room[enter[ei]] = true
			ei += 1
		} else { // 나갈 사람이 방에 존재할 때
			// 방에서 내보낸다.
			delete(room, leave[li])
			li += 1
		}
	}

	// index 0을 제외하고 리턴.
	return result[1:]
}
