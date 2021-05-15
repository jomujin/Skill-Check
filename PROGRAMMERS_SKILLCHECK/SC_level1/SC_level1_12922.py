# 수박수박수박수박수박수?
# 1차 시도 통과


def solution(n):
    return ("수박" * (n // 2 + 1))[:n]

print(solution(3))