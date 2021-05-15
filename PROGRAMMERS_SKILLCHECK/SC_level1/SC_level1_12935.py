# 제일 작은 수 제거하기
# 1차 시도 통과


def solution(arr):
    if len(arr) <= 1:
        return [-1]

    arr.pop(arr.index(min(arr)))
    return arr

print(solution([4,3,2,1]))


'''
타인풀이

def solution_2(arr):
    return [i for i in arr if i > min(arr)]


def solution_3(arr):
    arr.remove(min(arr))
    return arr
'''
