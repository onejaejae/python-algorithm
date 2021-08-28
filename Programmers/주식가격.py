from collections import deque


def solution(prices):
    queue = deque(prices)
    answer = []

    while queue:
        first = queue.popleft()
        sec = 0
        for x in queue:
            sec += 1
            if first > x:
                answer.append(sec)
                break
        else:
            answer.append(sec)
    print(answer)


solution([1, 2, 3, 2, 3])
