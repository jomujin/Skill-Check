# 소수 찾기

# import itertools
# def prime_num(n):
#     for i in range(2, int(n**0.5)+1):
#         if n % i == 0:
#             return False
#     return True

# def solution(numbers):
#     answer = []
#     for i in range(1, len(numbers)+1):
#         for j in itertools.permutations(numbers, i):
#             num = int(''.join(j))
#             if num not in [1, 0] and num not in answer and prime_num(num) == True:
#                 answer.append(num)
    
#     return len(answer)

# print(solution('17'))
# print(solution('011'))


def solution(bridge_length, weight, truck_weights):
    truck_nums = len(truck_weights)
    loading = []
    complete = []
    now_weight = weight
    total_time = 0

    while len(complete) < truck_nums:
        # 다리에 있는 트럭 시간 확인
        if loading:
            for t in loading:
                    if t[1] >= bridge_length:
                        complete.append(t[0])
                        loading = loading[1:] # 한번에 한대만 나가므로
                        now_weight += t[0]
        total_time += 1

        # 다리 무게보다 적으면 트럭 추가
        if truck_weights and now_weight >= truck_weights[0]:
            now_weight = now_weight - truck_weights[0]
            now_truck = truck_weights.pop(0)
            loading.append([now_truck, 0])

        if loading:
            # 다리에 있는 트럭 시간 추가
            for t in loading:
                t[1] += 1
        
    return total_time

print(solution(2, 10, [7,4,5,6]))
print(solution(100, 100, [10]))