# 다트 게임
# 1차 시도 통과
# 점수 변환 조건인 S, D, T, *, #을 dict로 해당되는 숫자로 연결
# 처음에는 문자열로 '**-1' 이런식으로 변환하여 하려했으나 이런 기호가 포함된 문자열은 int() 불가해 변경함
# 점수의 범위가 0~10까지라 10의 경우 '.'로 replace하여 처리함
# 전체적인 속도(0.02~0.03ms)


def solution(dartResult):
    dartResult = dartResult.replace('10', '.')
    answer = []
    exc = {'S':1, 'D':2, 'T':3, '*':2, '#':-1} 
    
    for i in dartResult:
        if i.isalpha():
            answer[-1] = answer[-1] ** exc[i]
        elif i.isdigit():
            answer.append(int(i))
        else:
            if i == '.':
                answer.append(10)
            elif len(answer) > 1 and i == '*':
                answer[-1], answer[-2] = answer[-1] * exc[i], answer[-2] * exc[i]
            elif len(answer) == 1 and i == '*':
                answer[-1] = answer[-1] * exc[i]
            else:
                answer[-1] = answer[-1] * exc[i]

    return sum(answer)

print(solution('1S2D*3T'))
print(solution('1D2S#10S'))
print(solution('1D2S0T'))
print(solution('1S*2T*3S'))
print(solution('1D#2S*3S'))
print(solution('1T2D3D#'))
print(solution('1D2S3T*'))


'''
타인풀이 (정규표현식, 전체적인 처리 속도 (0.20~0.30ms))

import re

def solution(dartResult):
    bonus = {'S' : 1, 'D' : 2, 'T' : 3}
    option = {'' : 1, '*' : 2, '#' : -1}
    p = re.compile('(\d+)([SDT])([*#]?)')
    dart = p.findall(dartResult)
    for i in range(len(dart)):
        if dart[i][2] == '*' and i > 0:
            dart[i-1] *= 2
        dart[i] = int(dart[i][0]) ** bonus[dart[i][1]] * option[dart[i][2]]

    answer = sum(dart)
    return answer

'''
