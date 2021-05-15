# N으로 표현
# 이러한 방법은 ex) 6이 나오는 경우의 수 (1,5), (2,4), (3,3), (4,2), (5,1) 처럼
# (3,3)까지를 제외하고는 중복된 값을 출력한다. 
# 이러한 시간을 단축하기 위해서는 범위를 //2+1 하면되나,
# 그럴경우, 빼기와 나누기의 경우 추가 설정해줘야 한다.
# 빼기와 나누기는 x - y, y - x, x / y, y / x처럼 순서에 따라 값이 달라지기 때문

# def solution(N, number):
#     answer = -1
#     S = [set() for _ in range(8)]
#     for idx, i in enumerate(S):
#         S[idx].add(int(str(N)*(idx+1)))
#     for i in range(len(S)):
#         for j in range(i):
#             for x in S[j]:
#                 for y in S[i-j-1]:
#                     S[i].add(x + y)
#                     S[i].add(x - y)
#                     S[i].add(x * y)
#                     if y != 0:
#                         S[i].add(x // y)
        
#         if number in S[i]:
#             answer = i + 1
#             return answer
#     return answer

# print(solution(5, 12))
# print(solution(2, 11))


# 시간은 훨씬 빠름, 근데 테스트 1,8 실패
def solution(N, number):
    answer = -1
    S = [set() for _ in range(8)]
    for idx, i in enumerate(S):
        S[idx].add(int(str(N)*(idx+1)))
    for i in range(len(S)):
        for j in range(int(i/2)):
            for x in S[j]:
                for y in S[i-j-1]:
                    S[i].add(x + y)
                    S[i].add(x - y)
                    S[i].add(y - x)
                    S[i].add(x * y)
                    if y != 0:
                        S[i].add(x // y)
                    if x != 0:
                        S[i].add(y // x)
        
        if number in S[i]:
            answer = i + 1
            return answer
    return answer

    
print(solution(5, 12))
print(solution(2, 11))
