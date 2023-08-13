# https://school.programmers.co.kr/learn/courses/30/lessons/120924

def solution(common):
    gap = common[1] - common[0]
    if common[2] - common[1] == gap:
        return common[len(common) - 1] + gap
    else:
        return common[len(common) - 1] * (common[1] // common[0])

print(solution([1, 2, 3, 4]))
print(solution([2, 4, 8]))