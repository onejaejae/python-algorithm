import heapq


def solution(scoville, K):
    heapq.heapify(scoville)
    cnt = 0

    while True:
        if scoville[0] >= K:
            break

        x = heapq.heappop(scoville)
        if len(scoville) == 0:
            return -1
        y = heapq.heappop(scoville)
        heapq.heappush(scoville, x + (2*y))
        cnt += 1

    return cnt


solution([1, 2, 3, 9, 10, 12], 7)
