# 3진법 뒤집기
# 1차 시도 통과


def solution(n):
    answer = 0
    th = ''
    # while n: 으로 하면 자연스럽게 n // 3 == 0 이 되면 멈춤
    while n:
        th += str(n % 3)
        n = n // 3

    for i in range(len(th[::-1])):
        answer += int(th[::-1][i]) * (3**i)

    return answer

print(solution(45))

'''
타인풀이

def solution(n):
    tmp = ''
    while n:
        tmp += str(n % 3)
        n = n // 3

    answer = int(tmp, 3)
    # int('0021', 3) 하면 자동으로 3진수 역계산이 되서 나옴
    return answer 

'''

# class로 풀기

class Three:
    def __init__(self, num):
        self.num = num
        self.th = ''

    def trans_th(self):
        while self.num:
            self.th += str(self.num % 3)
            self.num = self.num // 3
    
    def trans_re(self):
        return int(self.th, 3)

def solution_2(n):
    n = Three(n)
    n.trans_th()
    return n.trans_re()

print(solution_2(45))
    