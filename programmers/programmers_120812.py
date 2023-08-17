# https://school.programmers.co.kr/learn/courses/30/lessons/120812
from typing import List


def solution(array):
    count_list: List[int] = [0] * 1001
    for num in array:
        count_list[num] += 1

    answer: int = 0
    max_count: int = max(count_list)
    for num in range(1, len(count_list)):
        if count_list[num] == max_count:
            if answer != 0 and answer != num:
                return -1
            else:
                answer = num
    return answer


array1: List[int] = [1, 2, 3, 3, 3, 4]
array2: List[int] = [1, 1, 2, 2]
array3: List[int] = [1]

print(solution(array1))
print(solution(array2))
print(solution(array3))
