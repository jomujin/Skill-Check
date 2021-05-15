# 이중우선순위큐


import heapq as hp

def solution(operations):
    num = []
    for o in operations:
        if 'I' in o:
            num.append(int(o[2:]))
        elif o == 'D 1' and len(num) > 0: # 최대값
            heap = []
            for h in num:
                hp.heappush(heap, (-h, h))
            n = hp.heappop(heap)[1]
            num.remove(n)

        elif o == 'D -1' and len(num) > 0: # 최소값
            heap = []
            for h in num:
                hp.heappush(heap, h)
            n = hp.heappop(heap)
            num.remove(n)

    if len(num) == 0:
        return [0,0]
    elif len(num) == 1:
        return [max(num)]
    else:
        return [max(num), min(num)]