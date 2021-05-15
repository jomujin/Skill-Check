# 스킬트리
# 스킬의 순서를 확인할 수 있게 dict로 만들고
# 스킬의 idx가 순서대로 진행되지 않을경우 skill_trees에서 삭제
# 단 for문의 skill_trees를 [::] copy로 하지않을경우 리스트의 값이 사라지면서 
# 반복문이 진행되어 정답이 되지않음


def solution(skill, skill_trees):
    
    skill_sort = dict((s, idx) for idx, s in enumerate(skill))
    for i in skill_trees[::]:
        old_num = 0
        for j in i:
            if j in skill_sort.keys():
                if old_num == skill_sort[j]:
                    old_num += 1
                else:
                    skill_trees.remove(i)
                    break

    answer = len(skill_trees)           
    return answer

# print(solution("CBD", ["BACDE", "CBADF", "AECB", "BDA"])) # 2
# print(solution("CBD", ["CAD"])) # 0
# print(solution("REA", ["REA", "POA"])) # 1
# print(solution("CBD", ["AEF", "ZJW"])) # 2
print(solution("CBDK", ["BD", "AECD"])) # 0
print(solution("CBDK", ["AECD"])) # 0
# print(solution("CBDK", ["CB", "CXYB", "BD", "AECD", "ABC", "AEX", "CDB", "CBKD", "IJCB", "LMDK"])) # 4
# print(solution("BDC", ["AAAABACA"])) # 0
# print(solution("CBD", ["C", "D", "CB", "BDA"])) # 2


'''
타인풀의

def solution(skill, skill_trees):
    answer = 0

    for skills in skill_trees:
        skill_list = list(skill)

        for s in skills:
            if s in skill:
                if s != skill_list.pop(0):
                    break
        else:
            answer += 1

    return answer
    '''