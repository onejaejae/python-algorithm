import heapq

# 삽입을 할 때 정수형으로 변경을 해서 넣는데
# 그 이유는 음수값들도 들어가기 때문에
# 정렬을 하기 위해서는 정수형으로 바꾸는 것이 필수적이기 때문이다.


def solution(operations):
    heap = []
    answer = []
    for x in operations:
        tmp = x.split()
        num = tmp[1]
        commend = tmp[0]
        if commend == "I":
            heapq.heappush(heap, int(num))
        else:
            if len(heap) == 0:
                continue
            elif num == "1":
                heap.pop()
            elif num == "-1":
                heapq.heappop(heap)
        heap.sort()
    if heap:
        return [int(heap.pop()), int(heapq.heappop(heap))]
    else:
        return [0, 0]


solution(["I 4", "I -1", "I 6", "I 3"])
