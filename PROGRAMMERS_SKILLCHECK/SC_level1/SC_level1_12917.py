# 문자열 내림차순으로 배치하기
# 1차 시도 통과


def solution(s):
    answer = ''.join(sorted([i for i in s], reverse=True))

    # for i in range(len(s)-1):
    #     for j in range(i,len(s)):
    #         if s[i] < s[j]:
    #             s[i], s[j] = s[j], s[i]

    return answer

print(solution("Zbcdefg"))


'''
타인풀이

def solution(s):
    return ''.join(sorted(s, reverse=True))

    ** 문자열을 sorted()하면 list화 됨

'''