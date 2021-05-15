# 문자열 다루기 기본
# 1차 시도 통과
# class로 해서는 일부 실패
# cleck_num에서 return False로 할 경우 solution_2(s)에서는
# S.check_num()의 결과값 True, False가 S.check_digit()의 진행여부만 판단하다보니
# return False가 출력되지 않았음
# 이를 solution_2(s)에서 else 값에 return False를 추가하여 수정


def solution(s):
    if len(s) == 4 or len(s) == 6:
        return s.isdigit()
    return False

print(solution('a234'))


class Str:
    def __init__(self, word):
        self.word = word
        self.num_word = len(word)
        # self.check_digit()
        # self.check_num()

    def check_digit(self):
        return self.word.isdigit()

    def check_num(self):
        if self.num_word == 4 or self.num_word == 6:
            return True

def solution_2(s):
    S = Str(s)
    if S.check_num():
        return S.check_digit()
    return False


'''
타인풀이

def alpha_string46(s):
    return s.isdigit() and len(s) in [4,6]

    ** and len(s) in (4,6)


def alpha_string46(s):
    try:
        int(s)
    except:
        return False
    return len(s) == 4 or len(s) == 6 

    ** try int(s)
'''
