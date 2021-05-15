# 구명보트
# 1차 시도 20점, 효율성 10점
# 4차 시도 통과

# 통과
# 정확성 테스트는 대부분 2ms 이내, 효율성 테스트 약 11~14ms
# for 문의 사용을 최소화하도록 계산
# 중요한건 오름차순정렬로 해서 큰수부터 나오게 하고
# 맨마지막값(즉 가장작은값)과 합계가 limit 이하일때는 end값(people[-n]) 뒤쪽에서 불러오는 값이
# 점점 작아지게해서 이후 계산에서 i >= len(people) - end 를 만족하면 종료되도록 함
def solution(people, limit):
    people = sorted(people, reverse=True)
    answer = 0
    end = -1
    for i in range(len(people)):
        if people[i] + people[end] <= limit:
            end -= 1  

        answer += 1

        if i >= len(people) + end:
            break
    return answer


# 이전 시도 정확성 통과(75점), 효율성 10점, 탐욕법으로 계속 효율성에서 실패했음
def solution_0(people, limit):
    people.sort()

    answer = 0
    while people:
        a = people.pop()
        l = limit - a
        count = 1
        if l >= 40:
            for i in people[:]:
                if people and l >= i and count < 3:
                    l -= i
                    people.remove(i)
                    count += 1
                else:
                    continue
        answer += 1
    return answer


def solution_1(people, limit):
    answer = 0
    weight = 0
    for p in sorted(people):
        if weight + p <= limit:
            weight += p
        else:
            weight = p
            answer += 1

    return answer + 1


# 정확성 통과, 효율성 실패,, pop도 빼고 했는데도 효율성 실패함
# sort를 빼야하는건가
def solution_2(people, limit):
    answer = 0
    people.sort()

    while people:
        if people[0] + people[-1] <= limit:
            people = people[1:-1]
        else:
            people = people[:-1]        

        answer += 1
    return answer


# 최대 2명만 탈 수 있으므로 limit // 2 를 기준값으로 잡고 smaller, bigger 그룹으로
# 나눈뒤 계산했지만 정답과 다른 경우 다수 발생
import math
def solution_3(people, limit):
    smaller = 0
    bigger = 0
    for p in people:
        if p > limit // 2:
            bigger += 1
        else:
            smaller += 1

    return math.ceil(smaller/2) + bigger
    

print(solution([70, 50, 80, 50], 100))
print(solution([70, 50, 80], 100))



'''
타인풀이
내 정답풀이보다 더 빠름 정확성 테스트에서는 1ms내외, 효율성에서는 8~9ms

def solution(people, limit) :
    answer = 0
    people.sort()

    a = 0
    b = len(people) - 1
    while a < b :
        if people[b] + people[a] <= limit :
            a += 1
            answer += 1
        b -= 1
    return len(people) - answer

'''