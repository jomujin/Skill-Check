# 디스크 컨트롤러
# 1차 시도 테스트 14 ~ 20 빼고 실패
# heap 저장을 작업의 소요시간, 작업의 총 소요시간 순으로 바꾸니까 정답
# 왜 작업의 총 소요시간이 아닌 작업의 소요시간 기준인지 모르겠음

import heapq as hp

def solution(jobs):

    jobs.sort()
    num = len(jobs)
    heap = []
    total_time = 0
    time = 0
    while jobs or heap:
        # time 보다 작은 요소가 있을때
        if jobs and jobs[0][0] <= time:
            for i in jobs[::]:
                if i[0] <= time:
                    hp.heappush(heap, [i[1], i[1] + (time - i[0])])
                    # time 보다 작은 원소를 heap에 저장 [작업의 소요시간, 작업의 총 소요시간]
                    jobs.pop(0)
            
        else: # time 보다 작은 요소가 없을때 += 1 반복
            time += 1

        # heap 원소가 있으면 가장 작은 i[0] 작업의 (소요시간을 기준으로 heapq 구조)
        if heap:
            i = hp.heappop(heap)
            time += i[0] # 시간에는 작업의 소요시간을 더해줌
            total_time += i[1] # 총시간에는 작업의 총 시간을 더해줌
            if heap:
                for h in heap:
                    h[1] += i[0] 
                    # heapq의 각 원소에는 완료된 작업의 소요시간을 더해줌

        # print(jobs, heap, time, total_time)
    return total_time // num


print(solution([[0, 5], [1, 2], [5, 5]])) # 6
print(solution([[0, 3], [1, 9], [2, 6]])) # 9
print(solution([[0, 10], [2, 10], [9, 10], [15, 2]])) # 14
print(solution([[0, 10], [2, 12], [9, 19], [15, 17]])) # 25
print(solution([[0, 3], [1, 9], [2, 6]])) # 9
print(solution([[0, 1]])) # 1
print(solution([[1000, 1000]])) # 1000
print(solution([[0, 1], [0, 1], [0, 1]])) # 2
print(solution([[0, 1], [0, 1], [0, 1], [0, 1]])) # 2
print(solution([[0, 1], [1000, 1000]])) # 500
print(solution([[100, 100], [1000, 1000]])) # 550
print(solution([[10, 10], [30, 10], [50, 2], [51, 2]])) # 6
print(solution([[0, 3], [1, 9], [2, 6], [30, 3]])) # 7


# 첫번째꺼를 원소를 하고
# 첫번째 원소의 소요시간 - 작업 요청시간 = 현재까지 대기시간
# 현재부터 이후 예상 대기시간은 각 작업의 작업시간
# 즉 첫번째꺼를 완료한 시점에 각 요청작업의 소요시간은
# 2번째 원소는 3 - 1 + 9 = 11 
# 3번재 원소는 3 - 2 + 6 = 7
# 총 소요시간이 짧은걸 우선적으로 ?


'''
def solution(jobs):

    jobs.sort()
    num = len(jobs)
    heap = []
    total_time = 0
    time = 0
    while jobs or heap:
        # time 보다 작은 요소가 있을때
        if jobs and jobs[0][0] <= time:
            for i in jobs[::]:
                if i[0] <= time:
                    hp.heappush(heap, [i[1] + (time - i[0]), i[1]])
                    # time 보다 작은 원소를 heap에 저장 [작업의 총 소요시간, 작업의 소요시간]
                    jobs.pop(0)
            
        else: # time 보다 작은 요소가 없을때 += 1 반복
            time += 1

        # heap 원소가 있으면 가장 작은 i[0] 작업의 (총 소요시간을 기준으로 heapq 구조)
        if heap:
            i = hp.heappop(heap)
            # print(i)
            time += i[1] # 시간에는 작업의 소요시간을 더해줌
            total_time += i[0] # 총시간에는 작업의 총 시간을 더해줌
            if heap:
                for h in heap:
                    h[0] += i[1] 
                    # heapq의 각 원소에는 완료된 작업의 소요시간을 더해줌

        print(jobs, heap, time, total_time)
    return total_time // num

'''