# 자릿수 더하기
# 1차 시도 통과


def solution(n):
    answer = 0
    for i in str(n):
        answer += int(i)
    return answer

print(solution(123))


def solution_2(n):
    return sum(list(int(i) for i in str(n)))

print(solution_2(123))


'''
타인풀이
재귀구조로 풀이

def solution_3(n):
    if n < 10:
        return n
    return (n % 10) + solution_3(n // 10)

print(solution_3(123))

'''