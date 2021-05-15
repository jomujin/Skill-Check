# 멀쩡한 사각형
# 1차 시도 50점
# 시도 공식 (x * y) -  (math.ceil(x/y) * y)
# 2차 시도 
# 시도 공식 (x * y) - (x + y - comn) comn = 공배수
# 이유는 모르겠으나, 5x3 에서 선에 걸치는 사각형의 개수는 5+3-1*(최대공약수)
# 4*7에서도 4+7-1*(최대공약수), 그 외 경우에도 동일함
# 예제인 8*12 에서는 8+12-4(8과 12의 최대공약수 4)

# import math

# def solution(w, h):
#     x, y = max(w, h), min(w, h)
#     return (x * y) -  (math.ceil(x/y) * y)


def solution(w, h):
    x, y = max(w, h), min(w, h)
    for i in range(y, 0, -1):
        if x % i == 0 and y % i == 0:
            comn = i
            break
    
    return (x * y) - (x + y - comn)


print(solution(17,8))
print(solution(3,5))


'''
타인풀이
최소공배수를 쓴 동일한 방법 적용이지만 gcd로 구함
import math

def gcd(a,b): return b if (a==0) else gcd(b%a,a)    
def solution(w,h): return w*h-w-h+gcd(w,h)

'''

def gcd(a,b):
    if a % b == 0:
        return b
    else:
        return gcd(b, a%b)
