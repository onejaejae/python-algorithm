def solution(citations):

    length = len(citations)
    citations.sort()

    for i in range(length, 0, -1):
        for j in range(length):
            if citations[j] >= i:
                if length - j >= i and j <= i:
                    return i
                else:
                    break
    return 0


print(solution([0, 1, 1]))
