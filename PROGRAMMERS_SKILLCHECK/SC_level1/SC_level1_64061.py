# 크레인 인형뽑기 게임
# 정답 아래 타인답안보다 테스트 4만 빼고 결과도출 시간 및 용량 유리


def solution(board, moves):
    box = [0]
    N = len(board)
    answer = 0
    for i in moves:
        for j in range(N):
            # 0 비었을 경우 계속 진행
            if board[j][i-1] == 0:
                continue
            # 인형이 있을경우
            else:
                # 바구니에 인형이 1개 이상 있고 마지막으로 쌓여있는 인형과 넣으려는 인형이 동일할때 
                if board[j][i-1] == box[-1]:
                    board[j][i-1] = 0
                    answer += 2
                    box.pop(-1)
                    break
                # 바구니에 인형이 1개 이상 있고 마지막으로 쌓여있는 인형과 넣으려는 인형이 다를때
                else:
                    box.append(board[j][i-1])
                    board[j][i-1] = 0
                    break

    print(board)
    print(box)

    return answer


'''
타인풀이

def solution(board, moves):
    stacklist = []
    answer = 0

    for i in moves:
        for j in range(len(board)):
            if board[j][i-1] != 0:
                stacklist.append(board[j][i-1])
                board[j][i-1] = 0

                if len(stacklist) > 1:
                    if stacklist[-1] == stacklist[-2]:
                        stacklist.pop(-1)
                        stacklist.pop(-1)
                        answer += 2     
                break

    return answer
'''

print(solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]], [1,5,3,5,1,2,1,4]))