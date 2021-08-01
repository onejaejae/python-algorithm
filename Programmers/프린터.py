from collections import deque

Deque = deque()


def solution(priorities, location):
    result = []

    for i in range(len(priorities)):
        Deque.append((priorities[i], i))

    while Deque:
        tmp = Deque.popleft()
        if len(Deque) <= 0:
            result.append(tmp[1])
            break
        if tmp[0] >= max(Deque)[0]:
            result.append(tmp[1])
        else:
            Deque.append(tmp)

    answer = result.index(location)
    print(answer + 1)
    return answer


solution([1, 1, 9, 1, 1, 1]	, 0)
