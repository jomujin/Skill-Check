# 정수 제곱근 판별
# 1차 시도 통과


def solution(n):
    if n % (n ** 0.5) == 0:
        return int(n**0.5+1)**2
    return -1

print(solution(121))

# 나머지에 대한 Boolean
# 10 % 2 == True  >>> False
# 10 % 2 == False  >>> True
# 10 % 3 == True  >>> True

# 즉 나머지가 있어야 True, 나머지가 없으면 False

def solution_2(n):
    if n % (n ** 0.5) == False:
        return int(n**0.5+1)**2
    return -1


def solution_3(n):
    return n == int(n**.5)**2 and int(n**.5+1)**2 or -1
    # return 에서 or / and 의 의미
    # A and B 
    # A,B 둘 다 참이면 B를 출력
    # A,B 둘 다 거짓이면 A를 출력
    # A,B 둘 중에 하나만 참이면 거짓인 값을 출력
    # A or B
    # A,B 둘 다 참이면 A를 출력
    # A,B 둘 다 거짓이면 B를 출력
    # A,B 둘 중에 하나만 참이면 참인 값을 출력