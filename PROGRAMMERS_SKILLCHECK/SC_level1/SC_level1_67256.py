# 키패드 누르기
# 1차 시도 통과
# numpy의 where (index 위치 확인함수) 이용
# str.find() 는 문자열에만 사용가능 / list.index() 은 1행 리스트만 가능한듯
# numpy.where()는 ('a')의 해당하는 모든 문자열을 찾아내기 때문에 주의해아하지만
# 해당 문제에서는 중복되는 index가 없어서 위치값을 구하기가 수월했음


import numpy as np

keypad = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9'], ['*', '0', '#']]
keypad = np.array(keypad)

def solution(number, hand):
    answer = ''
    h = hand.upper()[0]
    lo_L = '*'
    lo_R = '#'

    for i in number:
        if i in [1, 4, 7, '*']:
            answer += 'L'
            lo_L = str(i)
        elif i in [3, 6, 9, '#']:
            answer += 'R'
            lo_R = str(i)
        else:
            # 찾을 대상의 키패드 위치값, 왼손 위치값, 오른손 위치값
            x, y = np.where(keypad == str(i))[0], np.where(keypad == str(i))[1]
            lx, ly = np.where(keypad == lo_L)[0], np.where(keypad == lo_L)[1]
            rx, ry = np.where(keypad == lo_R)[0], np.where(keypad == lo_R)[1]

            # 절대값(abs)으로 계산한 거리차 구하기
            if abs(lx-x) + abs(ly-y) < abs(rx-x) + abs(ry-y):
                answer += 'L'
                lo_L = str(i)
            elif abs(lx-x) + abs(ly-y) > abs(rx-x) + abs(ry-y):
                answer += 'R'
                lo_R = str(i)
            else:
                answer += h
                if h == 'R':
                    lo_R = str(i)
                else:
                    lo_L = str(i)

    return answer

print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], 'right'))
print(solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2], 'left'))


'''
타인 풀이

numpy를 사용하지 않을경우의 대한 방법
dict를 이용해 1:(0,0), 2:(0,1), 3:(0,2),... 처럼 key에 index를, value에 좌표값을 이용하면 됨
list를 이용해서는 [(0,0), (0,1), (0,2), (1,0),...] 좌표값만 입력한 후
enumerate를 이용해 index값과 연결시키든지 함(단, 이경우 10 = '*', 11 = 0, 12 = '#'에 대해서는 따로 지정 필요할듯)

'''
