# 실패율
# 1차 시도 70.4점 테스트 일부 실패(런타임에러)
# 효율성 측면 안좋아보임
# 2차 시도 통과
# 놓친 부분 : 스테이지에 도달한 유저가 없는 경우 해당 스테이지의 실패율은 0으로 정의한다는 문구의 해석
# 즉, 모든 스테이지에 대해 계산해야되는데 stages에 없는숫자는 패스하도록 설정해서 실패함
# 여전히 효율성 측면은 안좋음
# 조건 스테이지 개수 N은 1 <= N <= 500, stages의 길이는 1 <= len(stages) <= 200000
# 이므로 최대 500 * 200000 계산이 필요할 수 있음


def solution(N, stages):
    answer = []
    users = len(stages)
    for i in range(1, N+1):
        
        if stages.count(i) > 0:
            failer = stages.count(i)
            answer.append((i, failer / users))
            users -= failer
        else:
            answer.append((i, 0))
    return [i[0] for i in sorted(answer, key = lambda x: x[1], reverse=True)]
    # return [i[0] for i in sorted(answer, key = lambda x: x[1]+x[0], reverse=True)]
    # 조건을 x[1]+x[0]으로 했으나 자동으로 순서정렬(즉 안정정렬)이 되어 삭제함

# print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))
# print(solution(4, [4,4,4,4,4]))
print(solution(10, [2, 1, 2, 6, 2, 4, 3, 3]))
    

