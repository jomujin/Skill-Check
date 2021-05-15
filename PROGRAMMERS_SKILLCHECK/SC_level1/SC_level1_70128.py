# 내적
# 1차 시도 통과


def solution(a, b):
    answer = 0
    for x, y in zip(a, b):
        answer += x * y

    return answer

