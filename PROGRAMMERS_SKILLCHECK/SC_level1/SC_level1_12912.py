# 두 정수 사이의 합
# 1차 시도 통과


class Ih:
    def __init__(self, a, b):
        if b < a:
            a, b = b, a
        self.list = list(range(a, b+1))

    def sum(self):
        return sum(self.list)

def solution(a, b):
    x = Ih(a, b)
    return x.sum()

print(solution(3, 5))
print(solution(5, 3))


'''
타인풀이

def adder(a, b):
    return (abs(a-b)+1)*(a+b)//2

abs 절대값 함수 이용
효율성 측면에서 가장 좋을듯

'''