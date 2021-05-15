# 비밀지도
# 1차 시도 실패
# 2차 시도 통과
# zfill(n)을 통해 n자리 미만인 요소는 0을 추가하고 replace 진행


def solution(n, arr1, arr2):
    answer = []
    arr1 = [int(format(i, 'b')) for i in arr1]
    arr2 = [int(format(i, 'b')) for i in arr2]
    result = [str(x+y) for x,y in zip(arr1, arr2)]
    # print(arr1, arr2, result, sep='\n')
    for i in result:
        answer.append(i.zfill(n).replace('2', '#').replace('1', '#').replace('0', ' '))
    return answer
                
                
print(solution(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28]))
print(solution(6, [46, 33, 33, 22, 31, 50], [27, 56, 19, 14, 14, 10]))


'''
타인풀이

def solution(n, arr1, arr2):
    answer = []
    for i,j in zip(arr1,arr2):
        a12 = str(bin(i|j)[2:])
        a12=a12.rjust(n,'0')
        a12=a12.replace('1','#')
        a12=a12.replace('0',' ')
        answer.append(a12)
    return answer

    ** a12 = str(bin(i|j)[2:])
    ** | 는 비트연산자 (or 연산) 비트연산자를 사용하면 이진수로 바꾸어서 연산이 됨
    ** rjust(n, '0') zfill과 다르게 원하는 단어로 n - len(대상) 수만큼 채울수 있음

    비트연산자 종류

    & / AND 연산 / 둘 다 1이면 1
    | / OR 연산 / 하나만 1이어도 1
    ^ / XOR 연산 / 하나만 1일 경우 1
    ~ / Not 연산 / 0이면 1, 1이면 0
    << / 왼쪽 시프트 연산 / 지정된 수만큼 오른쪽 끝에 0을 채우고 넘치는 왼쪽 끝 숫자는 제거
    >> / 오른쪽 시프트 연산 / 지정된 수만큼 왼쪽 끝에 0을 채우고 넘치는 오른쪽 끝 숫자는 제거
'''