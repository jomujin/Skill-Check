# 이상한 문자 만들기
# 1차 시도 통과


def solution(s):
    arr = s.split(' ')
    answer = []
    for a in arr:
        word = ''
        for i in range(len(a)):
            if i % 2 == 0:
                word += a[i].upper()
            else:
                word += a[i].lower()
        answer.append(word)

    return ' '.join(answer)

print(solution("try hello world"))


'''
타인풀이

def toWeirdCase(s):
    res = []
    for x in s.split(' '):
        word = ''
        for i in range(len(x)):
            c = x[i].upper() if i % 2 == 0 else x[i].lower()
            word = word + c
        res.append(word)
    return ' '.join(res)

    ** 전체적으로 유사하지만
    c = x[i].upper() if i % 2 == 0 else x[i].lower()
    한줄로 처리하는것이 좋아보임
    '''