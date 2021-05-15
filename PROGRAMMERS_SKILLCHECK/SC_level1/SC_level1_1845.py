# 폰켓몬
# 1차 시도 통과
# 문제는 길었지만, 내용은 단순함
# 포켓몬이 들어있는 연구실(nums)에 총 N(len(nums))마리의 포켓몬중 N/2만 가져갈 수 있음
# 근데 중복된 포켓몬(동일종)들이 있으며 중복된 포켓몬일 경우 그 중 한마리만 가져갈 수 있을때
# 가장 많이 가져갈수 있는 수는
# 경우의 수를 할 필요 없이
# len(nums)//2 최대로 가져갈 수 있는 포켓몬의 숫자와
# nums에 있는 중복된 포켓몬들을 정리한 set(nums) 숫자중에 작은 값
# 왜냐하면 최대로 가져갈 수 있는 포켓몬의 숫자보다 set(nums)가 클 경우 
# 어차피 len(nums)//2 만큼만 가져갈 수 있으므로


def solution(nums):
    s_nums = set(nums)
    if len(nums) // 2 < len(s_nums):
        return len(nums) // 2
    return len(s_nums)

print(solution([3,1,2,3]))
print(solution([3,3,3,2,2,4]))
print(solution([3,3,3,2,2,2]))


'''
타인 풀이

def solution(ls):
    return min(len(ls)/2, len(set(ls))

    ** 위의 공식이 둘 중 작은값을 구하는 식이므로 간략해 짐
'''