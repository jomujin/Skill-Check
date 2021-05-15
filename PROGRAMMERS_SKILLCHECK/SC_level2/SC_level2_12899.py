# 124 나라의 숫자
# 효율성 통과, 정확성 테스트 2,4,5,6,8,11 실패
# 실패 이유 : 나머지가 0일 경우 예외상황 발생하기 때문
# 나머지가 0일경우 


def solution(n):
    t_list = [0]
    num = 0
    count = 0
    answer = ''
    while True:
        if n > num:
            count += 1
            num += 3**count
            t_list.append(num)

        else:
            for i in range(count, 0, -1):
                
                if i == 1:
                    x = (n / 1) - 1
                else:
                    if (n - t_list[i-1]) % (3**(i-1)) != 0:
                        x =  (n - t_list[i-1]) // (3**(i-1))
                    else:
                        x = (n - t_list[i-1]) // (3**(i-1)) - 1

                print(n, i, x)

                if x == 0:
                    answer = answer + '1'
                elif x == 1:
                    answer = answer + '2'
                else:
                    answer = answer + '4'
            
                n -= (3**(i-1) * (x+1))

            break

    return answer

# print(solution(28))
# print(solution(40))
print(solution(513))

'''
타인 풀이

def change124(n):
    num = ['1','2','4']
    answer = ""


    while n > 0:
        # n - 1 하고 3으로 나눈 나머지가 맞는 이유는 모지?
        n -= 1 
        answer = num[n % 3] + answer
        n //= 3

    return answer

'''