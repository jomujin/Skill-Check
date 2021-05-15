# 소수찾기
# 1차 시도 테스트 11 시간초과, 효율성 테스트 1~4 실패
# 2차 시도 효율성 테스트 1~4 실패
# 3차 시도 통과
# 변경내용
# 소수찾는 함수 def find_pn(m)의 범위설정에서 2,3을 먼저하게 하는것이 중요했음
# 이유는 2,3,5의 배수들을 빠르게 제거할 수 있으므로,,
# for i in range(2, x+1) x+1를 한 이유는
# 4의 제곱근의 경우 int()하면 내림이 되어 2가 됨
# 2와 3의 배수는 solution 함수에서 제외해줬으므로
# find_pn 실행값의 최소인 4부터는 range 범위 설정이 올바르게 하기위해서는 x+1이 필요했음


import math

def find_pn(m):
    x = int(math.sqrt(m))
    for i in range(2, x+1):
        if m % i == 0:
            # print("{}은 소수가 아닙니다.".format(m))
            return False
    return True 

def solution(n):
    prime_number = []
    for i in range(2, n+1):
        if i == 2 or i == 3:
            prime_number.append(i)
        else:
            if i % 2 != 0 and find_pn(i) == True:
                prime_number.append(i)
    
    return prime_number

print(solution(10))
print(solution(5))


'''
타인풀이

def solution(n):
    num=set(range(2,n+1))

    for i in range(2,n+1):
        if i in num:
            num-=set(range(2*i,n+1,i))
    return len(num)

    ** set(range(2, n+1)) 만든 후 반복문으로 i 의 배수 set 삭제
효율성 테스트 결과 내 풀이보다 약 8~10배 빠름

'''

def solution2(n):
    num = set(range(2, n+1))

    for i in range(2, int(n**0.5)+1):
        if i in num:
            num2 = set(range(2*i, n+1, i))
            num -= num2

    return num

print(solution2(10))
print(solution2(100))