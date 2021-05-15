# 시저 암호
# 어떤 문장의 각 알파벳을 일정한 거리만큼 밀어서 다른 알파벳으로 바꾸는 암호화 방식
# 1차 시도 통과

import string

def solution(s, n):
    upper = string.ascii_uppercase
    lower = string.ascii_lowercase
    answer = ''

    for i in s:
        if i == ' ':
            answer += ' '
        else:
            if i.islower():
                answer += lower[(lower.find(i)+n) % 26]
            else:
                answer += upper[(upper.find(i)+n) % 26]

    return answer

print(solution('AB', 1))
print(solution("z", 1))
print(solution("a B z", 4))


'''
타인풀이

def caesar(s, n):
    s = list(s)
    for i in range(len(s)):
        if s[i].isupper():
            s[i]=chr((ord(s[i])-ord('A')+ n)%26+ord('A'))
        elif s[i].islower():
            s[i]=chr((ord(s[i])-ord('a')+ n)%26+ord('a'))

    return "".join(s)

    ** ord(a)는 문자의 아스키 코드값을 돌려주는 함수
    ** chr(a)는 아스키 코드값을 입력받아 그 코드에 해당하는 문자를 출력하는 함수
    '''
    