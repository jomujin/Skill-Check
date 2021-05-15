# 나누어 떨어지는 숫자 배열
# 1차 시도 통과


def solution(arr, divisor):
    answer = list(i for i in arr if i % divisor == 0)
    if len(answer) == 0:
        return [-1]
    return sorted(answer)

print(solution([5, 9, 7 ,10], 5))


'''
타인풀이

def solution(arr, divisor): return sorted([n for n in arr if n%divisor == 0]) or [-1]

한줄풀이
return sorted([n for n in arr if n % divisor == 0]) or [-1]
list_a or list_b는 
list_a가 거짓일때 list_b가 호출됨
즉 list_a가 비어있을때 list_b 호출

'''