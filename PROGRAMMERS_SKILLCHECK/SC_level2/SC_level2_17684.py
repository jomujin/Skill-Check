# 압축
# 1차 시도 통과


import string

def solution(msg):
    
    DIC = {i : idx+1 for idx, i in enumerate(string.ascii_uppercase)}
    a = msg
    answer = []
    while len(a) > 0:
        for i in range(len(a)):
            # 사전에 현재 입력과 일치하는 문자열이 있을 경우 (한글자는 무조건 있으므로 패스)
            if len(a) > 1 and i+1 < len(a) and a[:i+1] in DIC.keys():
                continue

            # 마지막 여러글자일때
            elif len(a) > 1 and i+1 == len(a) and a[:i+1] in DIC.keys():
                answer.append(DIC[a[:i+1]])
                a = ''
                break

            # 마지막 한글자일때
            elif len(a) == 1:
                answer.append(DIC[a[:i+1]])
                a = ''
                break

            # 사전에 현재 입력과 일치하는 문자열이 없을 경우
            # 이전에 있었던 문자열까지 출력하고 
            # 다음 글자 문자열을 합친 문자열을 DIC에 추가
            # 입력된 글자만큼 msg에서 문자 삭제    
            else:
                answer.append(DIC[a[:i]])
                if a[:i+1] not in DIC.keys():
                    DIC[a[:i+1]] = len(DIC)+1
                a = a[i:]
                break

        # print(a, answer)

    return answer

# print(solution('KAKAO'))
# print(solution('TOBEORNOTTOBEORTOBEORNOT'))
# print(solution('ABABABABABABABAB'))
print(solution('"THATTHATISISTHATTHATISNOTISNOTISTHATITITISTHATTHATISISTHATTHATISNOTISNOTISTHATITITISTHATTHATISISTHATTHATISNOTISNOTISTHATITITISTHATTHATISISTHATTHATISNOTISNOTISTHATITITISTHATTHATISISTHATTHATISNOTISNOTISTHATITITISTHATTHATISISTHATTHATISNOTISNOTISTHATITITISTHATTHATISISTHATTHATISNOTISNOTISTHATITITISTHATTHATISISTHATTHATISNOTISNOTISTHATITITISTHATTHATISISTHATTHATISNOTISNOTISTHATITITISTHATTHATISISTHATTHATISNOTISNOTISTHATITITISTHATTHATISISTHATTHATISNOTISNOTISTHATITITISTHATTHATISISTHATTHATISNOTISNOTISTHATITITISTHATTHATISISTHATTHATISNOTISNOTISTHATITITISTHATTHATISISTHATTHATISNOTISNOTISTHATITITISTHATTHATISISTHATTHATISNOTISNOTISTHATITITISTHATTHATISISTHATTHATISNOTISNOTISTHATITITISTHATTHATISISTHATTHATISNOTISNOTISTHATITITISTHATTHATISISTHATTHATISNOTISNOTISTHATITITISTHATTHATISISTHATTHATISNOTISNOTISTHATITITISTHATTHATISISTHATTHATISNOTISNOTISTHATITITISTHATTHATISISTHATTHATISNOTISNOTISTHATITITISTHATTHATISISTHATTHATISNOTISNOTISTHATITITISTHATTHATISISTHATTHATISNOTISNOTISTHATITITIS"'))


'''
타인풀이 

def solution(msg):
    answer = []
    tmp = {chr(e + 64): e for e in range(1, 27)}
    num = 27
    while msg:
        tt = 1
        while msg[:tt] in tmp.keys() and tt <= msg.__len__():
            tt += 1
        tt -= 1
        if msg[:tt] in tmp.keys():
            answer.append(tmp[msg[:tt]])
            tmp[msg[:tt + 1]] = num
            num += 1
        msg = msg[tt:]
    return answer
    
    '''