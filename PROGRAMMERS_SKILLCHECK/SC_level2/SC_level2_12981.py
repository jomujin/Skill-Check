# 영어 끝말잇기
# 1차 시도 통과 (정리 필요)


def solution(n, words):
    words_ = []
    man = 1
    round_ = 1

    # while문으로 words list의 요소가 있을경우 진행
    while words:
        # 해당 loop 작성중의 문제는 해당 요소를 다음 요소값과 비교하는것
        # 따라서 len(words) > 1로 하면 끝말잇기 규칙의 만족 여부는 확인가능하지만
        # 동시에 이전에 등장했던 단어의 여부를 확인할 수 없음
        # 이러한 문제점 때문에 마지막 요소에서는 이미 이전 순서에서 끝말잇기 규칙은 확인 되었으므로
        # 이전에 등장한 단어 여부만 확인함
        if len(words) == 1:
            a = words[0]
            if a in words_:
                answer = [man, round_]
                return answer
            else:
                return [0,0]

        else:
            a = words[0]
            # 단어가 이전에 등장했던 단어인지 확인
            if a in words_:
                answer = [man, round_]
                return answer
            words_.append(a)

            # 끝말잇기 알파벳 확인
            if words[1][0] == a[-1]:
                if man == n:
                    man = 1
                    round_ += 1
                else:
                    man += 1
            else:
                if man == n:
                    man = 1
                    round_ += 1
                else:
                    man += 1
                answer = [man, round_]
                return answer
            words.pop(0)


# print(solution(3, ['tank', 'kick', 'know', 'wheel', 'land', 'dream', 'mother', 'robot', 'tank']))
print(solution(2, ["hello", "one", "even", "never", "now", "world", "draw"]))


'''
타인풀의
for문으로 진행하며 1, len(words)로 하여 나의 문제점을 해결
동시에 이전 등장 여부를 words[p] in words[:p]로 해결
또한 return 값을 p%n + 1, p//n + 1로 단순화 시킴

def solution(n, words):
    for p in range(1, len(words)):
        if words[p][0] != words[p-1][-1] or words[p] in words[:p]:
            return [(p%n)+1, (p//n)+1]
        else:
            return [0, 0]

'''