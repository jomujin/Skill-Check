# 가운데 글자 가져오기
#  1차 시도 통과


def solution(s):
    half = len(s) // 2
    if len(s) % 2 == 0:
        return s[half-1:half+1]
    return s[half]

print(solution("abcde"))
print(solution("we"))

# class로 만들어서 해보기
# return 이 안됨
class Word:
    def __init__(self, word):
        self.word = word
        self.half = len(self.word) // 2

    def mid(self):
        if len(self.word) % 2 == 0:
            answer = self.word[self.half-1:self.half+1]
        else:
            answer = self.word[self.half]
        return answer

def solution_2(s):
    word = Word(s)
    return word.mid()

print(solution_2("abcde"))
print(solution_2("we"))


'''
타인풀이

def string_middle(str):
    return str[(len(str)-1)//2:len(str)//2+1]
    
    # 만약 len(str) == 5 라면
    # (5-1)//2 : 5//2+1
    # 2 : 3
    # 만약 len(str) == 4 라면
    # (4-1)//2 : 4//2+1
    # 1 : 3
    # 홀수일땐 [2:3]처럼 가운데 한칸이 되고 
    # 짝수일땐 [1:3]처럼 가운데 두칸이 된다

'''