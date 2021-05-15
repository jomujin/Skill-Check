# 정수 내림차순으로 배치하기
# 여러가지 sort 방식으로 시도해봄
# bubble sort 방식으로
# 1차 시도 93.8점 테스트 7 실패


def solution(n):
    n_ = [_ for _ in str(n)]
    n_n = len(n_)

    if n_n <= 1:
        return n_

    for i in range(n_n-1):
        for j in range(i+1, n_n):
            if n_[i] < n_[j]:
                n_[i], n_[j] = n_[j], n_[i]

    return int(''.join(n_))

print(solution(118372))


# quick sort 방식으로
def solution_2(n):

    def quick_sort(arr):
        if len(arr) <= 1:
            return arr

        low, mid, high = [], [], []
        mid_n = arr[len(arr) // 2]

        for i in arr:
            if i > mid_n:
                high.append(i)
            elif i < mid_n:
                low.append(i)
            else:
                mid.append(i)
        return quick_sort(high) + mid + quick_sort(low)

    n_ = [_ for _ in str(n)]
    return int(''.join(quick_sort(n_)))
    
print(solution_2(118372))


# quick sort 방식으로
# 시간 초과

def solution_3(n):
    arr = [_ for _ in str(n)]

    if len(arr) <= 1:
        return arr

    low, mid, high = [], [], []
    mid_n = arr[len(arr) // 2]

    for i in arr:
        if i > mid_n:
            high.append(i)
        elif i < mid_n:
            low.append(i)
        else:
            mid.append(i)
    return int(solution_3(high) + mid + solution_3(low))
    
print(solution_2(118372))


# 통과
# bubble sort와 무슨 차이인지 잘 모르겠음

def solution_4(n):
    return int(''.join(sorted([_ for _ in str(n)], reverse=True)))

    #** lisT('123456') >>> ['1', '2', '3', '4', '5', '6']
    #** sorted(str('123456')) >>> ['1', '2', '3', '4', '5', '6']