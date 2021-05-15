# 신규 아이디 추천
# 아이디 규칙
# 아이디의 길이는 3자 이상 15자 이하여야 합니다.
# 아이디는 알파벳 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.) 문자만 사용할 수 있습니다.
# 단, 마침표(.)는 처음과 끝에 사용할 수 없으며 또한 연속으로 사용할 수 없습니다.

# 처리과정
# 1단계 new_id의 모든 대문자를 대응되는 소문자로 치환합니다.
# 2단계 new_id에서 알파벳 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.)를 제외한 모든 문자를 제거합니다.
# 3단계 new_id에서 마침표(.)가 2번 이상 연속된 부분을 하나의 마침표(.)로 치환합니다.
# 4단계 new_id에서 마침표(.)가 처음이나 끝에 위치한다면 제거합니다.
# 5단계 new_id가 빈 문자열이라면, new_id에 "a"를 대입합니다.
# 6단계 new_id의 길이가 16자 이상이면, new_id의 첫 15개의 문자를 제외한 나머지 문자들을 모두 제거합니다.
#      만약 제거 후 마침표(.)가 new_id의 끝에 위치한다면 끝에 위치한 마침표(.) 문자를 제거합니다.
# 7단계 new_id의 길이가 2자 이하라면, new_id의 마지막 문자를 new_id의 길이가 3이 될 때까지 반복해서 끝에 붙입니다.

# 1차 73.1점 (테스트 4, 14, 16, 17, 20, 21, 25 실패)
# 2차 통과 (3단계를 잘못이해함, '..', '...'와 같이 점이 2개 이상인경우 모두 '.'로 변환해야 함)


def chapter_3(word):
    wordlist = []
    for i in word:
        if wordlist and i == '.' and wordlist[-1] == i:
            continue
        wordlist.append(i)
    return ''.join(wordlist)

def chapter_4(word):
    # return False 로 안하고 return word로 해도 while문에 문제가 없음
    # 자동으로 if와 elif를 True로 인식하는건지는 모르겠음
    while True and word:
        if word[0] == '.':
            word = word[1:]
        elif word[len(word)-1] == '.':
            word = word[:len(word)-1]
        elif word[0] == '.' and word[len(word)-1] == '.':
            word = word[1:len(word)-1]
        else:
            return word

def solution(new_id):
    # 1단계
    new_id = new_id.lower()

    # 2단계
    for i in new_id:
        if i.isalnum() or i.isalpha() or i == '-' or i == '_' or i == '.':
            continue
        new_id = new_id.replace(i, '')
    
    # 3단계
    new_id = chapter_3(new_id)

    # 4단계
    new_id = chapter_4(new_id)

    # 5단계
    if new_id == None:
        new_id = 'a'

    # 6단계
    if len(new_id) > 15:
        new_id = new_id[:15]
    
    new_id = chapter_4(new_id)

    # 7단계
    if len(new_id) < 3:
        new_id = (new_id + new_id[-1] * 3)[:3]

    return new_id

print(solution("...!@BaT#*..y.abcdefghijklm"))
print(solution("z-+.^."))
print(solution("=.="))
print(solution("123_.def"))
print(solution("abcdefghijklmn.p"))


'''
타인풀이

import re

def solution(new_id):
    st = new_id
    st = st.lower()
    st = re.sub('[^a-z0-9\-_.]', '', st)
    st = re.sub('\.+', '.', st)
    st = re.sub('^[.]|[.]$', '', st)
    st = 'a' if len(st) == 0 else st[:15]
    st = re.sub('^[.]|[.]$', '', st)
    st = st if len(st) > 2 else st + "".join([st[-1] for i in range(3-len(st))])
    return st

'''
