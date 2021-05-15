# 최댓값과 최솟값
# 1차 시도 통과


def solution(s):
    s_list = [int(_) for _ in s.split(' ')]
    return str(min(s_list)) + ' ' + str(max(s_list))


print(solution('1 2 3 4'))
print(solution('-1 -2 -3 -4'))