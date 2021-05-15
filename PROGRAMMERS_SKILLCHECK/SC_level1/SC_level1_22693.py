# 문자열을 정수로 바꾸기
# 1차 시도 통과


def solution(s):
    return int(s)


'''
타인풀이


def solution_2(s):
    answer = 0
    for idx, i in enumerate(s[::-1]):
        if i == '-':
            answer = int(answer) * -1
        else:
            answer += (10 ** idx) * int(i)

    return answer

'''