# 예산
# 1차 시도 52.5점 테스트 7 ~ 17 실패(시간초과) combinations이 시간초과의 이유인것 같음
# 2차 시도 sorted or sort로 정렬 후 하나씩 더해서 budget을 넘으면 return answer
# (sorted로 해서 pop()하는 방식으로 했지만 틀림으로 떴음 왜인지는 모르겠음)
# pop을 빼고 for 문으로 실행시 통과


def solution(d, budget):
    spend = 0
    answer = 0
    if sum(d) <= budget: return len(d)
    for i in sorted(d):
        spend += i
        if spend > budget:
            return answer
        answer += 1


# itertools.combinations 실패(시간초과)
# def solution(d, budget):
#     import itertools
#     if sum(d) <= budget: return len(d)
#     for i in range(len(d)-1, 0, -1):
#         for j in itertools.combinations(d, i):
#             if sum(j) <= budget:
#                 return i
#     return 0


# sorted & pop 실패
# def solution(d, budget):
#     answer = len(d)
#     spend = sum(d)
#     if sum(d) <= budget: return len(d)
#     while sorted(d):
#         spend -= d.pop()
#         answer -= 1
#         if spend <= budget:
#             return answer 

print(solution([2,3,2,5,4], 9))
print(solution([2,2,3,3], 9))