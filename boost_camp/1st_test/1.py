def solution(name_list):
    for i, name in enumerate(name_list):
        for j in range(0, len(name_list)):
            # Find other name to include name in name_list 
            if name in name_list[j] and i != j:
                return True

    return False

if __name__ == "__main__":
    name_list = ["가을", "우주", "너굴"]
    name_list = ["봄", "여울", "봄봄"]
    solution(name_list)
