# 자연수 뒤집어 배열로 만들기
# 1차 시도 통과


def solution(n):
    return [int(_) for _ in str(n)[::-1]]

print(solution(12345))


# 재귀구조로 풀이해봄
# 이 방법이 시간이 2~3배 가량 유리한듯

answer = []
def solution_2(n):
    if n < 10:
        answer.append(n)
    else:
        answer.append(n % 10)
        return solution_2(n // 10)

    return answer

print(solution_2(12345))