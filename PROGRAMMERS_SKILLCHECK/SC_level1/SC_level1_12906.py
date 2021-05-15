# 같은 숫자는 싫어
# 한번에 통과함, 단 한번에 삭제하지 못하고 
# arr의 원소에 해당하지 않는 문자열 '*'로 변환한 후 '*'을 빼고 다시 리스트를 만드는 방식으로 진행함
# 효율성 테스트도 통과했지만 더 좋은 방법이 있을것으로 예상됨

def solution(arr):
    for i in range(1, len(arr)):
        if arr[i-1] == arr[i]:
            arr[i-1] = "*"

    answer = list(i for i in arr if str(i).isalnum() == True)
    return answer

print(solution([1,1,3,3,0,1,1]))
print(solution([4,4,4,3,3]))
    

'''
타인풀이

def solution_2(arr):
    answer = []
    for i in arr:
        if answer[-1:] == [i]: continue
        answer.append(i)

    return answer

'''

class Arr:
    def __init__(self, arr):
        self.arr = arr

    def resort(self):
        answer = []
        for i in self.arr:
            if answer[-1:] == [i]: continue
            answer.append(i)
        return answer

def solution_2(arr):
    arr = Arr(arr)
    return arr.resort()

print(solution_2([1,1,3,3,0,1,1]))