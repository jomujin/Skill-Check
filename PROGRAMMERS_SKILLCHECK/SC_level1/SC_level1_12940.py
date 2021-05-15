# 최대공약수와 최소공배수
# 1차 시도 87.5점 테스트 3, 16 실패
# 2차 시도 통과
# 실패했던 이유는 wihle, for 이중 반복문을 이용했는데
# while True로 진행하고 return True를 이용하니 중간에 for 문 탈출이 아닌 계속 True를 결과값으로 출력하였다
# 그래서 while n으로 변경한뒤 range를 n+1 부터 1까지 내려가게 진행하고
# i가 1이 되었을때 com_min과 com_max를 return 하도록 수정함


def solution(n, m):
    com_min = 1

    if n > m:
        n ,m = m, n

    while n:
        for i in range(n+1, 0, -1):
            if n % i == 0 and m % i == 0:
                com_min *= i
                n = int(n / i)
                m = int(m / i)
            if i == 1:
                return [com_min, com_min * n * m]


print(solution(3, 12))
print(solution(2, 5))
print(solution(250, 50))


'''
타인풀이

def gcdlcm(a, b):
    c, d = max(a, b), min(a, b)
    t = 1
    while t > 0:
        t = c % d
        c, d = d, t
    answer = [c, int(a*b/c)]

    return answer
'''

