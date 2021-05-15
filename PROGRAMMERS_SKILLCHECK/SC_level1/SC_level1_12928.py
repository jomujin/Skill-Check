# 약수의 합
# 1차 시도 82.4점 테스트 1, 2, 12 실패
# 2차 시도 통과
# 1차 시도에 실패 이유 (36과 같이 약수가 1,2,3,6,12,18,36 일때 6이 중복으로 들어갔음)
# 따라서 i == self.n / i일 경우 한번만 더하도록 수정함


# 약수 trivial divisor
class Td:
    def __init__(self, n):
        self.n = n
    
    def make_list(self):
        answer = 0
        for i in range(1, int(self.n**0.5) + 1):
            if self.n % i == 0:
                if i == self.n / i:
                   answer = answer + i
                else:
                    answer = answer + i + self.n/i

        return int(answer)

def solution(n):
    n = Td(n)
    return n.make_list()

print(solution(12))
print(solution(5))
print(solution(6))
print(solution(36))

# 일반적인 방법 
# n+1 까지 for 문으로 나머지가 i인 값이 나올때마다 answer += i
# 단 위의 방법처럼
# 범위를 1부터 n의 제곱근 + 1까지 한 후 나머지가 i인 값이 나오면
# i와 n / i의 값이 다를 경우 두 값을 모두 answer 에 더하고
# i와 n / i의 값이 같을 경우 한 값만 answer 에 더하면
# for 문의 반복횟수가 많이 줄어들수 있음
# 시간또한 최대 위의방법 0.03ms으로 아래방법 0.27과 최대 10배 가량 차이남

def solution_2(n):
    answer = 0
    for i in range(n+1):
        if n % i == 0:
            answer += i
    return answer