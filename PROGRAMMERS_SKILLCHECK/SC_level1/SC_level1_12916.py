# 문자열 내 p와 y의 개수
# 1차 시도 통과


def solution(s):
    s = s.lower()
    count_p = s.count('p')
    count_y = s.count('y')
    if count_p == count_y:
        return True
    return False

class PY:
    def __init__(self, s):
        self.s = s.lower()
        self.cp = self.s.count('p')
        self.cy = self.s.count('y')

    def compare(self):
        if self.cp == self.cy:
            return True
        return False

def solution_2(s):
    s = PY(s)
    return s.compare()

print(solution_2("pPoooyY"))


'''
타인풀이

def solution_3(s):
    return s.lower().count('p') == s.lower().count('y')

== 가 결과값에서 이미 True와 False를 반환하기때문에 위처럼 할 필요가 없음
'''