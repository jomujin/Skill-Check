# 괄호 변환
# 괄호가 바르게 짝지어졌다는 것은 '(' 문자로 열렸으면 반드시 짝지어서 ')' 문자로 닫혀야 한다는 뜻입니다. 예를 들어

# ()() 또는 (())() 는 올바른 괄호입니다.
# )()( 또는 (()( 는 올바르지 않은 괄호입니다.
# '(' 또는 ')' 로만 이루어진 문자열 s가 주어졌을 때, 문자열 s가 올바른 괄호이면 true를 return 하고, 올바르지 않은 괄호이면 false를 return 하는 solution 함수를 완성해 주세요.

# def solution(priorities, location):
#     answer = sorted(priorities)
#     print(answer[location])

# solution([2, 1, 3, 2], 2)
# solution([1, 1, 9, 1, 1, 1], 0)


def solution(a):
    alist= []
    if a[0] == ')' or a[-1] == '(': 
        print("올바르지 않은 괄호입니다. (조건1)") # 조건1. ')'로 시작하거나 '('로 끝나면 안된다.
        return False

    elif len(a) % 2 == 1: 
        print("올바르지 않은 괄호입니다. (조건2)") # 조건2. ()짝이 맞아야 하므로 개수는 짝수여야 한다.
        return False 

    else:
        # alist = list(a[i] for i in range(len(a)))
        for i in range(len(a)):
            alist.append(a[i])
            if a[i] == ')':
                if alist.count('(') < alist.count(')'):
                    print("올바르지 않은 괄호입니다. (조건3)") # 조건3. ')'이 나올경우 그 이전의 '(' 개수와 ')'의 차이가 1개 나야한다. '('가 1개 더 많아야한다.
                    return False

        if alist.count('(') != alist.count(')'): 
            print("올바르지 않은 괄호입니다. (조건4)") # 조건4. '('와 ')' 개수가 동일해야 한다.
            return False
        else:
            print(a)
            return True
    

solution(")(")
solution("(()")
solution("((()")
solution("(())")
solution("()))((()")
solution("()(())")
solution("()()()")
solution("(()())")

'''
# 괄호 변환 재풀이

# 균형잡힌 괄호('(' 와 ')'의 개수가 같을경우) 올바른 괄호 문자열 변환 과정

# 1. 입력이 빈 문자열인 경우, 빈 문자열을 반환합니다. 

# 2. 문자열 w를 두 "균형잡힌 괄호 문자열" u, v로 분리합니다. 
# 단, u는 "균형잡힌 괄호 문자열"로 더 이상 분리할 수 없어야 하며, 
# v는 빈 문자열이 될 수 있습니다. 

# 3. 문자열 u가 "올바른 괄호 문자열" 이라면 문자열 v에 대해 1단계부터 다시 수행합니다. 
#   3-1. 수행한 결과 문자열을 u에 이어 붙인 후 반환합니다. 

# 4. 문자열 u가 "올바른 괄호 문자열"이 아니라면 아래 과정을 수행합니다. 
#   4-1. 빈 문자열에 첫 번째 문자로 '('를 붙입니다. 
#   4-2. 문자열 v에 대해 1단계부터 재귀적으로 수행한 결과 문자열을 이어 붙입니다. 
#   4-3. ')'를 다시 붙입니다. 
#   4-4. u의 첫 번째와 마지막 문자를 제거하고, 나머지 문자열의 괄호 방향을 뒤집어서 뒤에 붙입니다. 
#   4-5. 생성된 문자열을 반환합니다.

# 1차 시도 20점
# 2차 시도 통과
# 과정 4번을 잘못이해함, return의 계산 순서 바꾸니 통과


# 균형잡힌 문자열 여부 판단
def check1(w):
    if w == '': return True
    if w.count('(') != w.count(')'): return False
    return True


# 올바른 괄호 문자열 여부 판단
def check2(w):
    if check1(w) == True:
        x, y = 0, 0
        for i in w:
            if i == '(': x += 1
            else: y += 1
            if x < y: return False
        return True


# 문자 위치 전환
def changes(w):
    result = ''
    for i in w:
        if i == ')': result += '('
        else: result += ')'
    return result


def solution(P):
    if P == '': return ''
    if check2(P) == True: return P
    u, v = '', ''

    for i in range(1, len(P)):
        if check1(P[:i]) == True:
            u, v = P[:i], P[i:]
            break
        u, v = P, ''

    # print('u는 {}, v는 {}'.format(u, v))

    if check2(u) == True:
        return u + solution(v)
    else:
        return '(' + solution(v) + ')' + changes(u[1:-1]) 


print(solution(")("))
print(solution("(()())()"))
print(solution("()))((()"))
print(solution("()))((()))(("))
print(solution(")()()()("))

'''

'''
타인풀이

def solution(p):
    if p=='': return p
    r=True; c=0
    for i in range(len(p)):
        if p[i]=='(': c-=1
        else: c+=1
        if c>0: r=False
        if c==0:
            if r:
                return p[:i+1]+solution(p[i+1:])
            else:
                return '('+solution(p[i+1:])+')'+''.join(list(map(lambda x:'(' if x==')' else ')',p[1:i]) ))

'''