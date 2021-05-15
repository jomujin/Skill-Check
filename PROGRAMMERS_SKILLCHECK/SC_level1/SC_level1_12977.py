# 소수 만들기
# 1차 시도 23.1점
# 2차 시도 통과
# 소수가 나오는 모든 경우의 수를 구해야 되는데, set로 중복되는 소수를 제거해서 값이 달랐음


import itertools

def prime_number(n):
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def solution(nums):
    result = 0
    arr = itertools.combinations(nums, 3)
    for a in arr:
        if prime_number(sum(a)) == True:
            result += 1

    return result


print(solution([1,2,3,4]))
print(solution([1,2,7,6,4]))


