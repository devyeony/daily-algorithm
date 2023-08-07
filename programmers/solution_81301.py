# https://school.programmers.co.kr/learn/courses/30/lessons/81301

def solution(s):
    num_list = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    for i in range(0, len(num_list)):
        s = s.replace(num_list[i], str(i))
    return int(s)

print(solution('one4seveneight'))
print(solution('23four5six7'))
print(solution('2three45sixseven'))
print(solution('123'))