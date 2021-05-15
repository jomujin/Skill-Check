# 2016년
# 1차 시도 통과
# datetime module 이용 


import datetime as dt
import calendar as cal

def solution(a, b):
    weeklist = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
    answer = weeklist[(dt.date(2016, a, b).weekday())]
    return answer
    

print(solution(5, 24))

# datetime을 쓰지 않고 푼다면

def solution_2(a, b):
    months = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    weeks = ['THU', 'FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED']
    # 2016-01-01이 금요일이므로 금요일부터

    for i in range(a-1):
        b += months[i]
    return weeks[b % 7]
    # 한줄로 풀면
    # return days[(sum(months[:a-1])+b) % 7]

print(solution_2(1, 1))
