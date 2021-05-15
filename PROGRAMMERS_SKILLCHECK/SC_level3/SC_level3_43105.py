# 정수 삼각형
# 삼각형의 높이는 1 이상 500 이하 
# 삼각형을 이루고 있는 숫자는 0 이상 9999 이하의 정수


def solution(triangle):
    t_h = len(triangle)
    t_w = [ [0 for _ in range(layer+1)] for layer in range(t_h) ]
    print(t_w)

    t_w[0][0] = triangle[0][0]
    print(t_w)
    for layer in range(1, t_h):
        print(layer)     
        for room in range(layer+1):
            if room == 0:
                    t_w[layer][room] = triangle[layer][room] + t_w[layer-1][room]
            elif room == layer:
                    t_w[layer][room] = triangle[layer][room] + t_w[layer-1][room-1]
            else: 
                    t_w[layer][room] = triangle[layer][room] + max(t_w[layer-1][room-1], t_w[layer-1][room])

    print(t_w) # 보면 
    return max(t_w[t_h-1])
    
print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))

'''
타인풀이
# solution = lambda t, l = []: max(l) if not t else solution(t[1:], [max(x,y)+z for x,y,z in zip([0]+l, l+[0], t[0])])

'''