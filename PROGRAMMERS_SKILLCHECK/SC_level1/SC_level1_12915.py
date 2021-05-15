# 문자열 내 마음대로 정렬하기
# 1차 시도 실패(이유 인덱스 n의 문자가 같은 문자열이 여럿일 경우, 사전순으로 정렬)
# 2차 시도 58.3점 
# 3차 정답

# 1차 작성 코드
# def solutino(strings, n):
#     return sorted(a, key = lambda x: x[1])

# 2차 작성 코드
# def solution(strings, n):
#     answer = sorted(strings, key = lambda x:x[n])
#     for i in range(1, len(answer)):
#         if answer[i-1][n] == answer[i][n]:
#             if answer[i-1] > answer[i]:
#                 answer[i-1], answer[i] = answer[i], answer[i-1]


# 3차 작성 코드 (bubble sort? 방법 적용)
def solution(strings, n):
    answer = sorted(strings, key = lambda x:x[n])
    for i in range(len(answer)):
        for j in range(i+1, len(answer)):
            if answer[i][n] == answer[j][n]:
                if answer[j] < answer[i]:
                    answer[j], answer[i] = answer[i], answer[j]
    return answer

print(solution(["abce", "abcd", "cdx"], 2))


'''
타인풀이

def solution(strings, n):
    return sorted(strings, key = lambda x: x[n]+x[:])

** 재정렬 할 필요없이 +x[:]하면 글자 크기순으로 정렬됨

'''