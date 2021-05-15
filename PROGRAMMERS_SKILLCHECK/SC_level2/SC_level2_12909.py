# 올바른 괄호
# 1차 시도 통과 (정확성, 효율성)
# SC_level2_22.py에서 상위호환의 문제에서 이미 만든 방법으로
# 올바른 괄호의 확인 process는 
# 1. '('와 ')'의 개수가 일치해야 하고
# 2. ')'가 나왔을때 그 이전에 '(' 개수와 현재 ')'의 개수가 len('(') >= len(')') 이어야 한다


def solution(s):
    if s.count('(') != s.count(')'): return False

    x, y = 0, 0
    for i in s:
        if i == '(': x += 1
        else: y += 1
        if x < y: return False
    
    return True

print(solution("()()"))
print(solution("(())()"	))
print(solution(")()("))
print(solution("(()("))
